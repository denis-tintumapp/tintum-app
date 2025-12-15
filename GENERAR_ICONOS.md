# Generar Iconos y Favicons desde el Logo

## 📋 Pasos para Generar los Iconos

### Paso 1: Colocar el Logo en el Proyecto

Coloca tu archivo de logo (PNG, JPG, SVG) en una ubicación accesible. Por ejemplo:

```bash
# Opción 1: En la carpeta de imágenes del proyecto
cp ruta/al/logo.png web/images/logo-original.png

# Opción 2: Usar la ruta completa
# python3 optimizar-iconos.py ~/Downloads/logo-tintum.png
```

### Paso 2: Ejecutar el Script

```bash
cd /Users/denispaiva/proyectos/tintum-app
python3 optimizar-iconos.py web/images/logo-original.png
```

O si el logo está en otra ubicación:

```bash
python3 optimizar-iconos.py ~/Downloads/logo-tintum.png
```

### Paso 3: Verificar los Iconos Generados

El script generará automáticamente:

**En `web/icons/`:**
- `icon-192.png` (192x192) - PWA estándar
- `icon-512.png` (512x512) - PWA alta resolución
- `favicon.png` (32x32) - Favicon del navegador
- `apple-touch-icon.png` (180x180) - iOS/Apple
- `icon-16.png`, `icon-32.png`, `icon-96.png` - Tamaños adicionales

**En `web/images/`:**
- `logo.png` - Logo optimizado
- `logo-large.png` - Logo grande (si aplica)

## ✅ Verificar que Funciona

Después de generar los iconos, verifica que estén en su lugar:

```bash
ls -la web/icons/
ls -la web/images/
```

## 🚀 Desplegar

Una vez generados los iconos, despliega los cambios:

```bash
firebase deploy --only hosting:tintum-web
```

## 📝 Notas

- El script mantiene el fondo morado (#4a148c) del logo original
- Los iconos se generan con padding para que se vean bien en diferentes tamaños
- El favicon es más pequeño y compacto para mejor visibilidad
- Todos los iconos están optimizados para web

## 🆘 Si Tienes Problemas

### Error: "Pillow no está instalado"

```bash
pip3 install Pillow
```

### Error: "El archivo no existe"

Verifica la ruta del archivo:
```bash
ls -la ruta/al/logo.png
```

O usa la ruta absoluta:
```bash
python3 optimizar-iconos.py /ruta/completa/al/logo.png
```

### Los iconos no se ven bien

El script está configurado para mantener el fondo morado. Si necesitas ajustar el padding o el fondo, edita el script `optimizar-iconos.py`.

