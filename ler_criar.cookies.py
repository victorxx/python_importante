import os
import json
from playwright.sync_api import sync_playwright

# 1. Localiza o arquivo que você criou antes
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
caminho_arquivo = os.path.join(desktop, 'link.json')

with sync_playwright() as p:
    # 2. Inicia o navegador
    browser = p.chromium.launch(headless=False)
    
    # 3. Cria o contexto (IMPORTANTE: o contexto deve estar vazio antes de carregar os cookies)
    context = browser.new_context()

    # 4. LÊ OS COOKIES DO ARQUIVO
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            cookies_salvos = json.load(f)
        
        # 5. INJETA OS COOKIES NO NAVEGADOR
        context.add_cookies(cookies_salvos)
        print("✅ Cookies carregados com sucesso!")
    else:
        print("❌ Erro: O arquivo link.json não foi encontrado no Desktop.")

    # 6. Abre a página (Se os cookies forem válidos, ele pula o login)
    page = context.new_page()
    page.goto('https://www.linkedin.com/feed/')

    # Mantém aberto para você ver o resultado
    input('Pressione Enter para fechar...')
    
    context.close()
    browser.close()


import os
import json
from playwright.sync_api import sync_playwright

# 1. Configura o caminho do arquivo no Desktop (Corrigido)
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
caminho_arquivo = os.path.join(desktop, 'link.json')

with sync_playwright() as p:
    # 2. Abre o navegador
    browser = p.chromium.launch(headless=False)
    
    # 3. Cria o contexto (essencial para capturar cookies)
    context = browser.new_context()
    page = context.new_page()

    # 4. Vai para a página de login
    page.goto('https://www.linkedin.com/login')

    print("\n--- AÇÃO NECESSÁRIA ---")
    print("1. Faça o login manualmente no navegador que abriu.")
    print("2. Quando estiver no seu Feed, volte aqui.")
    input("3. Pressione ENTER aqui no terminal para salvar os cookies...")

    # 5. Captura os cookies da sessão atual
    cookies = context.cookies()

    # 6. Salva no arquivo JSON
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(cookies, f, indent=4)

    print(f"\n✅ Arquivo criado em: {caminho_arquivo}")
    print(f"Total de cookies capturados: {len(cookies)}")

    # 7. Fecha tudo
    context.close()
    browser.close()
