from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://test.kelasotomesyen.com/login')

    # login
    page.get_by_test_id('login-email-input').fill('uno.testing3@gmail.com')
    page.get_by_test_id('login-password-input').fill('1234567890')
    page.get_by_test_id('login-submit-button').click()

    # data produk
    products = [
        {"name": "beli kelas 1", "price": "10000", "stock": "1", "category": "Toys"},
        {"name": "beli kelas 2", "price": "10000", "stock": "1", "category": "Home"},
        {"name": "beli kelas 3", "price": "10000", "stock": "1", "category": "Clothing"},
    ]

    # looping add produk
    for product in products:

        page.get_by_test_id('add-product-button-header').click()

        page.get_by_test_id('product-name-input').fill(product["name"])
        page.get_by_test_id('product-price-input').fill(product["price"])
        page.get_by_test_id('product-stock-input').fill(product["stock"])
        page.get_by_test_id('product-category-input').select_option(value=product["category"])
        page.get_by_test_id('product-description-input').fill('belajar bareng')

        page.get_by_test_id('submit-button').click()

    # tunggu sebentar supaya terlihat
    page.wait_for_timeout(3000)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)