import os

Inicio = os.path.dirname(os.path.abspath(__file__))
base = os.path.basename(__file__)

arquivo = [
    arquivo
    for arquivo in os.listdir(Inicio)
    if arquivo.endswith(".py") and arquivo != base
]
for arquivos in arquivo:
    caminho = os.path.join(Inicio, arquivos)
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
    if " WhatsApp: +55 27 99949-7001" in conteudo:
        print(f"nome do arquivo"+caminho)
        print("ok")
