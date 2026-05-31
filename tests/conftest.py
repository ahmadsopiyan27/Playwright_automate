from playwright.sync_api import sync_playwright
import pytest
import allure
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("TEST_USERNAME")
password = os.getenv("TEST_PASSWORD")


@pytest.fixture(scope='function')
def setup():
    playwright = sync_playwright().start()

    with allure.step('Open browser'):
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        page = context.new_page()

    with allure.step('Open SauceDemo'):
        page.goto(os.getenv("URL"))

    yield page

    with allure.step('Close browser'):
        context.close()
        browser.close()
        playwright.stop()