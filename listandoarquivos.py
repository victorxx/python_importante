import os

pasta = os.path.dirname(os.path.abspath(__file__))

arquivos = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith(".py")]
for arquivo in arquivos:
    print(arquivo)
