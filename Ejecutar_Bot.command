#!/bin/bash

# 1. Nos movemos a la carpeta donde está este script (el repositorio)
cd "$(dirname "$0")"

echo "================================================="
echo "Sincronizando con la última versión del bot..."
echo "================================================="

# 2. Descarga todo de GitHub y fuerza a la Mac a ser una copia exacta
# Nota: Si tu rama en GitHub se llama 'master' en lugar de 'main', cambia 'origin/main' por 'origin/master'
git fetch --all
git reset --hard origin/main

echo ""
echo "================================================="
echo "Iniciando el bot..."
echo "================================================="

# 3. AQUÍ VA EL COMANDO PARA EJECUTAR TU BOT
# Ejemplo si es Python: python3 main.py

echo ""
echo "Proceso finalizado. Puedes cerrar esta ventana."