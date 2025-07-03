from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
import subprocess

app = Flask(__name__)

OUTPUT_FOLDER = "qr_output"
ZIP_FILENAME = "qr_codes.zip"
URLS_FILE = "urls.txt"

@app.route("/")
def index():
    # Listar los QR generados
    qr_files = os.listdir(OUTPUT_FOLDER)
    return render_template("index.html", qr_files=qr_files, zip_filename=ZIP_FILENAME)

@app.route("/upload", methods=["POST"])
def upload_file():
    # Guardar el archivo subido como urls.txt
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(URLS_FILE)
    
    # Ejecutar el script generar_qr3.py
    subprocess.run(["python", "generar_qr3.py"], check=True)
    
    # Redirigir al índice para mostrar los nuevos QR
    return redirect(url_for('index'))

@app.route("/qr/<filename>")
def download_qr(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@app.route("/download_zip")
def download_zip():
    return send_from_directory(".", ZIP_FILENAME)

if __name__ == "__main__":
    app.run(debug=True)

