!pip install ultralytics

from ultralytics import YOLO
from google.colab import files

# 1️⃣ Fazer upload da imagem
uploaded = files.upload()
img = list(uploaded.keys())[0]

# 2️⃣ Carregar o modelo YOLO
model = YOLO("yolov8n.pt")

# 3️⃣ Rodar detecção e salvar resultados (os resultados vêm como lista)
results = model(img)  # Isso vai retornar uma lista de resultados

# 4️⃣ Mostrar a imagem com as detecções (acessando o primeiro item da lista)
results[0].show()  # Agora funciona corretamente
