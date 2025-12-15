---
layout: default
title: Inicio
description: Documentación del proyecto web de Tintum.app
---

# Bienvenido a Tintum.app

Documentación del proyecto web de Tintum.app hosteado en Firebase.

## Información del Proyecto

- **Cuenta Firebase**: denis@tintum.app
- **Repositorio**: [GitHub](https://github.com/denis-tintumapp/tintum-app)
- **Hosting**: Firebase Hosting
- **Base de datos**: Firestore

## Estructura del Proyecto

```
tintum-app/
├── docs/              # Documentación (Markdown + Liquid)
│   ├── _includes/    # Plantillas Liquid
│   ├── _layouts/      # Layouts Liquid
│   └── _config.yml    # Configuración Jekyll
├── web/               # Archivos estáticos para hosting
│   ├── js/            # JavaScript
│   ├── css/           # Estilos
│   ├── images/        # Imágenes
│   ├── icons/         # Iconos PWA
│   └── index.html     # Página principal
├── firebase.json       # Configuración de Firebase
├── firestore.rules     # Reglas de seguridad de Firestore
└── firestore.indexes.json  # Índices de Firestore
```

## Guías Rápidas

{% assign guides = site.pages | where: "category", "guide" %}
{% if guides.size > 0 %}
<ul>
  {% for guide in guides %}
  <li><a href="{{ guide.url | relative_url }}">{{ guide.title }}</a></li>
  {% endfor %}
</ul>
{% else %}
- [Configuración Inicial]({{ '/configuracion-inicial' | relative_url }})
- [Despliegue]({{ '/despliegue' | relative_url }})
- [Desarrollo]({{ '/desarrollo' | relative_url }})
{% endif %}

## Última Actualización

{% assign last_update = site.time | date: "%d/%m/%Y" %}
Última actualización: {{ last_update }}

