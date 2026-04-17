@echo off
echo.
echo 🚀 QRForge Setup for Windows
echo =====================================

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python not found!
    echo    Please download from https://www.python.org/downloads/
    echo    Make sure to check "Add python.exe to PATH"
    pause
    exit /b
)

echo ✓ Python found. Creating virtual environment...
python -m venv venv

echo ✓ Installing dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo To run QRForge in the future:
echo   1. Double-click run.bat  (we'll create it)
echo   or
echo   2. Run this command:
echo      venv\Scripts\activate.bat && python qrforge.py
echo.
pause