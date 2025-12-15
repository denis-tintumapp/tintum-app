#!/bin/bash

# Script para optimizar y generar iconos PWA desde el logo de Tintum.app
# Uso: ./optimizar-iconos.sh ruta/al/logo.png

if [ -z "$1" ]; then
    echo "Error: Debes proporcionar la ruta al archivo del logo"
    echo "Uso: ./optimizar-iconos.sh ruta/al/logo.png"
    exit 1
fi

LOGO_FILE="$1"
ICONS_DIR="web/icons"
IMAGES_DIR="web/images"

# Verificar que el archivo existe
if [ ! -f "$LOGO_FILE" ]; then
    echo "Error: El archivo $LOGO_FILE no existe"
    exit 1
fi

# Crear directorios si no existen
mkdir -p "$ICONS_DIR"
mkdir -p "$IMAGES_DIR"

# Verificar si ImageMagick está instalado
if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick no está instalado"
    echo "Instálalo con: brew install imagemagick"
    exit 1
fi

echo "Optimizando y generando iconos..."

# Copiar logo original a images (optimizado)
convert "$LOGO_FILE" -resize 1024x1024 -quality 90 "$IMAGES_DIR/logo.png"

# Generar icono 192x192
convert "$LOGO_FILE" -resize 192x192 -background none -gravity center -extent 192x192 "$ICONS_DIR/icon-192.png"

# Generar icono 512x512
convert "$LOGO_FILE" -resize 512x512 -background none -gravity center -extent 512x512 "$ICONS_DIR/icon-512.png"

# Generar favicon (32x32)
convert "$LOGO_FILE" -resize 32x32 -background none -gravity center -extent 32x32 "$ICONS_DIR/favicon.png"

# Generar apple-touch-icon (180x180)
convert "$LOGO_FILE" -resize 180x180 -background none -gravity center -extent 180x180 "$ICONS_DIR/apple-touch-icon.png"

echo "✓ Iconos generados exitosamente en $ICONS_DIR"
echo "✓ Logo optimizado guardado en $IMAGES_DIR/logo.png"
echo ""
echo "Iconos creados:"
echo "  - icon-192.png (192x192)"
echo "  - icon-512.png (512x512)"
echo "  - favicon.png (32x32)"
echo "  - apple-touch-icon.png (180x180)"

