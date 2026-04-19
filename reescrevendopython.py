from playwright.sync_api import sync_playwright
import time
import random


def pegar_noticia():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://eshoje.com.br/')
        page.wait_for_load_state('load')

        links = page.locator('a')
        lista_links = []

        for i in range(links.count()):
            href = links.nth(i).get_attribute('href')
            if href and href.startswith('http'):
                lista_links.append(href)

        if not lista_links:
            print("Nenhum link encontrado.")
            browser.close()
            return None

        link_escolhido = random.choice(lista_links)
        print(f"Acessando: {link_escolhido}")

        page.goto(link_escolhido)
        page.wait_for_load_state('load')

        time.sleep(2)

        if page.get_by_text("Compartilhe").count() > 0:
            print("Estamos na página de notícia")

            titulo = page.title()
            paragrafos = page.locator('p')
            if paragrafos.count()>0:
                primeiro=paragrafos.nth(0).inner_text()
                segundo=paragrafos.nth(1).inner_text()
            return titulo,primeiro,segundo

        else:
            print("Não é notícia")
            browser.close()
            return None


def reescrever():
    dado = pegar_noticia()

    if not dado:
        print("Nada retornado.")
        return

    primeiro,segundo,titulo = dado

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://quillbot.com/pt/reescrever-texto')
        page.wait_for_load_state('load')
        page.set_viewport_size({"width":660, "height": 440})

        time.sleep(5)
        texto=page.get_by_role('textbox')
        if texto.count()>0:
            print('ok')
            campo=texto.nth(0).click(force=True)
            print('clicado')
        time.sleep(20)
        texto=titulo+"\n\n"+"reescreva esse titulo"
        page.keyboard.type(texto,delay=100)
        print('escrito')
        time.sleep(10)
        botao = page.get_by_role("button", name="Reescrever").click()
        print('botao pressionado')
        time.sleep(50)

        browser.close()


# executar
reescrever()
