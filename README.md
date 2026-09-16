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
│       ├── .gitkeep
│       ├── mesa-stem-diseno-entornos-educativos-interactivos.html
│       ├── de-la-robotica-educativa-a-la-impresion-creativa.html
│       ├── educar-en-el-uso-de-la-tecnologia-no-simplemente-prohibirla.html
│       ├── cuando-no-hay-internet-el-problema-no-es-ensenar.html
│       ├── por-que-los-estudiantes-si-quieren-aprender.html
│       ├── lo-que-he-aprendido-sobre-impresion-3d.html
│       ├── linux-nunca-habia-sido-tan-importante-como-ahora.html
│       ├── un-ano-despues-asi-cambio-mi-forma-de-crear-proyectos.html
│       ├── tipos-de-inteligencia-artificial-aplicada.html
│       ├── mujeres-lenguaje-y-vocaciones-en-ingenieria.html
│       ├── lo-que-aprendimos-creando-nuestro-primer-robot.html
│       ├── robotica-educativa-puente-entre-curiosidad-e-innovacion.html
│       ├── robotica-educativa-a-investigacion-aplicada.html
│       ├── construyendo-proyectos-de-internet.html
│       ├── ojo-animatronico-con-esp32.html
│       └── arana-robotica-con-esp32.html
└── assets/
    ├── css/
    │   └── styles.css
    ├── js/
    │   ├── main.js
    │   └── blog.js
    └── img/
        ├── .gitkeep
        ├── perfil.jpg
        ├── mesa-stem/
        │   ├── .gitkeep
        │   └── portada.jpg
        └── blog/
            ├── .gitkeep
            ├── mesa-stem/.gitkeep
            ├── impresion-3d/.gitkeep
            ├── proyectos/.gitkeep
            └── robotica/.gitkeep
