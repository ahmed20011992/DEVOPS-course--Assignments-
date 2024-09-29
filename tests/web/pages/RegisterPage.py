from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class RegisterPage(PageBase):
    def __init__(self, driver):  # Correct the method name to __init__
        PageBase.__init__(self, driver=driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password1"]', self),
            'password_again': Element('//input[@id="password2"]', self),
            'register': Element('//button[@id="register"]', self),
        }

        self.elements = munchify(self.page_elements)

    def register1(self, username, password1, password2):
        self.elements.username.set(username)
        self.elements.password.set(password1)
        self.elements.password_again.set(password2)
        self.elements.register.click()
