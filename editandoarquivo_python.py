from pathlib import Path

antigo = 'buscar = page.get_by_text("Quero meter", exact=True)'
novo = 'buscar = page.get_by_text("Quero meter2", exact=True)'

pasta = Path(__file__).parent  # Pasta onde este script está

editados = 0

for arquivo in pasta.rglob("*.py"):
    # Não edita o próprio script
    if arquivo.resolve() == Path(__file__).resolve():
        continue

    try:
        conteudo = arquivo.read_text(encoding="utf-8")

        if "Comentar" in conteudo:
            print(f"\nEncontrado em: {arquivo}")

        if antigo in conteudo:
            conteudo = conteudo.replace(antigo, novo)
            arquivo.write_text(conteudo, encoding="utf-8")
            print(f"✅ Editado: {arquivo}")
            editados += 1

    except Exception as e:
        print(f"❌ Erro em {arquivo}: {e}")

print(f"\nConcluído! {editados} arquivo(s) editado(s).")
