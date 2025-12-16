#!/bin/bash

# Script para optimizar el logo principal usando herramientas nativas de macOS
# Optimiza "Logo Tintum.png" para uso web

INPUT="web/images/Logo Tintum.png"
OUTPUT="web/images/logo-principal.png"

if [ ! -f "$INPUT" ]; then
    echo "Error: No se encontró el archivo $INPUT"
    exit 1
fi

echo "Optimizando logo principal..."
echo "Archivo origen: $INPUT"

# Obtener dimensiones originales
WIDTH=$(sips -g pixelWidth "$INPUT" 2>/dev/null | awk '/pixelWidth:/ {print $2}')
HEIGHT=$(sips -g pixelHeight "$INPUT" 2>/dev/null | awk '/pixelHeight:/ {print $2}')

echo "Dimensiones originales: ${WIDTH}x${HEIGHT}"

# Redimensionar a máximo 300px manteniendo aspecto (si es necesario)
if [ "$WIDTH" -gt 300 ] || [ "$HEIGHT" -gt 300 ]; then
    echo "Redimensionando a máximo 300px..."
    sips -Z 300 "$INPUT" --out "$OUTPUT" > /dev/null 2>&1
else
    echo "Copiando archivo (ya está en tamaño óptimo)..."
    cp "$INPUT" "$OUTPUT"
fi

# Obtener tamaño del archivo
FILE_SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
NEW_WIDTH=$(sips -g pixelWidth "$OUTPUT" 2>/dev/null | awk '/pixelWidth:/ {print $2}')
NEW_HEIGHT=$(sips -g pixelHeight "$OUTPUT" 2>/dev/null | awk '/pixelHeight:/ {print $2}')

echo ""
echo "✓ Logo optimizado: $OUTPUT"
echo "  Dimensiones: ${NEW_WIDTH}x${NEW_HEIGHT}px"
echo "  Tamaño: $FILE_SIZE"

