import qrcode
import zipfile
import os

# Crear carpeta de salida
output_folder = "qr_output"
os.makedirs(output_folder, exist_ok=True)

# Leer archivo tipo CSV separado por coma
with open("urls.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Generar QR para cada línea
for i, line in enumerate(lines, start=1):
    # Saltar líneas vacías
    if not line.strip():
        continue

    # Separar por punto y coma
    try:
        url, nombre_archivo = line.strip().split(",")
    except ValueError:
        print(f"Línea malformada (línea {i}): {line}")
        continue

    # Crear QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Guardar QR con nombre personalizado
    safe_filename = f"{nombre_archivo.strip().replace(' ', ' ')}.png"
    qr_path = os.path.join(output_folder, safe_filename)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)
    print(f"✅ QR generado: {safe_filename}")

# Comprimir todos los QR en un ZIP
zip_filename = "qr_codes.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files in os.walk(output_folder):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print(f"🎉 ZIP creado: {zip_filename}")

