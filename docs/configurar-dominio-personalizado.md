---
layout: default
title: Configurar Dominio Personalizado
description: Guía para configurar tintum.app como dominio personalizado en Firebase Hosting
category: guide
---

# Configurar Dominio Personalizado tintum.app

Esta guía te ayudará a configurar `tintum.app` como dominio personalizado en Firebase Hosting.

## ⚠️ Importante: Dominio Raíz vs Subdominio

Para el dominio raíz (`tintum.app`), Firebase requiere registros **A y AAAA** en lugar de CNAME, ya que los CNAME no pueden usarse en el apex/root del dominio.

---

## Paso 1: Agregar Dominio en Firebase Console

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Haz clic en **"Add custom domain"** o **"Agregar dominio personalizado"**
3. Ingresa: `tintum.app`
4. Firebase te mostrará las instrucciones para configurar los registros DNS

---

## Paso 2: Obtener Registros DNS de Firebase

Firebase te proporcionará dos opciones:

### Opción A: Registros A y AAAA (Recomendado para dominio raíz)

Firebase te dará direcciones IP que debes configurar:

**Registros A (IPv4):**
```
Type: A Record
Host: @ (o dejar vacío para dominio raíz)
Value: [IP proporcionada por Firebase]
TTL: Automatic (o 30 min)
```

**Registros AAAA (IPv6):**
```
Type: AAAA Record
Host: @ (o dejar vacío para dominio raíz)
Value: [IPv6 proporcionada por Firebase]
TTL: Automatic (o 30 min)
```

**Nota:** Firebase puede proporcionar múltiples IPs. Debes agregar todas.

### Opción B: Verificación TXT (Temporal)

Firebase puede pedirte agregar un registro TXT para verificar la propiedad:

```
Type: TXT Record
Host: @ (o dejar vacío para dominio raíz)
Value: [Código de verificación de Firebase]
TTL: Automatic
```

---

## Paso 3: Configurar DNS en Namecheap

1. Accede a tu cuenta de [Namecheap](https://www.namecheap.com/)
2. Ve a **Domain List** → Selecciona `tintum.app` → **Manage**
3. Ve a la pestaña **Advanced DNS**
4. En la sección **Host Records**, agrega los registros:

### Registros A (IPv4)

Agrega todos los registros A que Firebase te proporcionó:

```
Type: A Record
Host: @
Value: [IP de Firebase - ejemplo: 151.101.1.195]
TTL: Automatic
```

Repite para cada IP que Firebase te proporcione.

### Registros AAAA (IPv6)

Si Firebase proporciona direcciones IPv6:

```
Type: AAAA Record
Host: @
Value: [IPv6 de Firebase]
TTL: Automatic
```

### Registro TXT (Si es necesario para verificación)

```
Type: TXT Record
Host: @
Value: [Código de verificación de Firebase]
TTL: Automatic
```

5. **Guarda los cambios**

---

## Paso 4: Verificar Propagación DNS

Espera 15-30 minutos y verifica que los registros se hayan propagado:

```bash
# Verificar registros A
dig tintum.app A

# Verificar registros AAAA (si aplica)
dig tintum.app AAAA

# Verificar registro TXT (si aplica)
dig tintum.app TXT
```

O usando nslookup:

```bash
nslookup tintum.app
```

---

## Paso 5: Verificar Dominio en Firebase

1. Regresa a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. En la sección **Domains**, busca `tintum.app`
3. El estado debería cambiar de:
   - ⏳ **"Pending verification"** → 
   - ⏳ **"Pending SSL"** → 
   - ✅ **"Connected"**

**Tiempo estimado:**
- Verificación DNS: 15-30 minutos
- Aprovisionamiento SSL: 1-24 horas (generalmente 1-2 horas)

---

## Paso 6: Verificar que Funciona

Una vez que el dominio esté conectado y el SSL esté activo:

1. Accede a `https://tintum.app`
2. Deberías ver la aplicación funcionando
3. Verifica que el certificado SSL sea válido (candado verde)

---

## URLs Resultantes

Después de la configuración:

- **Aplicación principal:** `https://tintum.app`
- **URL por defecto (sigue funcionando):** `https://tintum-web.web.app`
- **Ambas URLs apuntan al mismo contenido**

---

## Troubleshooting

### El dominio no carga después de configurar los registros A

1. **Verifica que los registros A estén correctos en Namecheap**
   - Asegúrate de usar `@` como Host para el dominio raíz
   - Verifica que las IPs sean exactamente las que Firebase proporcionó

2. **Espera la propagación DNS**
   - Puede tardar hasta 48 horas, pero generalmente es rápido (15-30 minutos)
   - Usa `dig` o `nslookup` para verificar

3. **Verifica que no haya conflictos**
   - Asegúrate de no tener otros registros A o CNAME que puedan interferir
   - Si tenías un CNAME en `@`, debes eliminarlo (los CNAME no pueden coexistir con registros A en el apex)

### Firebase no puede verificar el dominio

1. **Verifica el registro TXT** (si Firebase lo requiere)
   - Asegúrate de que el registro TXT esté configurado correctamente
   - Espera 15-30 minutos para la propagación

2. **Verifica los registros A**
   - Usa `dig tintum.app A` para verificar que apunten a las IPs de Firebase
   - Asegúrate de que todos los registros A estén configurados

3. **Reintenta la verificación en Firebase Console**
   - Haz clic en "Verify" o "Verificar" en Firebase Console
   - Espera unos minutos y vuelve a intentar

### El SSL no se configura automáticamente

- Firebase configura el SSL automáticamente después de verificar el dominio
- Puede tardar hasta 24 horas, pero generalmente es rápido (1-2 horas)
- Verifica en Firebase Console → Hosting → Domains
- El estado debe cambiar a "Connected" cuando el SSL esté listo

### Error: "Domain verification failed"

1. Verifica que todos los registros DNS estén correctos
2. Espera más tiempo para la propagación DNS (puede tardar hasta 48 horas)
3. Elimina y vuelve a agregar el dominio en Firebase Console
4. Contacta al soporte de Firebase si el problema persiste

---

## Comandos Útiles

```bash
# Verificar registros DNS
dig tintum.app A
dig tintum.app AAAA
dig tintum.app TXT

# Verificar con nslookup
nslookup tintum.app

# Verificar estado en Firebase (desde CLI)
firebase hosting:sites:get tintum-web

# Ver todos los dominios configurados
firebase hosting:sites:list
```

---

## Notas Importantes

✅ **El código ya está preparado:** La aplicación usa `window.location.origin` dinámicamente, por lo que funcionará automáticamente con cualquier dominio.

✅ **No se requieren cambios en el código:** Una vez configurado el DNS y Firebase, todo funcionará automáticamente.

✅ **Compatibilidad:** La URL por defecto (`tintum-web.web.app`) seguirá funcionando.

✅ **SSL Automático:** Firebase configura automáticamente el certificado SSL con Let's Encrypt.

---

## Referencias

- [Firebase Hosting - Custom Domains](https://firebase.google.com/docs/hosting/custom-domain)
- [Namecheap DNS Management](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-configure-dns-records-for-your-domain/)

