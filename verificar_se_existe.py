import easyocr
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


produtos = ["sonho de valsa", "chocolate garoto", "bis", "oreo","garoto","garotg"]

arquivo = r"C:\Users\xxvitaoxx\Downloads\images.jpg"

ler = easyocr.Reader(["pt"])

resultado = ler.readtext(arquivo)

for item in resultado:
    texto = item[1].lower()
    print("Texto:", texto)

    for produto in produtos:
        if produto in texto:
            print("Produto existe sim:", produto)
