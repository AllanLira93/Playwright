from playwright.sync_api import Playwright, sync_playwright
from home_page import HomePage
from search_item import SearchPage
from add_cart import AddCartPage
from check_out import CheckOut

class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "input[name='username']"
        self.password = "input[name='password']"

        self.submit_button = "button[type='submit']"

    def login(self, username, password):

        self.page.fill(self.username, username)
        self.page.fill(self.password, password)

        self.page.click(self.submit_button)


def run(playwright: Playwright):

    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    page.wait_for_load_state("networkidle")

    login_page = LoginPage(page)

    login_page.login(
        "Admin",
        "admin123"
    )

    page.wait_for_timeout(5000)



    page2 = context.new_page()

    page2.goto("https://sauce-demo.myshopify.com/search?type=product&q=")

    page2.wait_for_load_state("networkidle")

    search_item = SearchPage(page2)
    search_item.search(
        "notebook"
    )

    search_item = SearchPage(page2)
    search_item.search(
        "shirt"
    )

    cart_page2 = AddCartPage(page2)
    cart_page2.open_item()
    cart_page2.add_product_cart()

    check_out_page2 = CheckOut(page2)
    check_out_page2.open_my_cart()
    check_out_page2.check_out()

    home_page = HomePage(page2)
    home_page.home()


    page.wait_for_timeout(5000)

    browser.close()


with sync_playwright() as playwright:
    run(playwright)