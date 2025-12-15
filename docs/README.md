# Documentación Tintum.app

Esta carpeta contiene la documentación del proyecto usando Markdown y Liquid templates.

## Estructura

- `_config.yml` - Configuración de Jekyll/Liquid
- `_includes/` - Plantillas Liquid reutilizables
- `_layouts/` - Layouts para las páginas
- `*.md` - Páginas de documentación en Markdown

## Uso con Jekyll

Si quieres servir la documentación localmente con Jekyll:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

La documentación estará disponible en http://localhost:4000

## Variables Liquid Disponibles

- `site.title` - Título del sitio
- `site.description` - Descripción del sitio
- `page.title` - Título de la página actual
- `page.description` - Descripción de la página actual

## Agregar Nueva Documentación

1. Crea un archivo `.md` en la raíz de `docs/`
2. Agrega el front matter con `layout: default`
3. Escribe el contenido en Markdown
4. Usa includes de Liquid cuando sea necesario

Ejemplo:

```markdown
---
layout: default
title: Mi Nueva Página
---

# Contenido aquí
```

