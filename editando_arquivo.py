import os

pasta = os.path.dirname(os.path.abspath(__file__))

arquivos = [
    arquivo for arquivo in os.listdir(pasta)
    if arquivo.endswith(".py")
]

for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()

    if "sorteio = random.randint(1, 10)" in conteudo:
        print(f"Alterando {arquivo}...")

        conteudo = conteudo.replace(
            "sorteio = random.randint(1, 10)",
            "sorteio = random.randint(1, 10)"
        )

        # Grava novamente no arquivo
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)

print("Concluído!")
