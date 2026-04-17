import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw
import os
import re

def is_valid_hex_color(color: str) -> bool:
    pattern = re.compile(r'^#[0-9a-fA-F]{3}$|^#[0-9a-fA-F]{6}$')
    return bool(pattern.match(color.strip()))

def draw_rounded_rectangle(draw, xy, radius, fill):
    x1, y1, x2, y2 = xy
    draw.pieslice((x1, y1, x1 + radius*2, y1 + radius*2), 180, 270, fill=fill)
    draw.pieslice((x2 - radius*2, y1, x2, y1 + radius*2), 270, 360, fill=fill)
    draw.pieslice((x1, y2 - radius*2, x1 + radius*2, y2), 90, 180, fill=fill)
    draw.pieslice((x2 - radius*2, y2 - radius*2, x2, y2), 0, 90, fill=fill)
    draw.rectangle((x1 + radius, y1, x2 - radius, y2), fill=fill)
    draw.rectangle((x1, y1 + radius, x2, y2 - radius), fill=fill)


def get_valid_int(prompt: str, default: int, min_val: int, max_val: int) -> int:
    """Helper to get integer input with limits."""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return default
        try:
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"   ⚠️  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("   ⚠️  Please enter a valid number.")


def get_valid_float(prompt: str, default: float, min_val: float, max_val: float) -> float:
    """Helper to get float input with limits."""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return default
        try:
            value = float(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"   ⚠️  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("   ⚠️  Please enter a valid number.")


def generate_qrforge(
    data: str,
    filename: str = "qrforge_output.png",
    fill_color: str = "#000000",
    back_color: str = "#FFFFFF",
    logo_path: str = None,
    logo_size_ratio: float = 0.28,
    box_size: int = 12,
    corner_radius: int = 18,
    border: int = 4,
    version: int = None,
    error_correction: int = ERROR_CORRECT_H,
    output_dir: str = "output"
):
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)

    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        qr_width, qr_height = img.size
        
        safe_area_size = int(min(qr_width, qr_height) * logo_size_ratio)
        
        # Preserve aspect ratio
        logo_ratio = logo.width / logo.height
        if logo_ratio > 1:
            new_width = safe_area_size
            new_height = int(safe_area_size / logo_ratio)
        else:
            new_height = safe_area_size
            new_width = int(safe_area_size * logo_ratio)
        
        logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Rounded background
        padding = 12
        bg_size = safe_area_size + padding * 2
        bg_x = (qr_width - bg_size) // 2
        bg_y = (qr_height - bg_size) // 2
        
        draw = ImageDraw.Draw(img)
        draw_rounded_rectangle(
            draw,
            (bg_x, bg_y, bg_x + bg_size, bg_y + bg_size),
            corner_radius,
            fill=back_color
        )
        
        logo_x = (qr_width - new_width) // 2
        logo_y = (qr_height - new_height) // 2
        img.paste(logo, (logo_x, logo_y), logo)

    img.save(full_path, "PNG")
    print(f"✅ QRForge created successfully: {full_path}")
    return full_path


def get_unique_filename(base_name: str, output_dir: str = "output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    if not base_name.lower().endswith('.png'):
        base_name += '.png'
    full_path = os.path.join(output_dir, base_name)
    if not os.path.exists(full_path):
        return base_name
    
    print(f"⚠️  '{base_name}' already exists.")
    while True:
        choice = input("   Overwrite? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return base_name
        elif choice in ['n', 'no']:
            name, ext = os.path.splitext(base_name)
            counter = 1
            while True:
                new_name = f"{name}_{counter}{ext}"
                if not os.path.exists(os.path.join(output_dir, new_name)):
                    print(f"   → Using: {new_name}")
                    return new_name
                counter += 1
        else:
            print("   Please type 'y' or 'n'.")


# ==================== INTERACTIVE MODE ====================
if __name__ == "__main__":
    print("🚀 Welcome to QRForge\n")

    data = input("Enter data/URL/text: ").strip() or "https://example.com"
    base_filename = input("Filename (e.g. avane_qr): ").strip() or "qrforge_output"
    resolved_filename = get_unique_filename(base_filename)

    print("\nColors (use hex like #1E40AF):")
    while True:
        fill_color = input("Foreground color [#4A2C7A]: ").strip() or "#4A2C7A"
        if is_valid_hex_color(fill_color): break
        print("   Invalid hex format.")

    while True:
        back_color = input("Background color [#F5F0E8]: ").strip() or "#F5F0E8"
        if is_valid_hex_color(back_color): break
        print("   Invalid hex format.")

    # Logo
    logo_path = None
    logo_size_ratio = 0.28
    if input("\nAdd logo? (y/n): ").strip().lower() in ['y', 'yes']:
        print("   💡 Tip: PNG with transparent background works best.")
        while True:
            logo_input = input("   Logo full path: ").strip()
            if logo_input and os.path.exists(logo_input):
                logo_path = logo_input
                break
            print("   File not found.")
            if input("   Try again? (y/n): ").strip().lower() not in ['y', 'yes']:
                break
        if logo_path:
            logo_size_ratio = get_valid_float(
                "   Logo size ratio [0.28] (0.15–0.40 allowed): ",
                0.28, 0.15, 0.40
            )

    # Box Size with limits
    print("\nBox size = pixels per QR module")
    box_size = get_valid_int(
        "   Box size [12] (5–40 allowed, 8–20 recommended): ",
        12, 5, 40
    )

    # Corner Radius with limits
    print("\nCorner radius for the logo background")
    corner_radius = get_valid_int(
        "   Corner radius [18] (0–60 allowed, 8–30 recommended): ",
        18, 0, 60
    )

    generate_qrforge(
        data=data,
        filename=resolved_filename,
        fill_color=fill_color,
        back_color=back_color,
        logo_path=logo_path,
        logo_size_ratio=logo_size_ratio,
        box_size=box_size,
        corner_radius=corner_radius
    )

    print("\n🎉 Done! All values were validated.")