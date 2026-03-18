import pytesseract
from PIL import Image

# Caminho do executável do Tesseract no Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrir a imagem
imagem = Image.open(r'C:\Users\vitor\Desktop\images.jpg')

# Extrair texto
texto = pytesseract.image_to_string(imagem, lang='por')

# Mostrar resultado
print(texto)
