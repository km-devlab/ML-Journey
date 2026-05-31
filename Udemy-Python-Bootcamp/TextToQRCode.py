# Step 1: Install the library

# Open Command Prompt and run:

# pip install qrcode[pil]

import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)

filename = input("Enter file name: ")
img.save(f"{filename}.png")

# Open image automatically
img.show()

print("QR Code generated successfully!")

# Enter text or URL to generate QR Code: https://www.google.com
# Enter file name (without extension): google_qr

# QR Code saved successfully as google_qr.png
