# Despliegue: GitHub Pages (gratis) + dominio en Hostinger

La web se aloja gratis en GitHub Pages. Hostinger solo gestiona el dominio (DNS).
Cada `git push` a `main` publica los cambios automáticamente.

## 1. Activar GitHub Pages (una sola vez)

1. GitHub → **Vicotek/Vicotek-web → Settings → Pages**
2. *Build and deployment* → Source: **Deploy from a branch**
3. Branch: **main** · carpeta **/ (root)** → **Save**
4. *Custom domain*: `www.vicotek.app` → **Save** (el archivo `CNAME` del repo ya lo indica)

## 2. DNS en Hostinger (Dominios → vicotek.app → DNS)

Borra los registros antiguos que apuntan a GoHighLevel (A `@` y CNAME `www`) y crea:

| Tipo  | Nombre | Apunta a            |
|-------|--------|---------------------|
| A     | @      | 185.199.108.153     |
| A     | @      | 185.199.109.153     |
| A     | @      | 185.199.110.153     |
| A     | @      | 185.199.111.153     |
| CNAME | www    | vicotek.github.io   |

⚠️ No toques los registros **MX**, **TXT** (SPF/DKIM) ni subdominios de email/GHL (p. ej. `mail.`, `link.`, `msg.`).

## 3. HTTPS

Cuando GitHub verifique el dominio (de minutos a unas horas), en **Settings → Pages** marca **Enforce HTTPS**.
Los dominios `.app` exigen HTTPS, así que la web puede no abrir hasta que el certificado esté emitido.

## 4. GHL

En GHL → **Settings → Domains**, desvincula `vicotek.app` de la web antigua.
No borres el calendario: “Reservar demo” sigue usando el widget de GHL.

---

*Alternativa con hosting de Hostinger (de pago): hPanel → Sitios web → Avanzado → Git, repositorio `https://github.com/Vicotek/Vicotek-web.git`, rama `main`. En ese caso se usa el `.htaccess` incluido.*
