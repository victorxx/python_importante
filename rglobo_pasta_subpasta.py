from pathlib import Path

contador = 0
pasta = Path(__file__).parent
for arquivo in pasta.rglob("*.py"):
    contador += 1
    print(contador)
print(f"total de arquivos{contador}")
