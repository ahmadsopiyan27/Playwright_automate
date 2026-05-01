from playwright.sync_api import sync_playwright, expect
import pytest
import allure


@pytest.fixture(scope='function')
def setup():
    with sync_playwright() as p:
        with allure.step('Open browser'):
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(viewport={'width': 1280, 'height': 720})

        with allure.step('Open SauceDemo'):
            page.goto('https://www.saucedemo.com/')
        
        yield page
        browser.close()