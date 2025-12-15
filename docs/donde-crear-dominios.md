---
layout: default
title: Dónde Crear los Dominios Personalizados
description: Guía clara sobre en qué proyecto y sitio crear cada dominio
category: guide
---

# Dónde Crear los Dominios Personalizados

## 📌 Resumen

**Proyecto Firebase:** `tintum-web` (este es el único proyecto que usamos)

Dentro de este proyecto, tienes **múltiples sitios de hosting**. Cada dominio personalizado se agrega a un sitio específico.

---

## 🎯 Configuración de Dominios

### Proyecto: `tintum-web`

#### Sitio: `tintum-web` → Dominio: `hello.tintum.app`

**Dónde agregarlo:**
1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-web`** (el primero de la lista)
3. Haz clic en **"Add custom domain"** o **"Agregar dominio personalizado"**
4. Ingresa: `hello.tintum.app`
5. Configura el CNAME en Namecheap: `hello` → `tintum-web.web.app`

**Este es el sitio principal** que mostrará tu aplicación.

---

#### Sitio: `tintum-redirect` → Dominio: `tintum.app`

**Dónde agregarlo:**
1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona el sitio **`tintum-redirect`** (el segundo de la lista)
3. Haz clic en **"Add custom domain"** o **"Agregar dominio personalizado"**
4. Ingresa: `tintum.app`
5. Configura los registros A/AAAA en Namecheap con las IPs que Firebase te proporcione

**Este sitio solo redirige** a `https://hello.tintum.app`.

---

#### Sitio: `[por-crear]` → Dominio: `www.tintum.app`

**Dónde agregarlo:**
1. Primero crea el sitio desde [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
   - Haz clic en **"Add another site"**
   - Nombre sugerido: `www-redirect` o el que prefieras
2. Una vez creado, selecciona ese sitio
3. Haz clic en **"Add custom domain"**
4. Ingresa: `www.tintum.app`
5. Configura el CNAME en Namecheap: `www` → `[url-del-sitio].web.app`

**Este sitio también redirige** a `https://hello.tintum.app`.

---

## 📋 Tabla de Resumen

| Dominio | Proyecto | Sitio | Tipo DNS | Propósito |
|---------|----------|-------|----------|-----------|
| `hello.tintum.app` | `tintum-web` | `tintum-web` | CNAME | Contenido principal |
| `tintum.app` | `tintum-web` | `tintum-redirect` | A/AAAA | Redirige a hello.tintum.app |
| `www.tintum.app` | `tintum-web` | `[por-crear]` | CNAME | Redirige a hello.tintum.app |

---

## 🔍 Verificar

### Ver el proyecto actual:
```bash
firebase use
```
Debería mostrar: `tintum-web`

### Ver los sitios disponibles:
```bash
firebase hosting:sites:list
```

Deberías ver:
- `tintum-web`
- `tintum-redirect`
- `[el sitio para www cuando lo crees]`

### Ver dominios de un sitio específico:

Desde Firebase Console:
1. Ve a [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
2. Selecciona un sitio
3. Verás la sección "Domains" con los dominios agregados

---

## ⚠️ Importante

- **NO crees los dominios en otros proyectos** (como `tintum-hello-app` o `cata-pwa-dev`)
- **Todos los dominios van en el proyecto `tintum-web`**
- **Cada dominio va en su sitio correspondiente** dentro de `tintum-web`

---

## 🎯 Pasos en Orden

1. ✅ Proyecto `tintum-web` ya está seleccionado
2. ✅ Sitio `tintum-web` existe → Agregar `hello.tintum.app`
3. ✅ Sitio `tintum-redirect` existe → Agregar `tintum.app`
4. ⏳ Crear sitio para www → Agregar `www.tintum.app`
5. ⏳ Configurar DNS en Namecheap para cada uno
6. ⏳ Desplegar: `firebase deploy --only hosting`

---

## 📚 Referencias

- [Firebase Console - Hosting](https://console.firebase.google.com/project/tintum-web/hosting)
- [Configuración DNS en Namecheap]({{ '/configuracion-dns-namecheap' | relative_url }})
- [Inicializar Hosting]({{ '/inicializar-hosting' | relative_url }})

