import qrcode

# Abrir el archivo de URLs y leer las líneas
with open("urls.txt", "r") as file:
    urls = file.readlines()

# Quitar espacios en blanco y saltos de línea
urls = [url.strip() for url in urls]

# Crear un código QR para cada URL
for i, url in enumerate(urls, start=1):
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear la imagen y guardarla
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr_{i}.png")
    print(f"QR {i} generado para: {url}")

print("Todos los códigos QR han sido generados.")
