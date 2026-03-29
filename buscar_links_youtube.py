from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://www.youtube.com/@robsonvleite/videos', timeout=500000)

    # pega todos os <a>
    conteudo = page.locator('a')

    total = conteudo.count()

    for x in range(total):
        href = conteudo.nth(x).get_attribute('href')

        if href and 'watch?v=' in href:
            print('ok -> https://www.youtube.com' + href)
        else:
            print('nao ok')

    browser.close()
