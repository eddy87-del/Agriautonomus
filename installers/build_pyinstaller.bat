@echo off
REM Build script for PyInstaller to create a single-file EXE for the Agriautonomus main entrypoint.
REM Run this from the repository root in Windows cmd.exe

setlocal enabledelayedexpansion
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

REM Build main.py (change to agriautonomous.py if you prefer that as entrypoint)
pyinstaller --noconfirm --onefile --name Agriautonomus main.py

echo.
echo PyInstaller build finished. The EXE will be in the dist\ directory.
pause
