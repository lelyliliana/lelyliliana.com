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
├── index.html             # Contenido y estructura semántica
├── CNAME                  # Dominio existente; no modificar
├── README.md
└── assets/
    ├── css/styles.css     # Diseño responsive y temas claro/oscuro
    ├── js/main.js         # Menú, tema persistente y navegación activa
    └── img/.gitkeep       # Espacio reservado para imágenes
```

El sitio no necesita instalación, compilación ni backend. Puede abrirse con `index.html` o servirse como archivos estáticos. Las rutas a CSS, JavaScript e imágenes son relativas y compatibles con GitHub Pages.

## GitHub Pages

Publicar estos archivos en la raíz de la rama configurada en **Settings → Pages** del repositorio `lelyliliana/lelyliliana.com`. Conservar el archivo `CNAME` original y la configuración del dominio personalizado. No se requiere un flujo de compilación.

## Actualizar el contenido

- Editar los textos y enlaces en `index.html`.
- Ajustar colores y estilos en `assets/css/styles.css`.
- Para agregar la fotografía, guardar `assets/img/perfil.jpg` y sustituir el contenedor `.portrait-placeholder` por la etiqueta `img` indicada en el comentario HTML. Mantener un texto alternativo descriptivo.
- Agregar los datos públicos verificados de Mesa STEM en `.publication-details`. No publicar documentación ni información sensible de proyectos institucionales.
- Reemplazar “Próximamente” por enlaces a recursos únicamente cuando estén disponibles.

El modo claro es el inicial. La preferencia de tema se guarda en `localStorage` cuando está disponible. El contenido y la navegación siguen accesibles sin JavaScript; el menú móvil desplegable y el cambio de tema requieren JavaScript. Se respeta la preferencia de movimiento reducido.
