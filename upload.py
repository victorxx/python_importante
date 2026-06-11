import time
from playwright.sync_api import sync_playwright


def inicio():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('http://localhost/ok/')
        page.wait_for_load_state('load')
        botoes=page.get_by_role("button")
        if botoes.count()>0:
            quantidade=botoes.count()
            botao2=botoes.nth(0).set_input_files(r'C:\Users\vitor\Desktop\bots\bots.rar')
            print('enviado')
        input('pressione fechar')
        browser.close()
    

inicio()
