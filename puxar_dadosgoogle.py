from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    page = browser.new_page()
    page.goto("https://www.google.com")

    # remover webdriver
    page.add_init_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    page.fill("textarea[name='q']", "playwright python")
    page.keyboard.press("Enter")

    page.wait_for_timeout(5000)

    print(page.title())

    browser.close()
