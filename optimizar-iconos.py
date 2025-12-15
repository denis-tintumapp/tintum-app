#!/usr/bin/env python3
"""
Script para optimizar y generar iconos PWA desde el logo de Tintum.app
Uso: python3 optimizar-iconos.py ruta/al/logo.png
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image, ImageOps, ImageFilter
except ImportError:
    print("Error: Pillow no está instalado")
    print("Instálalo con: pip3 install Pillow")
    sys.exit(1)


def create_icon(input_path, output_path, size, background_color=None, padding=0.1):
    """Crea un icono del tamaño especificado"""
    try:
        # Abrir imagen original
        img = Image.open(input_path)
        
        # Convertir a RGBA si no lo es
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Si la imagen tiene fondo, extraer solo el logo (asumiendo que el logo es blanco/claro)
        # Para logos con fondo morado, podemos mantener el fondo o hacerlo transparente
        # Opción 1: Mantener el fondo original
        # Opción 2: Hacer el fondo transparente (si el logo es blanco sobre morado)
        
        # Calcular el tamaño con padding
        target_size = int(size * (1 - padding * 2))
        
        # Redimensionar manteniendo aspecto
        img.thumbnail((target_size, target_size), Image.Resampling.LANCZOS)
        
        # Crear imagen cuadrada
        if background_color:
            # Usar color de fondo especificado (ej: morado #4a148c)
            new_img = Image.new('RGBA', (size, size), background_color)
        else:
            # Mantener fondo transparente o usar el fondo original
            # Si queremos mantener el fondo morado, lo detectamos
            new_img = Image.new('RGBA', (size, size), (74, 20, 140, 255))  # #4a148c con alpha
        
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


def create_favicon(input_path, output_path, size=32):
    """Crea un favicon optimizado"""
    try:
        img = Image.open(input_path)
        
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Para favicon, hacer más pequeño con menos padding
        target_size = int(size * 0.9)
        img.thumbnail((target_size, target_size), Image.Resampling.LANCZOS)
        
        # Crear con fondo morado
        new_img = Image.new('RGBA', (size, size), (74, 20, 140, 255))
        
        x = (size - img.width) // 2
        y = (size - img.height) // 2
        new_img.paste(img, (x, y), img)
        
        new_img.save(output_path, 'PNG', optimize=True)
        print(f"✓ Creado: {output_path} ({size}x{size})")
        
    except Exception as e:
        print(f"Error procesando favicon: {e}")


def main():
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar la ruta al archivo del logo")
        print("Uso: python3 optimizar-iconos.py ruta/al/logo.png")
        print("\nEjemplo:")
        print("  python3 optimizar-iconos.py ~/Downloads/logo-tintum.png")
        print("  python3 optimizar-iconos.py web/images/logo-original.png")
        sys.exit(1)
    
    logo_file = sys.argv[1]
    
    # Verificar que el archivo existe
    if not os.path.isfile(logo_file):
        print(f"Error: El archivo {logo_file} no existe")
        print(f"Ruta absoluta buscada: {os.path.abspath(logo_file)}")
        sys.exit(1)
    
    # Crear directorios
    icons_dir = Path("web/icons")
    images_dir = Path("web/images")
    icons_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("Generando iconos y favicons para Tintum.app")
    print("=" * 60)
    print(f"Archivo origen: {logo_file}")
    print()
    
    # Optimizar logo original
    try:
        img = Image.open(logo_file)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Guardar versión optimizada del logo
        img.save(images_dir / "logo.png", 'PNG', optimize=True)
        print(f"✓ Logo optimizado guardado: {images_dir / 'logo.png'}")
        
        # También guardar una versión grande para referencia
        if img.width < 1024 or img.height < 1024:
            img_large = img.copy()
            img_large.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
            img_large.save(images_dir / "logo-large.png", 'PNG', optimize=True)
            print(f"✓ Logo grande guardado: {images_dir / 'logo-large.png'}")
    except Exception as e:
        print(f"⚠ Error optimizando logo: {e}")
    
    print()
    print("Generando iconos PWA y favicons...")
    print("-" * 60)
    
    # Color de fondo morado (#4a148c)
    bg_color = (74, 20, 140, 255)
    
    # Generar iconos PWA (con padding para que se vea bien)
    create_icon(logo_file, icons_dir / "icon-192.png", 192, bg_color, padding=0.15)
    create_icon(logo_file, icons_dir / "icon-512.png", 512, bg_color, padding=0.15)
    
    # Generar favicon (más pequeño, menos padding)
    create_favicon(logo_file, icons_dir / "favicon.png", 32)
    
    # Generar apple-touch-icon
    create_icon(logo_file, icons_dir / "apple-touch-icon.png", 180, bg_color, padding=0.15)
    
    # Generar iconos adicionales útiles
    create_icon(logo_file, icons_dir / "icon-16.png", 16, bg_color, padding=0.2)
    create_icon(logo_file, icons_dir / "icon-32.png", 32, bg_color, padding=0.15)
    create_icon(logo_file, icons_dir / "icon-96.png", 96, bg_color, padding=0.15)
    
    print()
    print("=" * 60)
    print("✓ Todos los iconos han sido generados exitosamente")
    print(f"  Ubicación: {icons_dir.absolute()}")
    print()
    print("Iconos creados:")
    print("  - icon-192.png (192x192) - PWA estándar")
    print("  - icon-512.png (512x512) - PWA alta resolución")
    print("  - favicon.png (32x32) - Favicon del navegador")
    print("  - apple-touch-icon.png (180x180) - iOS/Apple")
    print("  - icon-16.png, icon-32.png, icon-96.png - Tamaños adicionales")
    print()
    print("Logo guardado en:")
    print(f"  - {images_dir / 'logo.png'}")
    print("=" * 60)


if __name__ == "__main__":
    main()
