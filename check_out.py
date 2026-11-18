class CheckOut:
    def __init__(self,page2):

        self.page2 = page2
        self.my_cart =  page2.get_by_role("link", name="My Cart (1)")
        self.checkout_cart = page2.get_by_role("link", name="Check Out")
        self.checkout_cart_button = page2.get_by_role("button", name="Check Out")

    def open_my_cart(self):
        self.my_cart.click()

    def check_out(self):
        self.checkout_cart.click()
        self.checkout_cart_button.click()



