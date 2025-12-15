#!/bin/bash

# Script para verificar la configuración DNS de tintum.app
# Uso: ./configurar-dominio.sh

echo "🔍 Verificando configuración DNS para tintum.app"
echo ""

# Verificar registros A
echo "📋 Registros A (IPv4):"
dig +short tintum.app A
echo ""

# Verificar registros AAAA
echo "📋 Registros AAAA (IPv6):"
dig +short tintum.app AAAA
echo ""

# Verificar registro TXT
echo "📋 Registros TXT:"
dig +short tintum.app TXT
echo ""

# Verificar resolución completa
echo "🌐 Resolución completa:"
nslookup tintum.app
echo ""

# Verificar conectividad HTTPS
echo "🔒 Verificando SSL:"
curl -I https://tintum.app 2>&1 | head -10
echo ""

echo "✅ Verificación completada"
echo ""
echo "💡 Si los registros A no aparecen, asegúrate de:"
echo "   1. Haber configurado los registros A en Namecheap"
echo "   2. Esperar 15-30 minutos para la propagación DNS"
echo "   3. Verificar que el Host sea '@' para el dominio raíz"

