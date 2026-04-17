# QRForge — Reader Guide

A clean, interactive Python tool to generate professional QR codes with custom colors, rounded logo backgrounds, and high error correction.

---

## What It Does

- Fully interactive — no code editing needed
- Custom foreground & background colors (hex support)
- Logo embedding with preserved aspect ratio
- Rounded corners on logo background
- High error correction (`H` level) for reliable scanning even with logos
- Smart filename handling — no accidental overwrites
- Cross-platform: Windows, macOS, Linux

---

## Project Structure

```
qrforge/
├── qrforge.py
├── requirements.txt
├── setup.bat          # Windows one-click setup
├── setup.sh           # macOS & Linux setup
├── run.bat            # Windows quick run
├── run.sh             # macOS & Linux quick run
├── README.md
├── .gitignore
└── output/            # Generated QR codes (git-ignored)
```

---

## Installation

### Option 1: One-Click Setup (Recommended)

**Windows:**
1. Double-click `setup.bat`
2. Double-click `run.bat` to launch

**macOS & Linux:**
```bash
chmod +x setup.sh run.sh
./setup.sh
./run.sh
```

### Option 2: Manual Setup

```bash
# Create virtual environment
python -m venv venv          # Windows
python3 -m venv venv         # macOS / Linux

# Activate
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run
python qrforge.py            # Windows
python3 qrforge.py           # macOS / Linux
```

---

## Usage

QRForge guides you step-by-step at runtime:

1. Enter the URL or text to encode
2. Choose a filename
3. Set foreground & background colors (e.g. `#4A2C7A`)
4. Optionally embed a logo (PNG with transparent background recommended)
5. Adjust box size and corner radius

---

## Requirements

- Python 3.8 or higher
- Dependencies (auto-installed): `qrcode[pil]`

---

## Notes

- The `output/` folder is created automatically if missing.
- Generated QR codes are excluded from Git via `.gitignore`.
- Always test your QR code on multiple devices after embedding a large logo.

---

## License

Open source. Free to use, modify, and distribute.


---

## Contact & Connect

Feel free to reach out!


<a href="mailto:nabothtieng@gmail.com">
  <img src="https://www.svgrepo.com/show/452213/gmail.svg" width="68" height="68" alt="Email"/>
</a>
&nbsp;
<a href="https://www.linkedin.com/in/naboth-tieng-113aa1243">
  <img src="https://www.svgrepo.com/show/452051/linkedin.svg" width="68" height="68" alt="LinkedIn"/>
</a>

---

*Made with ❤️ using QRForge*

