---
layout: default
title: Solucionar Redirecciones
description: Cómo solucionar problemas con las redirecciones de tintum.app y www.tintum.app
---

# Solucionar Redirecciones

## 🔍 Diagnóstico

### Problema 1: `tintum.app` no redirige

**Causa:** El DNS no está configurado o el sitio no está desplegado.

**Solución:**
1. Verifica que el dominio `tintum.app` esté agregado en Firebase Console al sitio `tintum-redirect`
2. Verifica que los registros A/AAAA estén configurados en Namecheap
3. El sitio `tintum-redirect` ya está desplegado ✅

### Problema 2: `www.tintum.app` no redirige (error SSL)

**Causa:** El DNS apunta a `www-redirect.web.app` pero el sitio no existe en Firebase.

**Solución:**
1. Crear el sitio desde Firebase Console (no se puede desde CLI)
2. Configurar el sitio con redirecciones
3. Desplegar el sitio

---

## ✅ Solución Paso a Paso

### Para `tintum.app`

#### Paso 1: Verificar dominio en Firebase

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-redirect`**
3. Verifica que `tintum.app` esté en la lista de dominios
4. Si no está, agrégalo:
   - Haz clic en **"Add custom domain"**
   - Ingresa: `tintum.app`
   - Firebase te dará las IPs para configurar

#### Paso 2: Verificar DNS en Namecheap

1. Ve a Namecheap → Domain List → `tintum.app` → Manage → Advanced DNS
2. Verifica que tengas registros A configurados:
   ```
   Type: A Record
   Host: @
   Value: [IPs de Firebase]
   TTL: Automatic
   ```
3. Si no están, agrégalos con las IPs que Firebase te proporcionó

#### Paso 3: Verificar despliegue

El sitio `tintum-redirect` ya está desplegado. Si hiciste cambios, vuelve a desplegar:

```bash
firebase deploy --only hosting:tintum-redirect
```

#### Paso 4: Verificar

```bash
# Espera 15-30 minutos para propagación DNS
curl -I https://tintum.app
```

Deberías ver: `301 Moved Permanently` → `Location: https://hello.tintum.app`

---

### Para `www.tintum.app`

#### Paso 1: Crear el sitio en Firebase Console

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Haz clic en **"Add another site"** o **"Agregar otro sitio"**
3. Ingresa un nombre (ej: `www-redirect` o deja que Firebase sugiera uno)
4. Haz clic en **"Create site"**
5. **Anota el Site ID** que Firebase te da (puede ser diferente al nombre que ingresaste)

#### Paso 2: Agregar dominio al sitio

1. Selecciona el sitio que acabas de crear
2. Haz clic en **"Add custom domain"**
3. Ingresa: `www.tintum.app`
4. Firebase te mostrará las instrucciones (generalmente CNAME)

#### Paso 3: Actualizar configuración local

Actualiza `.firebasehosting.json` con el Site ID real:

```json
{
  "targets": {
    "tintum-web": "tintum-web",
    "tintum-redirect": "tintum-redirect",
    "www-redirect": "[Site ID real de Firebase]"
  },
  "sites": {
    "tintum-web": "hello.tintum.app",
    "tintum-redirect": "tintum.app",
    "www-redirect": "www.tintum.app"
  }
}
```

#### Paso 4: Actualizar firebase.json

Agrega la configuración del sitio para www:

```json
{
  "hosting": [
    {
      "target": "tintum-web",
      ...
    },
    {
      "target": "tintum-redirect",
      ...
    },
    {
      "target": "www-redirect",
      "public": "web",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "redirects": [
        {
          "source": "**",
          "destination": "https://hello.tintum.app",
          "type": 301
        }
      ]
    }
  ]
}
```

#### Paso 5: Configurar target y desplegar

```bash
# Configurar target
firebase target:apply hosting www-redirect [Site ID real]

# Desplegar
firebase deploy --only hosting:www-redirect
```

#### Paso 6: Verificar DNS en Namecheap

1. Ve a Namecheap → Domain List → `tintum.app` → Manage → Advanced DNS
2. Verifica que tengas:
   ```
   Type: CNAME Record
   Host: www
   Value: [URL del sitio, ej: www-redirect.web.app]
   TTL: Automatic
   ```
3. Si el valor no coincide con el Site ID real, actualízalo

#### Paso 7: Verificar

```bash
# Espera 15-30 minutos para propagación DNS
curl -I https://www.tintum.app
```

Deberías ver: `301 Moved Permanently` → `Location: https://hello.tintum.app`

---

## 🔍 Verificar Estado Actual

```bash
# Ver sitios disponibles
firebase hosting:sites:list

# Verificar DNS
dig tintum.app A +short
dig www.tintum.app CNAME +short

# Verificar redirecciones
curl -I https://tintum.app
curl -I https://www.tintum.app
curl -I https://hello.tintum.app
```

---

## ⚠️ Problemas Comunes

### "Could not resolve host: tintum.app"

- **Causa:** DNS no configurado o no propagado
- **Solución:** Verifica registros A en Namecheap, espera 15-30 minutos

### "SSL: no alternative certificate subject name matches"

- **Causa:** El dominio apunta a un sitio que no existe o no tiene el dominio agregado
- **Solución:** Crea el sitio en Firebase y agrega el dominio

### La redirección no funciona aunque el DNS esté bien

- **Causa:** El sitio no está desplegado o la configuración es incorrecta
- **Solución:** Verifica `firebase.json` y despliega: `firebase deploy --only hosting:[site-id]`

---

## 📚 Referencias

- [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
- [Configuración DNS en Namecheap]({{ '/configuracion-dns-namecheap' | relative_url }})

