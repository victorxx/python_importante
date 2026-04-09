from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    
    page=browser.new_page()
    page.set_viewport_size({"width":330,"height":250})
    page.goto('https://www.youtube.com/watch?v=ucYS8LM3oUo')
    page.wait_for_load_state('load')
    input('pressione para fechar')
    browser.close()
    
    
