from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto('https://www.espiritosanto-es.com.br/')
    page.wait_for_load_state('load')
    
    links = page.locator('a[href]')
    total = links.count()
    
    urls = []

    for i in range(total):
        href = links.nth(i).get_attribute('href')
        
        if href:
            if href.startswith('http'):
                urls.append(href)
            else:
                urls.append("https://www.espiritosanto-es.com.br" + href)

    for url in urls:
        print(url)

    browser.close()
