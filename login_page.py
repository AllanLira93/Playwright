class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = "input[name= 'username']"
        self.password = "input[name= 'password']"
        self.submit_button = "button[type='submit']"

    def open(self):
            self.page.goto("https://opensource-demo.orangehr.com/")

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.submit_button)




