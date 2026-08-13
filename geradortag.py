import unicodedata
from playwright.sync_api import sync_playwright
import time
import random

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.espiritosanto-es.com.br/")
    page.wait_for_load_state("load")

    for x in range(2):
        page.mouse.wheel(0, 1000)
        time.sleep(2)

    buscar = page.locator("a")
    quantidade = buscar.count()

    if quantidade > 0:
        print("ok")

        buscar.nth(random.randrange(quantidade)).click()
        time.sleep(3)

        buscar = page.locator("h2").inner_text()

        # Remove os acentos
        texto = unicodedata.normalize("NFD", buscar)
        texto = texto.encode("ascii", "ignore").decode("utf-8")

        # Pega os 10 primeiros caracteres
        minimizar = texto[:10]

        # Cria a tag
        remover = "#" + minimizar.strip()

        print(remover)
        print("sua tag ai")

        input("pressione por favor")

    browser.close()
