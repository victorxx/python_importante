from playwright.sync_api import sync_playwright,Playwright


def run(play:Playwright):
    iphone = play.devices["iPhone 14"]
    browser=play.webkit.launch(headless=False)
    contexto=browser.new_context(**iphone)
    page=contexto.new_page()
    page.goto("https://www.google.com")

    page.wait_for_load_state("networkidle")

    input("pressione enter para fechar")

    browser.close()


with sync_playwright() as play:
   run(play)
