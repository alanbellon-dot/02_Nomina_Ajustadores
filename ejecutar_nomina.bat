@echo off
title Bot de Nomina - Aseguradora Digital

echo === ACTUALIZANDO CODIGO DESDE GIT ===
git pull

echo.
echo === PREPARANDO ENTORNO VIRTUAL ===
if not exist venv (
    python -m venv venv
)

echo === ACTIVANDO ENTORNO E INSTALANDO DEPENDENCIAS ===
call venv\Scripts\activate
pip install -r requirements.txt
playwright install

echo.
echo === 🤖 INICIANDO BOT DE NOMINA ===
python main.py

echo.
echo Proceso terminado.
pause