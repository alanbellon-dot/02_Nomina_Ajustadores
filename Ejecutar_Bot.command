#!/bin/bash

# 1. Nos movemos a la carpeta del repositorio
cd "$(dirname "$0")"

echo "================================================="
echo "Sincronizando con la última versión del bot..."
echo "================================================="
git fetch --all
git reset --hard origin/main

echo ""
echo "================================================="
echo "Preparando Entorno Virtual..."
echo "================================================="
# Si la carpeta venv no existe, la crea
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

echo ""
echo "================================================="
echo "Activando entorno e instalando dependencias..."
echo "================================================="
# Activa el entorno en Mac
source venv/bin/activate

# Instala lo que está en requirements.txt y los navegadores de Playwright
pip3 install -r requirements.txt
playwright install

echo ""
echo "================================================="
echo "🤖 INICIANDO BOT DE NOMINA..."
echo "================================================="
# Ejecuta tu código principal
python3 main.py

echo ""
echo "Proceso terminado. Presiona cualquier tecla para cerrar esta ventana..."
read -n 1 -s