# lelyliliana.com

Sitio web personal y profesional de Leli Liliana Díaz Izquierdo.

## Tecnologías

- HTML5
- CSS3
- JavaScript
- GitHub Pages

## Dominio

https://lelyliliana.com

## Estructura

```text
/
├── index.html
├── CNAME                  # Dominio existente; no modificar
├── README.md
├── publicaciones/
│   └── mesa-stem.html
├── blog/
│   ├── index.html
│   └── articulos/
│       └── .gitkeep
└── assets/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── main.js
    └── img/
        ├── .gitkeep
        ├── perfil.jpg
        └── mesa-stem/
            ├── .gitkeep
            └── portada.jpg
```

El sitio no necesita instalación, compilación ni backend. Puede abrirse con `index.html` o servirse como archivos estáticos. Las rutas a CSS, JavaScript e imágenes son relativas y compatibles con GitHub Pages.

## GitHub Pages

Publicar estos archivos en la raíz de la rama configurada en **Settings → Pages** del repositorio `lelyliliana/lelyliliana.com`. Conservar el archivo `CNAME` original y la configuración del dominio personalizado. No se requiere un flujo de compilación.

## Blog

`blog/index.html` será la nueva ubicación de los artículos previamente publicados en Google Sites. Esta primera ampliación solo prepara seis tarjetas de artículos y tres tarjetas en la portada: no migra ni modifica los blogs anteriores ni crea artículos reales. `blog/articulos/` queda reservado para la migración posterior.

Ambas páginas comparten `assets/css/styles.css` y `assets/js/main.js`. Desde el blog se usan rutas `../assets/` y `../index.html#seccion` para volver a la portada. Los archivos `.gitkeep` conservan las carpetas vacías en Git.

## Publicaciones

`publicaciones/` contiene páginas individuales de publicaciones. `publicaciones/mesa-stem.html` presenta la ficha bibliográfica, descripción y DOI de Mesa STEM. La tarjeta de la portada enlaza a esta página mediante “Conocer el libro”. Se reutilizan los estilos y el JavaScript generales, con rutas relativas `../assets/`, `../blog/` y `../index.html#seccion`.

## Actualizar el contenido

- Editar los textos y enlaces en `index.html`.
- Ajustar colores y estilos en `assets/css/styles.css`.
- La fotografía del hero está en `assets/img/perfil.jpg`. Se conserva su proporción original con `object-fit: cover` y texto alternativo descriptivo.
- La portada oficial de Mesa STEM está en `assets/img/mesa-stem/portada.jpg`, extraída del frente de la cubierta PDF, sin lomo, contraportada ni marcas de imprenta. Se muestra completa en la tarjeta y la ficha del libro. Al sustituir imágenes, actualizar sus atributos `width` y `height` si cambian las dimensiones. El botón “Ver en ECOE Ediciones” de la ficha conserva `href="#"` y está deshabilitado mientras no exista una URL oficial exacta. Al añadirla, retirar `aria-disabled`, `tabindex`, `aria-describedby`, la clase `pending-link` y el aviso `#book-link-status`; añadir `target="_blank"` y `rel="noopener noreferrer"` al enlace externo.
- Reemplazar “Próximamente” por enlaces a recursos únicamente cuando estén disponibles.

El modo claro es el inicial. La preferencia de tema se guarda en `localStorage` cuando está disponible. El contenido y la navegación siguen accesibles sin JavaScript; el menú móvil desplegable y el cambio de tema requieren JavaScript. Se respeta la preferencia de movimiento reducido.
