from playwright.sync_api import sync_playwright
import time

textos = []

def inicio():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://localhost/ok/')
        
        page.wait_for_load_state('load')
        
        buscar = page.locator("#ok")
        
        try:
            if buscar.is_visible(timeout=5000):  
                texto = buscar.inner_text()
                textos.append(texto)
                print(f"Texto capturado: {texto}")
            else:
                print('Elemento não encontrado dentro do tempo.')
        except Exception as e:
            print(f'Elemento não apareceu. Erro: {e}')
            
        browser.close()

# LOOP PRINCIPAL
while True:
    inicio()
    
    # CORREÇÃO AQUI: Usamos len() para saber o tamanho (quantidade de itens) da lista
    if len(textos) == 2:
        print('ok - Mais de 1 texto foi coletado!')
        val=int(textos[0])
        val2=int(textos[1])

        if val>val2:
            print('ok o primeiro valor é maior')
        else:
            print('ok segundo valor é maior')
        
        break  # Opcional: break interrompe o loop quando a condição for atingida
    
    # DICA: Um pequeno sleep evita que seu script trave o processador abrindo navegadores sem parar
    time.sleep(2)
