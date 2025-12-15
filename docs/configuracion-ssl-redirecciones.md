---
layout: default
title: SSL con Let's Encrypt y Redirecciones
description: Configuración de certificados SSL automáticos y redirecciones de dominio
category: guide
---

# SSL con Let's Encrypt y Redirecciones

Esta guía explica cómo Firebase Hosting gestiona automáticamente los certificados SSL con Let's Encrypt y cómo configurar las redirecciones de dominio.

## 🔒 Certificados SSL con Let's Encrypt

### Gestión Automática

Firebase Hosting **gestiona automáticamente los certificados SSL** usando Let's Encrypt. No necesitas configurar nada manualmente.

**Características:**
- ✅ Certificados SSL automáticos para todos los dominios personalizados
- ✅ Renovación automática (cada 90 días)
- ✅ Sin configuración manual requerida
- ✅ Certificados válidos y reconocidos por todos los navegadores

### Proceso Automático

1. **Agregas un dominio personalizado** en Firebase Console
2. **Configuras los registros DNS** en tu proveedor (Namecheap)
3. **Firebase verifica** la propiedad del dominio
4. **Firebase solicita automáticamente** un certificado Let's Encrypt
5. **El certificado se instala** automáticamente (1-24 horas, generalmente 1-2 horas)
6. **El certificado se renueva** automáticamente cada 90 días

### Verificar Estado del SSL

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. En la sección **Domains**, verifica el estado:
   - ✅ **"Connected"**: SSL activo y funcionando
   - ⏳ **"Pending SSL"**: Esperando aprovisionamiento
   - ❌ **"Error"**: Problema con la configuración

### No Se Requiere Configuración Manual

A diferencia de otros servicios, Firebase Hosting:
- ❌ No requiere subir certificados manualmente
- ❌ No requiere configurar rutas de certificados
- ❌ No requiere scripts de renovación
- ✅ Todo es automático y gestionado por Firebase

---

## 🔄 Redirecciones de Dominio

### Configuración Objetivo

Queremos que:
- `https://tintum.app` → Redirige a `https://hello.tintum.app`
- `https://www.tintum.app` → Redirige a `https://hello.tintum.app`
- `https://hello.tintum.app` → Contenido principal de la aplicación

### Arquitectura de Múltiples Sitios

Firebase Hosting permite configurar múltiples sitios. Usaremos:

1. **Sitio principal** (`tintum-web`): `hello.tintum.app` - Contiene el contenido
2. **Sitio de redirección 1** (`tintum-redirect`): `tintum.app` - Solo redirige
3. **Sitio de redirección 2** (`www-redirect`): `www.tintum.app` - Solo redirige

### Paso 1: Crear Sitios en Firebase Console

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Haz clic en **"Add another site"** o **"Agregar otro sitio"**
3. Crea los siguientes sitios:
   - `tintum-redirect` (para tintum.app)
   - `www-redirect` (para www.tintum.app)

**Nota:** El sitio `tintum-web` ya existe y es el sitio principal.

### Paso 2: Configurar Dominios en Cada Sitio

#### Para hello.tintum.app (Sitio Principal)

1. En el sitio `tintum-web`, agrega el dominio: `hello.tintum.app`
2. Configura los registros DNS según la [guía de configuración de dominio]({{ '/configurar-dominio-personalizado' | relative_url }})
   - Usa CNAME: `hello` → `tintum-web.web.app`

#### Para tintum.app (Sitio de Redirección)

1. En el sitio `tintum-redirect`, agrega el dominio: `tintum.app`
2. Firebase te proporcionará direcciones IP (A/AAAA records)
3. Configura registros A/AAAA en Namecheap:
   ```
   Type: A Record
   Host: @
   Value: [IPs proporcionadas por Firebase]
   TTL: Automatic
   ```

#### Para www.tintum.app (Sitio de Redirección)

1. En el sitio `www-redirect`, agrega el dominio: `www.tintum.app`
2. Configura un registro CNAME en Namecheap:
   ```
   Type: CNAME Record
   Host: www
   Value: [URL del sitio www-redirect en Firebase, ej: www-redirect.web.app]
   TTL: Automatic
   ```

### Paso 3: Configurar .firebasehosting.json

El archivo `.firebasehosting.json` mapea los targets a los sitios. Ya está configurado:

```json
{
  "targets": {
    "tintum-web": "tintum-web",
    "tintum-redirect": "tintum-redirect",
    "www-redirect": "www-redirect"
  },
  "sites": {
    "tintum-web": "hello.tintum.app",
    "tintum-redirect": "tintum.app",
    "www-redirect": "www.tintum.app"
  }
}
```

