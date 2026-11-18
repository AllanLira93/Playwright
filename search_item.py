class SearchPage:
    def __init__(self, page2):
        self.page2 = page2

        self.search_item = page2.get_by_role("textbox", name="Search")

    def open(self):
        self.page2.goto("https://sauce-demo.myshopify.com/search?type=product&q=")

    def search(self, search_item):
        self.search_item.fill(search_item)
        self.search_item.press("Enter")


