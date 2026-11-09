# vicotek.app

Web corporativa de Vicotek: webs integradas con flujos profundos y agentes de IA.
Sitio estático publicado con GitHub Pages en 4 idiomas: castellano (`/`), inglés (`/en/`), danés (`/da/`) y catalán (`/ca/`).

## Cómo se edita

| Quiero cambiar…            | Edito…                                  |
|----------------------------|-----------------------------------------|
| Un texto                   | `i18n/es.json`, `en.json`, `da.json`, `ca.json` |
| La estructura / secciones  | `src/index.html`                        |
| Colores, tamaños           | `assets/styles.css` (variables `:root`) |
| Una foto                   | Sustituye el archivo en `assets/img/` con el **mismo nombre** |

Después de editar textos o `src/`, regenera las páginas y sube los cambios:

```bash
python3 build.py
git add -A && git commit -m "Actualiza textos" && git push
```

> No edites `index.html`, `en/`, `da/` ni `ca/` a mano: se generan con `build.py`.

## Fotos (`assets/img/`)

| Archivo                     | Dónde sale                 | Tamaño recomendado | Estado |
|-----------------------------|----------------------------|--------------------|--------|
| `hero.jpg`                  | Portada                    | 1100 × 880         | provisional |
| `sector-alimentacion.jpg`   | Sector alimentación        | 800 × 500          | provisional |
| `sector-vino.jpg`           | Sector vinicultores        | 800 × 500          | provisional |
| `sector-audiovisual.jpg`    | Sector audiovisual         | 800 × 500          | **falta** |
| `caso-isocore.jpg`          | Caso ISOCORE (vertical)    | 760 × 840          | provisional |
| `caso-bolighub.jpg`         | Caso Bolighub              | 900 × 520          | **falta** |
| `caso-envinat.jpg`          | Caso Envinat               | 900 × 520          | provisional |
| `jose-antonio.jpg`          | Equipo                     | 600 × 720          | ✓ |
| `escena-1.jpg` … `escena-4.jpg` | Sección "Detrás de escena" | 1 horizontal grande + 3 | **falta** |

- Si una foto falta, se muestra un recuadro limpio con un icono de cámara (no una imagen rota).
- La sección **"Detrás de escena"** aparece sola en cuanto exista `escena-1.jpg` (ejecuta `build.py` después de añadirla).
- Usa JPG de < 200 KB. Las fotos se recortan solas para encajar (`object-fit: cover`).
- Evita imágenes generadas con IA que tengan texto o logos deformados.

## Ver en local

```bash
python3 -m http.server 8000   # y abre http://localhost:8000
```

## Despliegue

Ver [DEPLOY.md](DEPLOY.md). Cada `git push` a `main` publica en https://www.vicotek.app
