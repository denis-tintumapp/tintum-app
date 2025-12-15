# Corregir www.tintum.app - Guía Rápida

## 🔍 Problema Identificado

El DNS de `www.tintum.app` apunta a `www-redirect.web.app`, pero ese sitio **NO existe** en Firebase. Esto causa el error SSL.

## ✅ Solución

Usar el sitio `tintum-redirect` que ya existe y está configurado para manejar ambas redirecciones.

---

## 📋 Pasos para Corregir

### Paso 1: Agregar `www.tintum.app` en Firebase Console

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-redirect`**
3. Verifica si `www.tintum.app` ya está en la lista de dominios
4. Si **NO está**, haz clic en **"Add custom domain"**:
   - Ingresa: `www.tintum.app`
   - Firebase te mostrará las instrucciones (generalmente CNAME)
   - **Anota el valor del CNAME** - debería ser `tintum-redirect.web.app`

### Paso 2: Corregir DNS en Namecheap

1. Ve a Namecheap → Domain List → `tintum.app` → Manage → **Advanced DNS**
2. Busca el registro CNAME existente para `www`
3. **Modifica** el valor a: `tintum-redirect.web.app`
   - Si no existe, agrégalo:
     ```
     Type: CNAME Record
     Host: www
     Value: tintum-redirect.web.app
     TTL: Automatic
     ```
4. **Guarda los cambios**

### Paso 3: Verificar Despliegue

El sitio `tintum-redirect` ya está desplegado, pero puedes verificar:

```bash
firebase deploy --only hosting:tintum-redirect
```

### Paso 4: Esperar y Verificar

1. Espera 15-30 minutos para la propagación DNS
2. Firebase configurará SSL automáticamente (1-2 horas)
3. Verifica:
   ```bash
   curl -I https://www.tintum.app
   ```
   Deberías ver: `301 Moved Permanently` → `Location: https://hello.tintum.app`

---

## 📝 Resumen de Configuración DNS

En Namecheap, el registro CNAME para `www` debe ser:

```
Type: CNAME Record
Host: www
Value: tintum-redirect.web.app
TTL: Automatic
```

**NO debe apuntar a `www-redirect.web.app`** (ese sitio no existe).

---

## ✅ Estado Esperado

Después de corregir:

- `tintum.app` → Redirige a `hello.tintum.app` (sitio `tintum-redirect`)
- `www.tintum.app` → Redirige a `hello.tintum.app` (mismo sitio `tintum-redirect`)
- `hello.tintum.app` → Contenido principal (sitio `tintum-web`)

---

## 🆘 Si Sigue Sin Funcionar

1. Verifica en Firebase Console que `www.tintum.app` esté agregado al sitio `tintum-redirect`
2. Verifica que el estado del dominio sea "Connected" o "Pending SSL"
3. Verifica el DNS: `dig www.tintum.app CNAME +short` debe mostrar `tintum-redirect.web.app`
4. Espera más tiempo (DNS puede tardar hasta 48 horas, pero generalmente es rápido)

