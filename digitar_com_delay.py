from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("http://localhost/teste/index.php")

    page.wait_for_load_state()

    page.type("input", "teste", delay=200)

    time.sleep(10)

    input("pressione para fechar")

    browser.close()
