from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    contexto=browser.new_context()
    page=contexto.new_page()
    page.clock.install()
    page.clock.set_fixed_time("2026-01-01T10:00:00Z")
    page.goto("https://example.com")
    print(page.evaluate("new Date().toISOString()"))
    browser.close()
