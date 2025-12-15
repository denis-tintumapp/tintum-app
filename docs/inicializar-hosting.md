---
layout: default
title: Inicializar Hosting en Firebase
description: Guía para inicializar y configurar Firebase Hosting con múltiples sitios
category: guide
---

# Inicializar Hosting en Firebase

Esta guía te muestra cómo inicializar y configurar Firebase Hosting correctamente.

## ✅ Estado Actual

### Sitios Creados

- ✅ `tintum-web` - Sitio principal (ya existe)
- ✅ `tintum-redirect` - Para redirigir tintum.app (ya creado)
- ⏳ `www-redirect` - Para redirigir www.tintum.app (necesita crearse desde consola)

## 📋 Paso 1: Verificar Sitios Existentes

```bash
firebase hosting:sites:list
```

Deberías ver:
- `tintum-web`
- `tintum-redirect`

## 📋 Paso 2: Crear Sitio para www.tintum.app

Firebase tiene restricciones en los nombres de sitios cuando se crean desde CLI. Para `www.tintum.app`, necesitas crearlo desde la consola web:

### Opción A: Desde Firebase Console (Recomendado)

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Haz clic en **"Add another site"** o **"Agregar otro sitio"**
3. Ingresa un nombre para el sitio (ej: `www-redirect` o deja que Firebase sugiera uno)
4. Haz clic en **"Create site"**

### Opción B: Desde CLI (si el nombre es válido)

```bash
firebase hosting:sites:create [nombre-del-sitio]
```

**Nota:** Los nombres de sitios deben seguir el patrón: `[nombre]-[hash]` o solo `[nombre]` sin caracteres especiales.

## 📋 Paso 3: Actualizar .firebasehosting.json

Una vez creado el sitio para www, actualiza `.firebasehosting.json`:

```json
{
  "targets": {
    "tintum-web": "tintum-web",
    "tintum-redirect": "tintum-redirect",
    "www-redirect": "[id-del-sitio-creado]"
  },
  "sites": {
    "tintum-web": "hello.tintum.app",
    "tintum-redirect": "tintum.app",
    "www-redirect": "www.tintum.app"
  }
}
```

## 📋 Paso 4: Verificar Configuración

```bash
# Ver todos los sitios
firebase hosting:sites:list

# Verificar configuración
firebase deploy --only hosting --dry-run
```

## 📋 Paso 5: Agregar Dominios a Cada Sitio

### Para hello.tintum.app

1. En Firebase Console, selecciona el sitio `tintum-web`
2. Haz clic en **"Add custom domain"**
3. Ingresa: `hello.tintum.app`
4. Sigue las instrucciones para configurar DNS

### Para tintum.app

1. En Firebase Console, selecciona el sitio `tintum-redirect`
2. Haz clic en **"Add custom domain"**
3. Ingresa: `tintum.app`
4. Sigue las instrucciones para configurar DNS (registros A/AAAA)

### Para www.tintum.app

1. En Firebase Console, selecciona el sitio creado para www
2. Haz clic en **"Add custom domain"**
3. Ingresa: `www.tintum.app`
4. Sigue las instrucciones para configurar DNS (CNAME)

## 📋 Paso 6: Desplegar

Una vez configurados los dominios:

```bash
# Desplegar todos los sitios
firebase deploy --only hosting

# O desplegar sitios específicos
firebase deploy --only hosting:tintum-web
firebase deploy --only hosting:tintum-redirect
```

## ✅ Verificar

```bash
# Verificar sitios
firebase hosting:sites:list

# Verificar redirecciones
curl -I https://tintum.app
curl -I https://www.tintum.app
curl -I https://hello.tintum.app
```

## 🔧 Troubleshooting

### Error: "Invalid name" al crear sitio

- Los nombres de sitios no pueden tener ciertos caracteres especiales
- Usa la consola web para crear sitios con nombres personalizados
- O usa nombres simples sin guiones múltiples

### Error: "Site not found" al desplegar

- Verifica que el sitio exista: `firebase hosting:sites:list`
- Verifica que el ID en `.firebasehosting.json` coincida con el Site ID real
- Los Site IDs pueden diferir de los nombres que les diste

### El sitio no aparece en la lista

- Espera unos segundos después de crear el sitio
- Verifica que estés en el proyecto correcto: `firebase use`
- Recarga la lista: `firebase hosting:sites:list`

## 📚 Referencias

- [Firebase Hosting - Multiple Sites](https://firebase.google.com/docs/hosting/multisites)
- [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)

