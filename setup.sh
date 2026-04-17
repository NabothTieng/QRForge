#!/bin/bash
echo ""
echo "🚀 QRForge Setup for macOS / Linux"
echo "====================================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found!"
    echo "   Please install it:"
    echo "   macOS: brew install python3   (or from python.org)"
    echo "   Linux: sudo apt install python3 python3-venv"
    exit 1
fi

echo "✓ Python 3 found. Creating virtual environment..."
python3 -m venv venv

echo "✓ Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run QRForge in the future:"
echo "   1. Double-click run.sh     (we'll create it)"
echo "   or"
echo "   2. Run this command:"
echo "      source venv/bin/activate && python3 qrforge.py"
echo ""

# Make it executable automatically
chmod +x run.sh 2>/dev/null || true