class HomePage:
    def __init__(self, page2):
        self.page2 = page2
        self.home_page = page2.get_by_role("link", name="Sauce Demo Navigate to Online")

    def home(self):
        self.home_page.click()