# Instrucciones: Firebase y Namecheap

## 🎯 Configuración Óptima

He configurado para usar **un solo sitio** (`tintum-redirect`) para ambas redirecciones:
- `tintum.app` → Redirige a `https://hello.tintum.app`
- `www.tintum.app` → Redirige a `https://hello.tintum.app`

Esto simplifica la configuración y el mantenimiento.

---

## 📋 Paso 1: Configurar en Firebase Console

### 1.1 Agregar `tintum.app` al sitio `tintum-redirect`

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-redirect`**
3. Verifica si `tintum.app` ya está en la lista de dominios
4. Si **NO está**, haz clic en **"Add custom domain"**:
   - Ingresa: `tintum.app`
   - Firebase te mostrará las **direcciones IP** (registros A)
   - **Anota estas IPs** - las necesitarás para Namecheap
5. Si **YA está**, verifica que el estado sea "Connected" o "Pending SSL"

### 1.2 Agregar `www.tintum.app` al mismo sitio `tintum-redirect`

1. En el mismo sitio **`tintum-redirect`**
2. Haz clic en **"Add custom domain"**
3. Ingresa: `www.tintum.app`
4. Firebase te mostrará las instrucciones (generalmente CNAME)
5. **Anota el valor del CNAME** - lo necesitarás para Namecheap

---

## 📋 Paso 2: Configurar en Namecheap

Ve a Namecheap → Domain List → `tintum.app` → Manage → **Advanced DNS**

### 2.1 Para `tintum.app` (Registros A)

Agrega **registros A** con las IPs que obtuviste de Firebase:

```
Type: A Record
Host: @
Value: [Primera IP de Firebase]
TTL: Automatic
```

**IMPORTANTE:** Firebase puede darte 2-4 IPs. Debes agregar **TODAS** como registros A separados.

**Ejemplo:**
Si Firebase te da:
- `151.101.1.195`
- `151.101.65.195`

Agrega en Namecheap:
```
A Record | @ | 151.101.1.195 | Automatic
A Record | @ | 151.101.65.195 | Automatic
```

### 2.2 Para `www.tintum.app` (CNAME)

Modifica o agrega el registro CNAME:

```
Type: CNAME Record
Host: www
Value: tintum-redirect.web.app
TTL: Automatic
```

**Acción:**
- Si ya existe un CNAME para `www`, **modifica** el valor a: `tintum-redirect.web.app`
- Si no existe, **agrégalo** con ese valor

### 2.3 Verificar `hello.tintum.app` (Ya configurado)

**NO MODIFIQUES** este registro - ya está funcionando:
```
Type: CNAME Record
Host: hello
Value: tintum-web.web.app
TTL: Automatic
```

---

## ✅ Resumen de Configuración en Namecheap

Tu configuración final debería verse así:

```
Type          Host    Value                      TTL
----------------------------------------------------------
CNAME         hello   tintum-web.web.app         Automatic  ✅ (Ya existe)
A             @       151.101.1.195             Automatic  ⬅️ AGREGAR
A             @       151.101.65.195            Automatic  ⬅️ AGREGAR (si hay más)
CNAME         www     tintum-redirect.web.app   Automatic  ⬅️ MODIFICAR/AGREGAR
```

**Nota:** Las IPs son ejemplos. Usa las IPs reales que Firebase te proporcione.

---

## 🔍 Verificar después de Configurar

Espera 15-30 minutos para la propagación DNS y luego verifica:

```bash
# Verificar tintum.app
dig tintum.app A +short
# Debería mostrar las IPs de Firebase

# Verificar www.tintum.app
dig www.tintum.app CNAME +short
# Debería mostrar: tintum-redirect.web.app

# Verificar redirecciones
curl -I https://tintum.app
# Debería mostrar: 301 Moved Permanently
#                  Location: https://hello.tintum.app

curl -I https://www.tintum.app
# Debería mostrar: 301 Moved Permanently
#                  Location: https://hello.tintum.app
```

---

## ⚠️ Puntos Importantes

1. **Para `tintum.app`**: Usa registros **A** (NO CNAME) porque es el dominio raíz
2. **Para `www.tintum.app`**: Usa **CNAME** apuntando a `tintum-redirect.web.app`
3. **Para `hello.tintum.app`**: Ya está configurado - no modificar
4. **Espera 15-30 minutos** después de hacer cambios en Namecheap
5. Firebase configurará SSL automáticamente (1-2 horas después de verificar DNS)

---

## 🆘 Si Algo No Funciona

1. Verifica que los valores en Namecheap sean exactos (sin espacios, sin `https://`)
2. Verifica que el Host sea exactamente `@`, `www`, o `hello`
3. Verifica en Firebase Console que los dominios estén agregados y su estado
4. Espera más tiempo para la propagación DNS (puede tardar hasta 48 horas)
5. Verifica que el sitio `tintum-redirect` esté desplegado:
   ```bash
   firebase deploy --only hosting:tintum-redirect
   ```

---

## 📚 Enlaces Útiles

- [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
- [Namecheap DNS Management](https://www.namecheap.com/myaccount/login/)

