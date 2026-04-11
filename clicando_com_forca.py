from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Lançar o navegador (headless=False para você ver a ação)
    browser = p.chromium.launch(headless=False)
    # Recomenda-se usar um viewport padrão para evitar que elementos sumam
    page = browser.new_page()
    
    # Acessar o vídeo no YouTube
    page.goto('https://www.youtube.com/watch?v=UjpvWTEbRbY')
    
    # Em vez de wait_for_load_state, vamos esperar o seletor específico aparecer
    # Isso é mais seguro para SPAs (Single Page Applications) como o YouTube
    try:
        # Localiza o botão pelo papel de acessibilidade e nome
        botao = page.get_by_role("button", name="Compartilhar")
        
        # Espera até 10 segundos para o botão estar visível
        botao.wait_for(state="visible", timeout=10000)
        
        # Clica no botão. O Playwright já tenta clicar no centro do elemento.
        # force=True ignora verificações de "clicabilidade" (útil se houver um overlay invisível)
        botao.click(force=True)
        
        print('Botão "Compartilhar" clicado com sucesso!')
        
        # Pausa para você ver o modal aberto antes de fechar
        input('Modal aberto. Pressione Enter para fechar o navegador...')
        
    except Exception as e:
        print(f'Erro ao tentar clicar no botão: {e}')
    
    # Fechar o navegador
    browser.close()
