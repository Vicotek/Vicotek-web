#!/usr/bin/env python3
"""
Genera la web en todos los idiomas a partir de src/ + i18n/*.json.

  python3 build.py

- Castellano (es) va en la raíz:  /index.html, /privacidad.html, /aviso-legal.html
- El resto en su carpeta:         /en/, /da/, /ca/

Para cambiar un texto: edita i18n/<idioma>.json y vuelve a ejecutar el script.
Para cambiar el diseño: edita src/index.html o assets/styles.css.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SITE = "https://www.vicotek.app/"

# Orden en el selector. El primero es el idioma por defecto (raíz).
LANGS = [
    ("es", "ES", "Castellano"),
    ("en", "EN", "English"),
    ("da", "DA", "Dansk"),
    ("ca", "CA", "Català"),
]
DEFAULT = LANGS[0][0]


def folder(code):
    return "" if code == DEFAULT else f"{code}/"


def render(template, values, where):
    def sub(m):
        key = m.group(1)
        if key not in values:
            sys.exit(f"Falta la clave '{key}' ({where})")
        return values[key]
    return re.sub(r"\{\{(\w+)\}\}", sub, template)


def switcher(current, base, label):
    links = []
    for code, short, name in LANGS:
        href = base + folder(code) if (base + folder(code)) else "./"
        cur = ' aria-current="true"' if code == current else ""
        links.append(
            f'        <a href="{href}" hreflang="{code}" lang="{code}" '
            f'title="{name}" data-set-lang="{code}"{cur}>{short}</a>'
        )
    return (
        f'      <div class="lang" role="group" aria-label="{html.escape(label)}">\n'
        + "\n".join(links)
        + "\n      </div>"
    )


def hreflang_tags():
    tags = [f'  <link rel="alternate" hreflang="{c}" href="{SITE}{folder(c)}">' for c, _, _ in LANGS]
    tags.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE}">')
    return "\n".join(tags)


def escena_block(base, vals):
    """Sección 'Detrás de escena': solo aparece cuando existe assets/img/escena-1.jpg."""
    if not (ROOT / "assets/img/escena-1.jpg").exists():
        return ""
    tiles = "\n".join(
        f'        <div class="ph"><img src="{base}assets/img/escena-{i}.jpg" alt="{vals["alt_scene"]}" '
        f'loading="lazy" onerror="this.remove()"></div>'
        for i in range(1, 5)
    )
    return f"""  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{vals["scene_eyebrow"]}</span>
        <h2 class="h2">{vals["scene_h2"]}</h2>
      </div>
      <div class="scenes reveal">
{tiles}
      </div>
    </div>
  </section>
"""


def main():
    index_tpl = (ROOT / "src/index.html").read_text(encoding="utf-8")
    legal_tpl = (ROOT / "src/legal.html").read_text(encoding="utf-8")

    for code, _, _ in LANGS:
        data = json.loads((ROOT / f"i18n/{code}.json").read_text(encoding="utf-8"))
        vals = {k: html.escape(v, quote=True) for k, v in data.items() if not k.startswith("_")}
        base = "" if code == DEFAULT else "../"
        out_dir = ROOT / folder(code)
        out_dir.mkdir(exist_ok=True)

        vals.update(
            lang=code,
            base=base,
            canonical=SITE + folder(code),
            hreflang=hreflang_tags(),
            lang_switcher=switcher(code, base, data["lang_aria"]),
        )
        vals["escena"] = escena_block(base, vals)
        (out_dir / "index.html").write_text(render(index_tpl, vals, f"{code}/index"), encoding="utf-8")

        for fname, title_key in (("privacidad.html", "privacy"), ("aviso-legal.html", "legal")):
            v = dict(vals, page_title=vals[title_key])
            (out_dir / fname).write_text(render(legal_tpl, v, f"{code}/{fname}"), encoding="utf-8")

        print(f"✓ {code}: /{folder(code)}")


if __name__ == "__main__":
    main()
