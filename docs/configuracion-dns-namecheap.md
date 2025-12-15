---
layout: default
title: Configuración DNS en Namecheap
description: Guía paso a paso para configurar DNS en Namecheap para Firebase Hosting
category: guide
---

# Configuración DNS en Namecheap para Firebase

Esta guía te muestra exactamente qué registros DNS configurar en Namecheap para cada dominio.

## 📋 Resumen Rápido

| Dominio | Tipo de Registro | Host | Valor |
|---------|-----------------|------|-------|
| `hello.tintum.app` | CNAME | `hello` | `tintum-web.web.app` |
| `tintum.app` | A | `@` | [IPs de Firebase] |
| `www.tintum.app` | CNAME | `www` | `www-redirect.web.app` |

---

## 🌐 Paso 1: Acceder a Namecheap

1. Inicia sesión en [Namecheap](https://www.namecheap.com/)
2. Ve a **Domain List** (Lista de Dominios)
3. Encuentra `tintum.app` y haz clic en **Manage**

---

## 🔧 Paso 2: Configurar hello.tintum.app (Sitio Principal)

Este es el dominio principal que mostrará tu aplicación.

### En Firebase Console

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio `tintum-web`
3. Haz clic en **"Add custom domain"** o **"Agregar dominio personalizado"**
4. Ingresa: `hello.tintum.app`
5. Firebase te mostrará las instrucciones

### En Namecheap

1. Ve a la pestaña **Advanced DNS**
2. En la sección **Host Records**, agrega:

```
Type: CNAME Record
Host: hello
Value: tintum-web.web.app
TTL: Automatic (o 30 min)
```

3. **Guarda los cambios**

**Nota:** El valor debe ser exactamente `tintum-web.web.app` (sin `https://` ni `/`)

---

## 🔧 Paso 3: Configurar tintum.app (Redirección)

Este dominio redirigirá a `hello.tintum.app`.

### En Firebase Console

1. Primero crea el sitio `tintum-redirect` si no existe:
   - En Firebase Console → Hosting → **"Add another site"**
   - Nombre: `tintum-redirect`
2. Selecciona el sitio `tintum-redirect`
3. Haz clic en **"Add custom domain"**
4. Ingresa: `tintum.app`
5. **Firebase te dará direcciones IP** (registros A y AAAA)

### En Namecheap

1. Ve a la pestaña **Advanced DNS**
2. En la sección **Host Records**, agrega los registros A:

```
Type: A Record
Host: @
Value: [Primera IP de Firebase]
TTL: Automatic
```

Repite para cada IP que Firebase te proporcione. Firebase puede dar 2-4 IPs.

**Ejemplo:**
```
Type: A Record
Host: @
Value: 151.101.1.195
TTL: Automatic

Type: A Record
Host: @
Value: 151.101.65.195
TTL: Automatic
```

3. Si Firebase también proporciona direcciones IPv6 (AAAA), agrega:

```
Type: AAAA Record
Host: @
Value: [IPv6 de Firebase]
TTL: Automatic
```

4. **Guarda los cambios**

**Importante:** 
- El Host debe ser `@` (arroba) para el dominio raíz
- Debes agregar TODAS las IPs que Firebase te proporcione
- No uses CNAME para el dominio raíz (tintum.app), solo A/AAAA

---

## 🔧 Paso 4: Configurar www.tintum.app (Redirección)

Este dominio también redirigirá a `hello.tintum.app`.

### En Firebase Console

1. Primero crea el sitio `www-redirect` si no existe:
   - En Firebase Console → Hosting → **"Add another site"**
   - Nombre: `www-redirect`
2. Selecciona el sitio `www-redirect`
3. Haz clic en **"Add custom domain"**
4. Ingresa: `www.tintum.app`
5. Firebase te mostrará las instrucciones (generalmente CNAME)

### En Namecheap

1. Ve a la pestaña **Advanced DNS**
2. En la sección **Host Records**, agrega:

```
Type: CNAME Record
Host: www
Value: www-redirect.web.app
TTL: Automatic (o 30 min)
```

**Nota:** El valor exacto puede variar. Firebase te dirá el valor correcto cuando agregues el dominio.

3. **Guarda los cambios**

---

## ✅ Paso 5: Verificar la Configuración

### Esperar Propagación DNS

- La propagación DNS puede tardar **15-30 minutos** (a veces hasta 48 horas)
- Los cambios generalmente son visibles en 15-30 minutos

### Verificar con Comandos

```bash
# Verificar hello.tintum.app
dig hello.tintum.app CNAME

# Verificar tintum.app (registros A)
dig tintum.app A

# Verificar www.tintum.app
dig www.tintum.app CNAME

# O usar nslookup
nslookup hello.tintum.app
nslookup tintum.app
nslookup www.tintum.app
```

### Verificar en Firebase Console

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. En cada sitio, verifica el estado del dominio:
   - ⏳ **"Pending verification"**: Esperando verificación DNS
   - ⏳ **"Pending SSL"**: DNS verificado, esperando SSL
   - ✅ **"Connected"**: Todo configurado y funcionando

---

## 📝 Ejemplo Completo de Configuración en Namecheap

Aquí está cómo debería verse tu configuración en Namecheap Advanced DNS:

```
Type          Host    Value                      TTL
----------------------------------------------------------
CNAME         hello   tintum-web.web.app         Automatic
A             @       151.101.1.195             Automatic
A             @       151.101.65.195            Automatic
AAAA          @       2606:4700::6810:1c3        Automatic (si aplica)
CNAME         www     www-redirect.web.app       Automatic
```

**Nota:** Las IPs son ejemplos. Firebase te dará las IPs reales cuando agregues cada dominio.

---

## 🔍 Troubleshooting

### El dominio no se verifica en Firebase

1. **Verifica que los registros estén correctos:**
   - CNAME debe apuntar exactamente a `[site-id].web.app`
   - A records deben usar `@` como Host
   - No debe haber espacios extra en los valores

2. **Espera más tiempo:**
   - La propagación DNS puede tardar hasta 48 horas
   - Generalmente es rápido (15-30 minutos)

3. **Verifica con comandos:**
   ```bash
   dig hello.tintum.app CNAME
   dig tintum.app A
   ```

### Error: "CNAME and other records conflict"

- No puedes tener un CNAME en el dominio raíz (`@`) junto con registros A
- Para `tintum.app` (dominio raíz), usa SOLO registros A/AAAA
- Para subdominios (`hello`, `www`), usa CNAME

### El SSL no se configura

- Firebase configura SSL automáticamente con Let's Encrypt
- Espera 1-2 horas después de que el dominio esté verificado
- Verifica en Firebase Console → Hosting → Domains

---

## 📚 Referencias

- [Firebase Hosting - Custom Domains](https://firebase.google.com/docs/hosting/custom-domain)
- [Namecheap DNS Management](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-configure-dns-records-for-your-domain/)

---

## ⚠️ Notas Importantes

✅ **CNAME para subdominios**: `hello.tintum.app` y `www.tintum.app` usan CNAME

✅ **A/AAAA para dominio raíz**: `tintum.app` usa registros A (y AAAA si aplica)

✅ **Valores exactos**: Los valores deben coincidir exactamente con lo que Firebase te proporciona

✅ **Propagación DNS**: Espera 15-30 minutos antes de verificar

✅ **SSL Automático**: Firebase configurará SSL automáticamente con Let's Encrypt (1-2 horas)

