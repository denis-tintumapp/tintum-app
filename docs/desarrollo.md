---
layout: default
title: Desarrollo Local
description: Guía para desarrollo local de Tintum.app
category: guide
---

# Desarrollo Local

Guía para desarrollar y probar Tintum.app localmente.

## Emuladores de Firebase

Firebase proporciona emuladores locales para probar sin afectar el entorno de producción.

### Iniciar Emuladores

```bash
firebase emulators:start
```

Esto iniciará:
- Hosting Emulator (puerto 5000)
- Firestore Emulator (puerto 8080)
- Y otros servicios configurados

### Acceder a los Emuladores

- **Hosting**: http://localhost:5000
- **Firestore UI**: http://localhost:4000
- **Emulator Suite UI**: http://localhost:4000

## Estructura de Desarrollo

### Archivos Principales

- `web/index.html` - Página principal
- `web/js/app.js` - Lógica principal de la aplicación
- `web/css/styles.css` - Estilos principales

### Agregar Nuevas Funcionalidades

1. Crea los archivos necesarios en `web/`
2. Actualiza `index.html` si es necesario
3. Prueba localmente con los emuladores
4. Haz commit y push a GitHub

## Scripts Útiles

### Generar Iconos

```bash
python3 optimizar-iconos.py ruta/al/logo.png
```

O con ImageMagick:

```bash
./optimizar-iconos.sh ruta/al/logo.png
```

## Debugging

### Ver Logs de Firebase

```bash
firebase functions:log
```

### Ver Estado de Hosting

```bash
firebase hosting:channel:list
```

## Flujo de Trabajo Recomendado

1. **Desarrollo Local**: Usa emuladores para probar cambios
2. **Commit**: Haz commit de cambios significativos
3. **Push**: Sube cambios a GitHub
4. **Despliegue**: Despliega a Firebase cuando esté listo

## Recursos

- [Documentación de Firebase Emulators](https://firebase.google.com/docs/emulator-suite)
- [Firebase Hosting Docs](https://firebase.google.com/docs/hosting)