### Paso 4: Verificar firebase.json

El archivo `firebase.json` ya está configurado con:

- **Sitio principal** (`tintum-web`): Contiene el contenido, sin redirects
- **Sitio tintum-redirect**: Solo redirects a `https://hello.tintum.app`
- **Sitio www-redirect**: Solo redirects a `https://hello.tintum.app`

### Paso 5: Desplegar

```bash
# Desplegar todos los sitios
firebase deploy --only hosting

# O desplegar sitios específicos
firebase deploy --only hosting:tintum-web
firebase deploy --only hosting:tintum-redirect
firebase deploy --only hosting:www-redirect
```

---

## 📋 Resumen de Configuración DNS

### Para hello.tintum.app (Principal)

```
Type: CNAME Record
Host: hello
Value: tintum-web.web.app
TTL: Automatic
```

### Para tintum.app (Redirección)

```
Type: A Record
Host: @
Value: [IPs proporcionadas por Firebase para tintum-redirect]
TTL: Automatic
```

**Nota:** Firebase puede proporcionar múltiples IPs. Debes agregar todas.

### Para www.tintum.app (Redirección)

```
Type: CNAME Record
Host: www
Value: [URL del sitio www-redirect, ej: www-redirect.web.app]
TTL: Automatic
```

---

## ✅ Verificar que Funciona

### Verificar Redirecciones

```bash
# Verificar redirección de tintum.app
curl -I https://tintum.app

# Verificar redirección de www.tintum.app
curl -I https://www.tintum.app

# Verificar que hello.tintum.app funciona
curl -I https://hello.tintum.app
```

Deberías ver:
- `tintum.app` → `301 Moved Permanently` → `Location: https://hello.tintum.app`
- `www.tintum.app` → `301 Moved Permanently` → `Location: https://hello.tintum.app`
- `hello.tintum.app` → `200 OK` (contenido de la aplicación)

### Verificar SSL

Todos los dominios deben tener certificados SSL válidos:
- ✅ `https://tintum.app` (con redirección)
- ✅ `https://www.tintum.app` (con redirección)
- ✅ `https://hello.tintum.app` (contenido principal)

Firebase configurará automáticamente los certificados SSL con Let's Encrypt para todos los dominios.

---

## 🔧 Troubleshooting

### Las redirecciones no funcionan

1. **Verifica que los sitios estén creados** en Firebase Console
2. **Verifica que los dominios estén agregados** a cada sitio
3. **Verifica que el DNS esté configurado** correctamente
4. **Espera la propagación DNS** (15-30 minutos)
5. **Verifica el archivo `.firebasehosting.json`** esté correcto
6. **Verifica que hayas desplegado** los sitios: `firebase deploy --only hosting`

### El SSL no se configura en los sitios de redirección

- Firebase configurará SSL automáticamente para todos los dominios usando Let's Encrypt
- Espera 1-2 horas después de agregar el dominio
- Verifica en Firebase Console → Hosting → Domains
- El estado debe cambiar a "Connected" cuando el SSL esté listo

### Error: "Site not found"

- Asegúrate de haber creado los sitios en Firebase Console primero
- Verifica que los nombres en `.firebasehosting.json` coincidan con los IDs de los sitios
- Ejecuta `firebase hosting:sites:list` para ver los sitios disponibles

### Error al desplegar

Si obtienes un error al desplegar, verifica:
```bash
# Ver sitios disponibles
firebase hosting:sites:list

# Verificar configuración
firebase deploy --only hosting --dry-run
```

---

## 📚 Referencias

- [Firebase Hosting - Multiple Sites](https://firebase.google.com/docs/hosting/multisites)
- [Firebase Hosting - Custom Domains](https://firebase.google.com/docs/hosting/custom-domain)
- [Firebase Hosting - Redirects](https://firebase.google.com/docs/hosting/full-config#redirects)
- [Let's Encrypt](https://letsencrypt.org/)

---

## Notas Importantes

✅ **SSL Automático**: Firebase gestiona todos los certificados SSL automáticamente con Let's Encrypt

✅ **Renovación Automática**: Los certificados se renuevan automáticamente cada 90 días

✅ **Redirecciones Permanentes**: Usamos redirecciones 301 (permanentes) para SEO

✅ **Múltiples Sitios**: Firebase Hosting permite múltiples sitios en un solo proyecto

✅ **Sin Configuración Manual de SSL**: Todo es automático, no necesitas gestionar certificados
