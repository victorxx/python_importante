from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    contexto=browser.new_context(
     geolocation={"latitude": -20.3297, "longitude": -40.2925}
    )
    page=contexto.new_page()
    page.goto('https://www.google.com/maps')
    input('pressione para fechar')
    browser.close()
    
