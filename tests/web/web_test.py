import pytest
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.calculator_page import CalculatorPage
from tests.web.pages.RegisterPage import RegisterPage


class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).login('admin', 'test1234')
        assert CalculatorPage(self.driver).elements.username.text == 'admin'
        # CalculatorPage(self.driver).elements.logout_button.click()

    def test_register(self):
        LoginPage(self.driver).elements.register.click()

        RegisterPage(self.driver).register1('hello7', '1234', '1234')
        print(CalculatorPage(self.driver).elements.username.text)
        # RegisterPage(self.driver).element.register.click()
        assert CalculatorPage(self.driver).elements.username.text == 'hello7'

       # CalculatorPage(self.driver).elements.logout_button.click()

    def test_add(self):
        LoginPage(self.driver).login('admin', 'test1234')

        CalculatorPage(self.driver).elements.key_1.click()
        CalculatorPage(self.driver).elements.key_add.click()
        CalculatorPage(self.driver).elements.key_2.click()
        CalculatorPage(self.driver).elements.key_equals.click()

        assert CalculatorPage(self.driver).elements.screen.value == '3'

    def test_subtract(self):
        LoginPage(self.driver).login('admin', 'test1234')
        CalculatorPage(self.driver).elements.key_7.click()
        CalculatorPage(self.driver).elements.key_subtract.click()
        CalculatorPage(self.driver).elements.key_2.click()
        CalculatorPage(self.driver).elements.key_equals.click()

        assert CalculatorPage(self.driver).elements.screen.value == '5'
        # testing a clear  button
        CalculatorPage(self.driver).elements.key_clear.click()
        assert CalculatorPage(self.driver).elements.screen.value == ''

    def test_history(self):
        LoginPage(self.driver).login('admin', 'test1234')

        CalculatorPage(self.driver).elements.key_4.click()
        CalculatorPage(self.driver).elements.key_add.click()
        CalculatorPage(self.driver).elements.key_3.click()
        CalculatorPage(self.driver).elements.key_equals.click()

        assert CalculatorPage(self.driver).elements.screen.value == '7'

        CalculatorPage(self.driver).elements.toggle_button.click()

        assert CalculatorPage(self.driver).elements.history.value == '4+3=7\n'

        CalculatorPage(self.driver).elements.clear_history.click()
        assert CalculatorPage(self.driver).elements.history.value == ''
        CalculatorPage(self.driver).elements.toggle_button.click()
        CalculatorPage(self.driver).elements.logout_button.click()
       # LoginPage(self.driver).elements.username.set('a')

       # LoginPage(self.driver).elements.password.set('1234')
       # LoginPage(self.driver).elements.login.click()

 # docker run --name selenium -d --add-host host.docker.internal:host-gateway -p 4444:4444 -p 5900:5900 --shm-size="2g" selenium/standalone-chrome:4.2.1-20220531
