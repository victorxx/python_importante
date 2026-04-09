import os
import json
import time
import random
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    contexto=browser.new_context(
        viewport={'width':250,'height':250}
    )
    page=contexto.new_page()
    try:
        page.goto('https://www.youtube.com/watch?v=Fk8IfLvx7g0')
        page.wait_for_load_state('load')
        input('pressione enter pra fechar')
    except Exception as e:
        print(f'erro')
    finally:
        browser.close()
