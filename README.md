# QR Code Generator

A simple Python command-line tool for generating QR code images from links.

## Requirements

- Python 3.8+
- `qrcode`
- `Pillow`

## Installation

```bash
python -m pip install "qrcode[pil]"
```

## Usage

```bash
python buat-qr.py
```

Follow the prompts:

```text
Enter the link to generate a QR code: github.com/bgzs89
Enter the image filename: github-profile
QR code saved at: D:\Push Github\github-profile.png
```

The tool automatically adds `https://` when the link does not include a protocol. The output image is saved in the current terminal folder.

## License

MIT
