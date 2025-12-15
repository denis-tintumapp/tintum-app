# Configuración Final en Namecheap

## ✅ Configuración Completada en Firebase

He configurado Firebase para que:
- `tintum.app` → Redirige a `https://hello.tintum.app` (sitio `tintum-redirect`)
- `www.tintum.app` → Redirige a `https://hello.tintum.app` (mismo sitio `tintum-redirect`)

## 📋 Registros a Configurar en Namecheap

Ve a Namecheap → Domain List → `tintum.app` → Manage → **Advanced DNS**

### Registros que DEBES tener:

#### 1. hello.tintum.app (Ya configurado - NO MODIFICAR)
```
Type: CNAME Record
Host: hello
Value: tintum-web.web.app
TTL: Automatic
```
✅ Este ya está funcionando - no lo toques

---

#### 2. tintum.app (AGREGAR - Registros A)

Firebase te dará direcciones IP cuando agregues el dominio. Necesitas agregar **registros A**:

```
Type: A Record
Host: @
Value: [Primera IP de Firebase]
TTL: Automatic
```

**IMPORTANTE:** Firebase puede darte 2-4 IPs. Debes agregar **TODAS** como registros A separados.

**Ejemplo si Firebase te da estas IPs:**
- `151.101.1.195`
- `151.101.65.195`

Agrega en Namecheap:
```
A Record | @ | 151.101.1.195 | Automatic
A Record | @ | 151.101.65.195 | Automatic
```

**Cómo obtener las IPs:**
1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-redirect`**
3. Si `tintum.app` no está en la lista, haz clic en **"Add custom domain"**
4. Ingresa: `tintum.app`
5. Firebase te mostrará las IPs que debes usar

---

#### 3. www.tintum.app (MODIFICAR - CNAME)

Modifica el registro CNAME existente para que apunte al sitio correcto:

```
Type: CNAME Record
Host: www
Value: tintum-redirect.web.app
TTL: Automatic
```

**Acción:** 
- Si ya existe un CNAME para `www`, modifica el valor a: `tintum-redirect.web.app`
- Si no existe, agrégalo con el valor: `tintum-redirect.web.app`

---

## 📝 Resumen de Configuración en Namecheap

Tu configuración en Namecheap Advanced DNS debería verse así:

```
Type          Host    Value                      TTL
----------------------------------------------------------
CNAME         hello   tintum-web.web.app         Automatic
A             @       151.101.1.195             Automatic  ← Agregar
A             @       151.101.65.195            Automatic  ← Agregar (si hay más IPs)
CNAME         www     tintum-redirect.web.app    Automatic  ← Modificar
```

**Nota:** Las IPs son ejemplos. Firebase te dará las IPs reales cuando agregues `tintum.app` como dominio.

---

## ✅ Pasos en Namecheap

### Paso 1: Para tintum.app

1. Obtén las IPs desde Firebase Console (sitio `tintum-redirect`, dominio `tintum.app`)
2. En Namecheap → Advanced DNS → Host Records
3. Haz clic en **"Add New Record"**
4. Agrega registros A:
   - Type: **A Record**
   - Host: **@**
   - Value: **[Primera IP de Firebase]**
   - TTL: **Automatic**
5. Repite para cada IP adicional que Firebase te dé

### Paso 2: Para www.tintum.app

1. En Namecheap → Advanced DNS → Host Records
2. Busca el registro CNAME existente para `www`
3. Si existe, haz clic en el ícono de edición (lápiz)
4. Modifica el Value a: **`tintum-redirect.web.app`**
5. Si no existe, agrégalo:
   - Type: **CNAME Record**
   - Host: **www**
   - Value: **tintum-redirect.web.app**
   - TTL: **Automatic**
6. Guarda los cambios

---

## 🔍 Verificar después de Configurar

Espera 15-30 minutos y verifica:

```bash
# Verificar tintum.app
dig tintum.app A +short
# Debería mostrar las IPs de Firebase

# Verificar www.tintum.app
dig www.tintum.app CNAME +short
# Debería mostrar: tintum-redirect.web.app

# Verificar redirecciones
curl -I https://tintum.app
# Debería mostrar: 301 → Location: https://hello.tintum.app

curl -I https://www.tintum.app
# Debería mostrar: 301 → Location: https://hello.tintum.app
```

---

## ⚠️ Importante

- **NO modifiques** el registro CNAME de `hello` - ya está funcionando
- Para `tintum.app` usa **registros A** (NO CNAME) porque es el dominio raíz
- Para `www.tintum.app` usa **CNAME** apuntando a `tintum-redirect.web.app`
- Espera 15-30 minutos para la propagación DNS después de hacer cambios

---

## 🆘 Si Tienes Problemas

1. Verifica que los valores sean exactos (sin espacios, sin `https://`)
2. Verifica que el Host sea exactamente `@` o `www` o `hello`
3. Espera más tiempo para la propagación DNS (puede tardar hasta 48 horas)
4. Verifica en Firebase Console que los dominios estén "Connected"

