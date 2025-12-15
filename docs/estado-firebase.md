---
layout: default
title: Estado de Firebase
description: Estado actual del proyecto Firebase de Tintum.app
---

# Estado del Proyecto Firebase

## Información del Proyecto

- **Project ID**: `tintum-web`
- **Project Display Name**: `tintum-web`
- **Project Number**: `784982125106`
- **Cuenta**: `denis@tintum.app`
- **Estado**: ✅ Configurado y disponible

## Servicios Habilitados

### ✅ Firebase Hosting

- **Site ID**: `tintum-web`
- **URL por defecto**: https://tintum-web.web.app
- **Estado**: Activo y listo para desplegar
- **Carpeta pública**: `web/`

### ⚠️ Firestore

- **Estado**: API no habilitada aún
- **Acción requerida**: Se habilitará automáticamente en el primer despliegue
- **Reglas**: Configuradas en `firestore.rules` (compilan correctamente)
- **Índices**: Configurados en `firestore.indexes.json`

## Configuración Actual

### Archivo `.firebaserc`

```json
{
  "projects": {
    "default": "tintum-web"
  }
}
```

### Archivo `firebase.json`

- Hosting configurado apuntando a `web/`
- Firestore configurado con reglas e índices
- Headers de cache configurados
- Rewrites configurados para SPA

## Verificación

El proyecto está correctamente configurado. Un dry-run muestra:

```
✔  Dry run complete!
Project Console: https://console.firebase.google.com/project/tintum-web/overview
Hosting URL: https://tintum-web.web.app
```

## Próximos Pasos

1. **Habilitar Firestore** (se hará automáticamente en el primer despliegue):
   ```bash
   firebase deploy
   ```

2. **O habilitar manualmente**:
   - Visita: https://console.developers.google.com/apis/api/firestore.googleapis.com/overview?project=tintum-web
   - O espera a que se habilite automáticamente durante el despliegue

3. **Desplegar el proyecto**:
   ```bash
   firebase deploy
   ```

## Enlaces Útiles

- **Firebase Console**: https://console.firebase.google.com/project/tintum-web/overview
- **Hosting URL**: https://tintum-web.web.app
- **API Firestore**: https://console.developers.google.com/apis/api/firestore.googleapis.com/overview?project=tintum-web

