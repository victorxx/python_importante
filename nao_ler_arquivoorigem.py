from pathlib import Path

pasta = Path(__file__).parent

origem=Path(__file__).resolve()
for arquivo in pasta.glob("*.py"):
    conteudo = arquivo.read_text(encoding="utf-8")
    if arquivo.resolve()==origem:
        continue
    print(f"\n=== {arquivo.name} ===")
    print(conteudo)
