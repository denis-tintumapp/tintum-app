# Clarificación: Sitios en Firebase

## 📊 Situación Actual

### Proyecto: `tintum-web` (Proyecto Principal)

Este es el proyecto que estamos usando. Tiene **2 sitios**:

1. **`tintum-web`** 
   - URL por defecto: `https://tintum-web.web.app`
   - Dominio personalizado: `hello.tintum.app`
   - **Propósito**: Contenido principal de la aplicación
   - **Estado**: ✅ Necesario

2. **`tintum-redirect`**
   - URL por defecto: `https://tintum-redirect.web.app`
   - Dominios personalizados: `tintum.app`, `www.tintum.app`
   - **Propósito**: Redirigir a `hello.tintum.app`
   - **Estado**: ✅ Necesario

### Proyecto: `tintum-hello-app` (Otro Proyecto)

Este es un **proyecto diferente** (no un sitio). Puede tener sus propios sitios, pero **NO es necesario** para la configuración actual.

---

## ✅ Respuesta: ¿Qué Debe Existir?

### En el Proyecto `tintum-web`:

**SÍ, ambos sitios deben existir:**
- ✅ `tintum-web` - Para el contenido principal (`hello.tintum.app`)
- ✅ `tintum-redirect` - Para las redirecciones (`tintum.app`, `www.tintum.app`)

### Proyecto `tintum-hello-app`:

**NO es necesario** para la configuración actual. Es un proyecto separado que puedes:
- Mantener si lo usas para otra cosa
- Eliminar si no lo necesitas
- Ignorar si no afecta a `tintum-web`

---

## 🎯 Configuración Correcta

### Estructura de Sitios en `tintum-web`:

```
Proyecto: tintum-web
├── Sitio: tintum-web
│   └── Dominio: hello.tintum.app (contenido principal)
│
└── Sitio: tintum-redirect
    ├── Dominio: tintum.app (redirige a hello.tintum.app)
    └── Dominio: www.tintum.app (redirige a hello.tintum.app)
```

### Archivos de Configuración:

- `firebase.json` - Configura ambos sitios
- `.firebasehosting.json` - Mapea los targets a los sitios
- `.firebaserc` - Define el proyecto actual (`tintum-web`)

---

## ⚠️ Si Ves `hello-app` como Sitio

Si en Firebase Console ves un sitio llamado `hello-app` dentro del proyecto `tintum-web`, puede ser:

1. **Un sitio antiguo** que ya no se usa - Puedes eliminarlo si no tiene dominios configurados
2. **Un sitio creado por error** - Puedes eliminarlo
3. **Un sitio que se creó automáticamente** - Verifica si tiene dominios configurados antes de eliminarlo

---

## 🔍 Cómo Verificar

```bash
# Ver sitios en el proyecto actual
firebase hosting:sites:list

# Ver información de un sitio específico
firebase hosting:sites:get tintum-web
firebase hosting:sites:get tintum-redirect
```

---

## 📝 Resumen

| Elemento | Debe Existir? | Propósito |
|----------|---------------|-----------|
| Proyecto `tintum-web` | ✅ SÍ | Proyecto principal |
| Sitio `tintum-web` | ✅ SÍ | Contenido en `hello.tintum.app` |
| Sitio `tintum-redirect` | ✅ SÍ | Redirecciones |
| Proyecto `tintum-hello-app` | ❓ Opcional | Proyecto diferente, no necesario |
| Sitio `hello-app` (si existe) | ❓ Verificar | Puede ser antiguo o innecesario |

---

## 🆘 Si Tienes Dudas

1. Verifica qué dominios tiene cada sitio en Firebase Console
2. Si un sitio no tiene dominios configurados y no lo usas, puedes eliminarlo
3. El proyecto `tintum-hello-app` es independiente y no afecta a `tintum-web`

