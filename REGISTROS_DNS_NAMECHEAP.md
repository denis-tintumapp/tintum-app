# Registros DNS en Namecheap para Tintum.app

## 📋 Resumen de Registros Necesarios

Para que funcionen todos los dominios, necesitas estos registros en Namecheap:

| Dominio | Tipo | Host | Valor | Estado |
|---------|------|------|-------|--------|
| `hello.tintum.app` | CNAME | `hello` | `tintum-web.web.app` | ✅ Ya configurado |
| `tintum.app` | A | `@` | [IPs de Firebase] | ⏳ Pendiente |
| `www.tintum.app` | CNAME | `www` | [URL del sitio] | ⏳ Pendiente |

---

## 🔧 Configuración Detallada en Namecheap

### Paso 1: Acceder a Namecheap

1. Inicia sesión en [Namecheap](https://www.namecheap.com/)
2. Ve a **Domain List** (Lista de Dominios)
3. Encuentra `tintum.app` y haz clic en **Manage**

---

## ✅ Registro 1: hello.tintum.app (Ya Funcionando)

**Este ya está configurado y funcionando.** Solo verifica que exista:

```
Type: CNAME Record
Host: hello
Value: tintum-web.web.app
TTL: Automatic (o 30 min)
```

**No modifiques este registro** - ya está funcionando correctamente.

---

## ⏳ Registro 2: tintum.app (Necesita Configuración)

### Paso 1: Obtener las IPs de Firebase

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-redirect`**
3. Verifica que `tintum.app` esté en la lista de dominios
4. Si no está, agrégalo:
   - Haz clic en **"Add custom domain"**
   - Ingresa: `tintum.app`
   - Firebase te mostrará las direcciones IP que necesitas

### Paso 2: Configurar en Namecheap

En Namecheap → Advanced DNS, agrega **registros A**:

```
Type: A Record
Host: @
Value: [Primera IP de Firebase]
TTL: Automatic
```

**Importante:** Firebase puede darte 2-4 IPs. Debes agregar **TODAS** como registros A separados.

**Ejemplo si Firebase te da estas IPs:**
- `151.101.1.195`
- `151.101.65.195`

Agrega:
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

### Paso 3: Si Firebase también da IPv6 (AAAA)

Si Firebase proporciona direcciones IPv6, agrega también:

```
Type: AAAA Record
Host: @
Value: [IPv6 de Firebase]
TTL: Automatic
```

**⚠️ Importante:**
- El Host debe ser `@` (arroba) para el dominio raíz
- NO uses CNAME para el dominio raíz (`tintum.app`)
- Debes agregar TODAS las IPs que Firebase te proporcione

---

## ⏳ Registro 3: www.tintum.app (Necesita Configuración)

### Paso 1: Crear el sitio en Firebase (si no existe)

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Haz clic en **"Add another site"**
3. Crea el sitio (nombre sugerido: `www-redirect` o el que prefieras)
4. **Anota el Site ID** que Firebase te da

### Paso 2: Agregar dominio en Firebase

1. Selecciona el sitio que acabas de crear
2. Haz clic en **"Add custom domain"**
3. Ingresa: `www.tintum.app`
4. Firebase te mostrará las instrucciones (generalmente CNAME)

### Paso 3: Configurar en Namecheap

En Namecheap → Advanced DNS, agrega:

```
Type: CNAME Record
Host: www
Value: [URL del sitio, ej: www-redirect.web.app]
TTL: Automatic (o 30 min)
```

**El valor exacto** dependerá del Site ID que Firebase te dio. Ejemplos:
- Si el Site ID es `www-redirect` → Valor: `www-redirect.web.app`
- Si el Site ID es `redirect-abc123` → Valor: `redirect-abc123.web.app`

**⚠️ Importante:**
- El Host debe ser `www` (sin el punto)
- El valor debe ser exactamente `[site-id].web.app`
- No incluyas `https://` ni `/` al final

---

## 📝 Ejemplo Completo de Configuración en Namecheap

Aquí está cómo debería verse tu configuración completa en Namecheap Advanced DNS:

```
Type          Host    Value                      TTL
----------------------------------------------------------
CNAME         hello   tintum-web.web.app         Automatic
A             @       151.101.1.195             Automatic
A             @       151.101.65.195            Automatic
CNAME         www     www-redirect.web.app       Automatic
```

**Nota:** 
- Las IPs son ejemplos - Firebase te dará las IPs reales
- El valor de `www` puede variar según el Site ID que Firebase te asigne

---

## ✅ Verificar Configuración

Después de configurar, verifica con estos comandos:

```bash
# Verificar hello.tintum.app
dig hello.tintum.app CNAME +short
# Debería mostrar: tintum-web.web.app

# Verificar tintum.app
dig tintum.app A +short
# Debería mostrar las IPs de Firebase

# Verificar www.tintum.app
dig www.tintum.app CNAME +short
# Debería mostrar: [site-id].web.app
```

---

## ⚠️ Errores Comunes

### Error: "CNAME and other records conflict"

- **Causa:** Tienes un CNAME en `@` junto con registros A
- **Solución:** Para el dominio raíz (`tintum.app`), usa SOLO registros A/AAAA, NO CNAME

### Error: El dominio no resuelve

- **Causa:** Los registros no están configurados o hay un error de tipeo
- **Solución:** 
  - Verifica que el Host sea exactamente `@` o `hello` o `www`
  - Verifica que los valores sean exactos (sin espacios, sin `https://`)
  - Espera 15-30 minutos para la propagación DNS

### Error: El valor no coincide

- **Causa:** El valor del CNAME no coincide con el Site ID real
- **Solución:** Verifica el Site ID real en Firebase Console y actualiza el valor

---

## 🔄 Orden de Configuración Recomendado

1. **Primero:** Configura `tintum.app` (registros A)
2. **Segundo:** Crea el sitio para `www.tintum.app` en Firebase
3. **Tercero:** Configura `www.tintum.app` (CNAME)
4. **Cuarto:** Espera 15-30 minutos para propagación DNS
5. **Quinto:** Verifica que todo funcione

---

## 📚 Referencias

- [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
- [Namecheap DNS Management](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-configure-dns-records-for-your-domain/)

---

## 💡 Resumen Rápido

**Para `tintum.app`:**
- Tipo: **A Record** (múltiples, una por cada IP)
- Host: **@**
- Valor: **IPs de Firebase** (obtener desde Firebase Console)

**Para `www.tintum.app`:**
- Tipo: **CNAME Record**
- Host: **www**
- Valor: **`[site-id].web.app`** (obtener desde Firebase Console)

**Para `hello.tintum.app`:**
- ✅ Ya está configurado - no modificar

