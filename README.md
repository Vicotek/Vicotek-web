# vicotek.app

Web corporativa de Vicotek: webs integradas con flujos profundos y agentes de IA.

Sitio estático (HTML + CSS + JS, sin compilación), pensado para alojarse en Hostinger con despliegue automático desde este repositorio.

## Estructura

```
index.html          Página principal
privacidad.html     Política de privacidad (pendiente de texto)
aviso-legal.html    Aviso legal (pendiente de texto)
.htaccess           HTTPS + www, caché y compresión (Apache/Hostinger)
assets/
  styles.css        Estilos — colores de marca en las variables :root
  main.js           Menú móvil y animaciones
  favicon.svg
```

## Cambios habituales

- **Colores:** edita `--accent`, `--bg`, etc. al principio de `assets/styles.css`.
- **Textos:** directamente en `index.html`.
- **Foto del equipo:** sube `assets/jose-antonio.jpg` y sigue el comentario en la sección `#equipo`.
- **Métricas de casos:** busca `[+X%]` y `[X h]` en `index.html`.

## Ver en local

Abre `index.html` en el navegador, o:

```bash
python3 -m http.server 8000
```

## Despliegue

Ver [DEPLOY.md](DEPLOY.md).
