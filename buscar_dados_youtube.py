from playwright.sync_api import sync_playwright
import time
import os

with sync_playwright() as p:
    dados=[]
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.youtube.com/@SBTNews/videos')
    page.wait_for_load_state('load')
    videos=page.locator('a[href*="/watch"]')
    for x in range(videos.count()):
        numero=videos.nth(x).get_attribute('href')
        if numero and "/watch" in numero:
            link_completo="https://www.youtube.com"+numero
            if link_completo not in dados:
                dados.append(link_completo)
for x in dados:
    print(x)
