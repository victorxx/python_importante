import os
from pathlib import Path


def comecar_com_os():
    pasta = os.path.dirname(__file__)

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".py"):
            caminho = os.path.join(pasta, arquivo)
            print("listando com os")
            print(caminho)


def com_path():
    pasta = Path(__file__).parent

    for arquivo in pasta.glob("*.py"):
        print("listando com path")
        print(arquivo)


com_path()
