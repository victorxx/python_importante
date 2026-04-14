import os
import json
import random
from playwright.sync_api import sync_playwright

def extrair(url_base, range_pagina):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        contexto = browser.new_context()
        page = contexto.new_page()
        
        # Sorteia a página
        num_random = random.randint(1, range_pagina)
        url_alvo = f"{url_base.rstrip('/')}/?pagina={num_random}"
        
        print(f'Acessando: {url_alvo}')
        page.goto(url_alvo)
        page.wait_for_load_state('load')
        
        dado = []
        link_locator = page.locator('a')
        contagem = link_locator.count()
        
        if contagem > 0:
            for x in range(contagem):
                href = link_locator.nth(x).get_attribute('href')
                if href:
                    if href.startswith('http'):
                        completo = href
                    else:
                        completo = f"{url_base.rstrip('/')}/{href.lstrip('/')}"
                    dado.append(completo)
        
        # Escolha aleatória dentro do bloco with para garantir que 'dado' exista
        if dado:
            escolhido = random.choice(dado)
            print(f"Escolhido: {escolhido}")
            browser.close()
            return escolhido
        
        browser.close()
        return None

def comecar():
    link = extrair("https://www.espiritosanto-es.com.br/", 3)
    return link

if __name__ == "__main__":
    comecar()
