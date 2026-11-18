class AddCartPage:
    def __init__(self,page2):

        self.page2 = page2

        self.select_item = page2.get_by_role("link", name="Striped top Striped top £")
        self.add_cart = page2.get_by_role("button", name="Add to Cart")

    def open_item(self):
        self.select_item.click()

    def add_product_cart(self):
        self.add_cart.click()
