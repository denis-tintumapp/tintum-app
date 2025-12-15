---
layout: default
title: Despliegue Completado
description: Estado del despliegue de hello.tintum.app
---

# ✅ Despliegue Completado

El sitio `tintum-web` ha sido desplegado exitosamente.

## 📊 Estado Actual

- ✅ **Sitio desplegado**: `tintum-web`
- ✅ **URL por defecto**: https://tintum-web.web.app
- ✅ **Dominio personalizado**: `hello.tintum.app` (configurado)
- ✅ **Archivos desplegados**: 4 archivos desde la carpeta `web/`

## 🌐 URLs Disponibles

- **URL por defecto**: https://tintum-web.web.app
- **Dominio personalizado**: https://hello.tintum.app (cuando el DNS y SSL estén listos)

## 📋 Próximos Pasos

1. **Verificar dominio personalizado**:
   - Espera a que el estado en Firebase Console cambie a "Connected"
   - Verifica que el SSL esté activo (candado verde)

2. **Verificar que funciona**:
   ```bash
   curl -I https://hello.tintum.app
   ```

3. **Configurar los otros dominios**:
   - `tintum.app` → sitio `tintum-redirect`
   - `www.tintum.app` → crear nuevo sitio

4. **Desplegar los sitios de redirección**:
   ```bash
   firebase deploy --only hosting:tintum-redirect
   ```

## 🔍 Verificar Estado

```bash
# Ver sitios
firebase hosting:sites:list

# Ver información del sitio
firebase hosting:sites:get tintum-web

# Verificar despliegue
curl -I https://tintum-web.web.app
```

## 📚 Referencias

- [Firebase Console](https://console.firebase.google.com/project/tintum-web/hosting)
- [Estado de Firebase]({{ '/estado-firebase' | relative_url }})

