@echo off
REM Перейти в папку, где лежит сам батник (и скрипт)
pushd "%~dp0"
REM Запустить Python-скрипт
python generate_readme.py
REM Опционально: пауза, чтобы видеть вывод
pause
popd
