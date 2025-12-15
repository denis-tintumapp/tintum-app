#!/usr/bin/env python3
"""
Script para optimizar y generar iconos PWA desde el logo de Tintum.app
Uso: python3 optimizar-iconos.py ruta/al/logo.png
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Error: Pillow no está instalado")
    print("Instálalo con: pip3 install Pillow")
    sys.exit(1)


def create_icon(input_path, output_path, size, background=None):
    """Crea un icono del tamaño especificado"""
    try:
        # Abrir imagen original
        img = Image.open(input_path)
        
        # Convertir a RGBA si no lo es
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Redimensionar manteniendo aspecto
        img.thumbnail((size, size), Image.Resampling.LANCZOS)
        
        # Crear imagen cuadrada con fondo transparente o especificado
        if background:
            new_img = Image.new('RGBA', (size, size), background)
        else:
            new_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        
        # Centrar la imagen
        x = (size - img.width) // 2
        y = (size - img.height) // 2
        new_img.paste(img, (x, y), img)
        
        # Guardar optimizado
        new_img.save(output_path, 'PNG', optimize=True)
        print(f"✓ Creado: {output_path} ({size}x{size})")
        
    except Exception as e:
        print(f"Error procesando {output_path}: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar la ruta al archivo del logo")
        print("Uso: python3 optimizar-iconos.py ruta/al/logo.png")
        sys.exit(1)
    
    logo_file = sys.argv[1]
    
    # Verificar que el archivo existe
    if not os.path.isfile(logo_file):
        print(f"Error: El archivo {logo_file} no existe")
        sys.exit(1)
    
    # Crear directorios
    icons_dir = Path("web/icons")
    images_dir = Path("web/images")
    icons_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)
    
    print("Optimizando y generando iconos...")
    print(f"Archivo origen: {logo_file}")
    print()
    
    # Optimizar logo original
    try:
        img = Image.open(logo_file)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        img.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
        img.save(images_dir / "logo.png", 'PNG', optimize=True)
        print(f"✓ Logo optimizado: {images_dir / 'logo.png'}")
    except Exception as e:
        print(f"Error optimizando logo: {e}")
    
    print()
    
    # Generar iconos
    create_icon(logo_file, icons_dir / "icon-192.png", 192)
    create_icon(logo_file, icons_dir / "icon-512.png", 512)
    create_icon(logo_file, icons_dir / "favicon.png", 32)
    create_icon(logo_file, icons_dir / "apple-touch-icon.png", 180)
    
    print()
    print("✓ Todos los iconos han sido generados exitosamente")
    print(f"  Ubicación: {icons_dir.absolute()}")


if __name__ == "__main__":
    main()

