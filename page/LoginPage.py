from locator.Locator import Locator
from page.Page import Page


class LoginPage(Page):

    emailField = Locator("ID", "email")
    passField = Locator("ID", "pass")
    loginButton = Locator("CSS", "#loginbutton input")

    login_page = Locator("CSS", ".loggedout_menubar")

    def login(self, user, password):
        self.get_element(self.emailField).send_keys(user)
        self.get_element(self.passField).send_keys(password)
        self.get_element(self.loginButton).click()

    def is_it_login_page(self):
        return self.exists(self.login_page)
