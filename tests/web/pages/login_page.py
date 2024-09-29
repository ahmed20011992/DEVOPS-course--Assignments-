from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class LoginPage(PageBase):
    def __init__(self, driver):
        # Initialize the base class
        PageBase.__init__(self, driver=driver)

        # Define the page elements
        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password"]', self),
            'login': Element('//button[@id="login"]', self),
            'register': Element('//button[@id="register"]', self)
        }

        # Munchify the page_elements and assign it to self.elements
        self.elements = munchify(self.page_elements)

    def login(self, username, password):
        self.elements.username.set(username)
        self.elements.password.set(password)
        self.elements.login.click()
