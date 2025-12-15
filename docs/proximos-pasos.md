---
layout: default
title: Próximos Pasos
description: Checklist de pasos para completar la configuración de Tintum.app
---

# Próximos Pasos

Esta guía te ayudará a completar la configuración del proyecto Tintum.app.

## ✅ Completado

- [x] Estructura del proyecto creada
- [x] Repositorio Git inicializado
- [x] Conexión a GitHub configurada
- [x] Documentación con Markdown y Liquid creada
- [x] Conexión a Firebase verificada
- [x] Configuración de SSL automático documentada
- [x] Configuración de redirecciones preparada

## 📋 Pendiente

### 1. Crear Sitios Adicionales en Firebase

Necesitas crear dos sitios adicionales para las redirecciones:

1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Haz clic en **"Add another site"** o **"Agregar otro sitio"**
3. Crea:
   - `tintum-redirect` (para redirigir tintum.app)
   - `www-redirect` (para redirigir www.tintum.app)

**Comando para verificar:**
```bash
firebase hosting:sites:list
```

### 2. Configurar Dominio Principal (hello.tintum.app)

1. En el sitio `tintum-web`, agrega el dominio: `hello.tintum.app`
2. Configura CNAME en Namecheap:
   ```
   Type: CNAME
   Host: hello
   Value: tintum-web.web.app
   TTL: Automatic
   ```
3. Espera verificación y SSL (1-2 horas)

### 3. Configurar Dominio de Redirección (tintum.app)

1. En el sitio `tintum-redirect`, agrega el dominio: `tintum.app`
2. Firebase te dará direcciones IP (A/AAAA records)
3. Configura en Namecheap:
   ```
   Type: A Record
   Host: @
   Value: [IPs de Firebase]
   TTL: Automatic
   ```
4. Espera verificación y SSL (1-2 horas)

### 4. Configurar Dominio de Redirección (www.tintum.app)

1. En el sitio `www-redirect`, agrega el dominio: `www.tintum.app`
2. Configura CNAME en Namecheap:
   ```
   Type: CNAME
   Host: www
   Value: [URL del sitio www-redirect, ej: www-redirect.web.app]
   TTL: Automatic
   ```
3. Espera verificación y SSL (1-2 horas)

### 5. Primer Despliegue

Una vez configurados los dominios:

```bash
# Desplegar todos los sitios
firebase deploy --only hosting
```

### 6. Verificar Redirecciones

```bash
# Verificar redirecciones
curl -I https://tintum.app
curl -I https://www.tintum.app
curl -I https://hello.tintum.app

# O usar el script
./configurar-dominio.sh
```

### 7. Agregar Iconos PWA

Si aún no lo has hecho:

```bash
# Usar el logo optimizado
python3 optimizar-iconos.py ruta/al/logo.png
```

### 8. Personalizar Contenido

- Editar `web/index.html`
- Personalizar `web/css/styles.css`
- Agregar funcionalidad en `web/js/app.js`

## 🎯 Orden Recomendado

1. **Crear sitios en Firebase Console** (5 minutos)
2. **Configurar hello.tintum.app** (15 minutos + espera DNS)
3. **Hacer primer despliegue** (2 minutos)
4. **Configurar tintum.app y www.tintum.app** (30 minutos + espera DNS)
5. **Verificar que todo funciona** (5 minutos)

## 📚 Documentación de Referencia

- [Configuración Inicial]({{ '/configuracion-inicial' | relative_url }})
- [Despliegue]({{ '/despliegue' | relative_url }})
- [Configurar Dominio Personalizado]({{ '/configurar-dominio-personalizado' | relative_url }})
- [SSL y Redirecciones]({{ '/configuracion-ssl-redirecciones' | relative_url }})
- [Estado de Firebase]({{ '/estado-firebase' | relative_url }})

## ⚠️ Notas Importantes

- Los certificados SSL se configuran automáticamente con Let's Encrypt (1-2 horas)
- La propagación DNS puede tardar 15-30 minutos
- Verifica el estado en Firebase Console antes de continuar
- Todos los dominios deben estar "Connected" antes de desplegar

## 🆘 Si Tienes Problemas

Consulta la sección de Troubleshooting en:
- [Configurar Dominio Personalizado]({{ '/configurar-dominio-personalizado' | relative_url }}#troubleshooting)
- [SSL y Redirecciones]({{ '/configuracion-ssl-redirecciones' | relative_url }}#troubleshooting)