```

El sitio no necesita instalación, compilación ni backend. Puede abrirse con `index.html` o servirse como archivos estáticos. Las rutas a CSS, JavaScript e imágenes son relativas y compatibles con GitHub Pages.

## GitHub Pages

Publicar estos archivos en la raíz de la rama configurada en **Settings → Pages** del repositorio `lelyliliana/lelyliliana.com`. Conservar el archivo `CNAME` original y la configuración del dominio personalizado. No se requiere un flujo de compilación.

## Blog

El índice contiene 16 tarjetas: “Educar en el uso de la tecnología, no simplemente prohibirla” está migrado íntegramente a partir del texto suministrado por la autora, con fecha julio de 2026 (`datetime="2026-07"`, sin día inventado). También está migrado íntegramente “Cuando no hay internet, el problema no es enseñar… es con qué hacerlo”, con fecha 2026 (`datetime="2026"`, sin mes ni día inventados), nota final y enlace al video suministrado. También está migrado “Por qué los estudiantes sí quieren aprender… pero no como creemos”, con fecha marzo de 2026 (`datetime="2026-03"`). Está migrado también “Llevo más de veinte años usando Linux… pero nunca había sido tan importante como ahora”, con fecha junio de 2026 (`datetime="2026-06"`). Las otras 12 fichas siguen pendientes de contenido. No se ha accedido ni modificado Google Sites.

Los títulos se han recuperado de los nombres de archivo indicados; los dos proyectos usan los títulos expresos suministrados. Las categorías son una organización temática inicial basada en esos títulos y deben revisarse con los textos originales. Los cuatro artículos migrados tienen fecha, metadatos y extractos derivados del contenido suministrado. El índice muestra julio, junio y marzo de 2026, seguidos del artículo que solo tiene año; la posición temporal exacta de este último no puede determinarse sin su mes. “Últimos artículos” conserva únicamente las tres tarjetas con mes conocido más reciente: julio, junio y marzo. Las fichas sin fecha quedan después. La navegación sigue la secuencia solicitada por la autora: “Educar…” → “Cuando no hay internet…” → “Por qué los estudiantes…” → “Llevo más de veinte años usando Linux…”, con enlaces recíprocos anterior/siguiente. Esta secuencia es independiente de la ordenación de tarjetas por fecha. No se enlazan fichas pendientes como siguientes de los artículos publicados.

`assets/js/blog.js` controla exclusivamente los filtros accesibles del índice. Sin JavaScript todas las tarjetas permanecen visibles. `assets/js/main.js` mantiene menú y tema compartidos. Los artículos usan `../../assets/`, `../../index.html` y `../index.html` para volver al blog. Las imágenes se reservan bajo `assets/img/blog/` y no se insertan etiquetas de imagen hasta disponer de archivos reales.

### Incorporar cada artículo

1. Pegar el contenido original completo en `.article-body`, conservando párrafos, encabezados, listas y referencias.
2. Confirmar título y categorías; actualizar la ficha, tarjeta, breadcrumb, metadatos y enlaces anterior/siguiente cuando corresponda.
3. Completar `meta description` y `og:description` solo con información suministrada o validada por la autora; los comentarios señalan las ubicaciones pendientes.
4. Incorporar la fecha original con `<time datetime="AAAA-MM-DD">` en artículo e índice cuando se suministre. Ordenar manualmente las tarjetas por fecha descendente, dejando al final los artículos aún sin fecha, y actualizar anterior/siguiente de forma coherente.
5. Añadir la imagen opcional solo si existe, con texto alternativo y dimensiones reales. Retirar el aviso de migración del artículo y de su tarjeta al incorporar el texto.

La portada de la serie “Construyendo Proyectos de Internet” enlaza a los dos proyectos ESP32; cada proyecto incluye un enlace de regreso a la serie. “Proyectos publicados” conserva el encabezado solicitado y los avisos de migración aclaran el estado de sus fichas.

El artículo narrativo de Mesa STEM es independiente de la ficha bibliográfica y enlaza a ella mediante “Información editorial del libro”. Incluye también “Conocer y adquirir el libro”, que abre la URL oficial de ECOE en otra pestaña. Su cuerpo sigue pendiente de migración y aún no se ha añadido el enlace de regreso desde la ficha editorial. “Últimos artículos” muestra únicamente los tres artículos reales más recientes según las fechas disponibles.

## Publicaciones

`publicaciones/` contiene páginas individuales de publicaciones. `publicaciones/mesa-stem.html` presenta la ficha bibliográfica, descripción y DOI de Mesa STEM. La tarjeta de la portada enlaza a esta página mediante “Conocer el libro”. Se reutilizan los estilos y el JavaScript generales, con rutas relativas `../assets/`, `../blog/` y `../index.html#seccion`.

## Actualizar el contenido

- Editar los textos y enlaces en `index.html`.
- Ajustar colores y estilos en `assets/css/styles.css`.
- La fotografía del hero está en `assets/img/perfil.jpg`. El archivo original permanece intacto. El encuadre se ajusta solo mediante CSS: marco de hasta 340 px en escritorio y 260 px en móvil, proporción cuadrada, `object-fit: cover` y `object-position: center top` para priorizar rostro y hombros sin cortar la cabeza.
- La portada oficial de Mesa STEM está en `assets/img/mesa-stem/portada.jpg`, extraída del frente de la cubierta PDF, sin lomo, contraportada ni marcas de imprenta. Se muestra completa en la tarjeta y la ficha del libro. Al sustituir imágenes, actualizar sus atributos `width` y `height` si cambian las dimensiones. El botón “Ver en ECOE Ediciones” de la ficha enlaza a `https://ecoeediciones.com/product/mesa-stem-2/` y usa `target="_blank"` y `rel="noopener noreferrer"`.
- Reemplazar “Próximamente” por enlaces a recursos únicamente cuando estén disponibles.

El modo claro es el inicial. La preferencia de tema se guarda en `localStorage` cuando está disponible. El contenido y la navegación siguen accesibles sin JavaScript; el menú móvil desplegable y el cambio de tema requieren JavaScript. Se respeta la preferencia de movimiento reducido.
