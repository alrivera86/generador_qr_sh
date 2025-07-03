import qrcode
import zipfile
import os

# Crear una carpeta para los QR generados
output_folder = "qr_output"
os.makedirs(output_folder, exist_ok=True)

# Abrir el archivo de URLs y leer las líneas
with open("urls.txt", "r") as file:
    urls = file.readlines()

# Quitar espacios en blanco y saltos de línea
urls = [url.strip() for url in urls]

# Crear un código QR para cada URL y guardar con nombres identificables
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
    qr_filename = f"qr_{i}_{url.replace('https://', '').replace('/', '_')}.png"
    qr_path = os.path.join(output_folder, qr_filename)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)
    print(f"QR {i} generado: {qr_filename}")

# Crear un archivo ZIP que contenga todos los QR generados
zip_filename = "qr_codes.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files in os.walk(output_folder):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print(f"Archivo ZIP generado: {zip_filename}")

