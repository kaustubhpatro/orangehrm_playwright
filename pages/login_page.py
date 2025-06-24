from playwright.sync_api import Page


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("xpath=//input[@name='username']")
        self.password = page.locator("xpath=//input[@name='password']")
        self.submit = page.locator("xpath=//button[@type='submit']")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()
        self.page.wait_for_selector("xpath=//aside")
