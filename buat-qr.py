import qrcode
from pathlib import Path

link = input("Enter the link to generate a QR code: ").strip()

if not link:
    print("Error: Link cannot be empty.")
    raise SystemExit(1)

if not link.startswith(("http://", "https://")):
    link = "https://" + link

filename = input("Enter the image filename: ").strip()

if not filename:
    print("Error: Filename cannot be empty.")
    raise SystemExit(1)

if not filename.lower().endswith(".png"):
    filename += ".png"

output_path = Path.cwd() / filename
qrcode.make(link).save(output_path)
print(f"QR code saved at: {output_path}")
