# Despliegue en Hostinger desde GitHub

## 1. Conectar el repositorio (una sola vez)

1. Entra en **hPanel → Sitios web → vicotek.app → Avanzado → Git**.
   - Si `vicotek.app` aún no está añadido en Hostinger, primero **Añadir sitio web** con ese dominio.
2. En **Crear un nuevo repositorio**:
   - Repositorio: `https://github.com/Vicotek/vicotek-web.git`
   - Rama: `main`
   - Directorio: déjalo **vacío** (instala en `public_html`).
   - Si el directorio `public_html` no está vacío, borra antes su contenido (p. ej. el `default.php` de Hostinger).
3. Pulsa **Crear** y luego **Desplegar**.

## 2. Despliegue automático en cada cambio

1. En la misma pantalla de Git, pulsa **Despliegue automático** y copia la **URL del webhook**.
2. En GitHub: **Vicotek/vicotek-web → Settings → Webhooks → Add webhook**
   - Payload URL: la URL copiada
   - Content type: `application/json`
   - Evento: *Just the push event*
3. A partir de ahora, cada `git push` a `main` actualiza la web.

## 3. Apuntar el dominio a Hostinger (salir de GHL)

> Hazlo cuando la web ya se vea bien en la URL temporal de Hostinger.

1. En hPanel, mira los **nameservers** o la **IP** que indica Hostinger para el sitio.
2. Donde esté registrado el dominio `vicotek.app` (registrador):
   - **Opción A (recomendada):** cambia los nameservers a los de Hostinger (`ns1.dns-parking.com`, `ns2.dns-parking.com` — confirma en hPanel).
   - **Opción B:** deja los nameservers y cambia los registros:
     - `A` `@` → IP de Hostinger
     - `CNAME` `www` → `vicotek.app` (o la IP como registro A)
   - Elimina los registros antiguos que apuntaban a GoHighLevel (suelen ser un `A` o `CNAME` hacia LeadConnector/GHL).
3. ⚠️ Si usas el dominio para **email** o para **envíos desde GHL** (registros MX, SPF, DKIM, subdominios tipo `mail.` o `link.`), **cópialos tal cual** en la nueva zona DNS antes de cambiar los nameservers.
4. En GHL: **Settings → Domains**, desvincula `vicotek.app` de la web antigua (no borres el calendario: el botón “Reservar demo” sigue usando el widget de GHL).
5. En hPanel → **Seguridad → SSL**, activa el certificado gratuito. La propagación DNS tarda de minutos a 24 h.
