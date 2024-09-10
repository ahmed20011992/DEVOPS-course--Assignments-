# content of test_sample.py
from BE.calculator_helper import CalculatorHelper


class TestC():
    def test_first(self):
        calculator = CalculatorHelper()
        result = calculator.add(6, 2)  # Pass 6 and 2 directly to the method

        assert result == 8, "expected value is 8"

        result = calculator.divide(4, 2)

        assert result == 2, " expexted value is 2"

    # def test_setup_module(self):

    #     self.calculator = CalculatorHelper()

    #     assert isinstance(self.calculator, CalculatorHelper)

    # def test_Teardown_module(module):
    #     print("\nTeardown module")
    #     # del module.calculator # python delete direct after i am out of function so if i add this i will have no passed test
