from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in (p.chromium, p.firefox, p.webkit):

        print(f" running on {browser_type.name.capitalize()}")

        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://kelasotomesyen.com/')

        print(f"Title: {page.title()}")

        browser.close()