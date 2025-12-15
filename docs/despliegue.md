---
layout: default
title: Despliegue
description: Guía para desplegar Tintum.app a Firebase Hosting
category: guide
---

# Guía de Despliegue

Cómo desplegar el proyecto Tintum.app a Firebase Hosting.

## Despliegue Completo

Para desplegar todo (hosting + Firestore):

```bash
firebase deploy
```

## Despliegue Parcial

### Solo Hosting

```bash
firebase deploy --only hosting
```

### Solo Reglas de Firestore

```bash
firebase deploy --only firestore:rules
```

### Solo Índices de Firestore

```bash
firebase deploy --only firestore:indexes
```

## Verificar el Despliegue

Después del despliegue, Firebase te proporcionará una URL. Ejemplo:

```
✔  Deploy complete!

Project Console: https://console.firebase.google.com/project/tintum-app/overview
Hosting URL: https://tintum-app.web.app
```

## Rollback

Si necesitas revertir un despliegue:

```bash
firebase hosting:rollback
```

## Variables de Entorno

Si necesitas configurar variables de entorno, puedes usar:

```bash
firebase functions:config:set app.key="value"
```

## Notas Importantes

- Asegúrate de estar autenticado con `denis@tintum.app`
- Verifica que el proyecto Firebase esté correctamente configurado
- Revisa los logs si hay errores durante el despliegue

