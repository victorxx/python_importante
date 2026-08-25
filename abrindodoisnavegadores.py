from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser1 = p.chromium.launch(headless=False)

    browser2 = p.chromium.launch(headless=False)

    page1 = browser1.new_page()
    
    page2 = browser2.new_page()

    page1.goto("https://google.com")

    page2.goto("https://youtube.com")

    page1.wait_for_timeout(10000)

    browser1.close()
    browser2.close()
