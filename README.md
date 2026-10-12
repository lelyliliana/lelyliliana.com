# lelyliliana.com

Sitio web personal y profesional de **Leli Liliana Díaz Izquierdo**, creado como espacio para compartir experiencias, proyectos, publicaciones y recursos relacionados con educación, ingeniería, tecnología, inteligencia artificial, robótica e investigación.

🌐 **Sitio web:** https://lelyliliana.com

## Contenido del sitio

El sitio está organizado en cuatro áreas principales:

- **Blog:** artículos, experiencias y reflexiones sobre educación, tecnología, inteligencia artificial, investigación y otros temas de interés.
- **Proyectos:** documentación de desarrollos, prototipos, experimentos y proyectos tecnológicos.
- **Recursos:** cursos, guías, ejemplos y materiales abiertos para estudiantes y personas interesadas en tecnología.
- **Publicaciones:** información sobre libros, artículos y otros productos académicos.

## Tecnologías

El sitio está desarrollado como una web estática utilizando:

- HTML5
- CSS3
- JavaScript
- GitHub Pages

No requiere backend, base de datos ni proceso de compilación.

## Estructura general

```text
/
├── index.html
├── CNAME
├── blog/
├── proyectos/
├── recursos/
├── publicaciones/
└── assets/
    ├── css/
    ├── js/
    └── img/
```

## Publicación

El sitio se publica mediante **GitHub Pages** desde este repositorio y utiliza el dominio personalizado:

**https://lelyliliana.com**

El archivo `CNAME` contiene la configuración necesaria para conservar el dominio personalizado.

## Sobre este repositorio

Este repositorio contiene el código fuente y los recursos públicos utilizados en el sitio web. El contenido se actualiza progresivamente con nuevos artículos, proyectos, publicaciones y materiales.

---

**Leli Liliana Díaz Izquierdo**  
Ingeniera de Sistemas · Docente · Investigadora

## Actualizar el catálogo de cursos

La página recursos/index.html contiene información y unidades directas de los cursos públicos de Aprende con Leli. El catálogo se genera como HTML estático: sus desplegables funcionan sin JavaScript.

Con una copia actualizada de aprende-con-leli junto a este repositorio, ejecuta desde la raíz:

```text
python scripts/sincronizar-cursos.py --fuente ../aprende-con-leli
```

El script utiliza el catálogo y las páginas de cursos de esa copia, registra su revisión en recursos/catalogo.json y conserva los enlaces complementarios de ejemplos e investigación. Antes de publicar, comprueba las nuevas unidades y la correspondencia con el sitio de aprendizaje.
