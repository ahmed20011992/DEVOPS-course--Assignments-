import pytest
from BE.calculator_helper import CalculatorHelper


class Base:
    def setup_method(self):
        self.calculator = CalculatorHelper()
        assert isinstance(self.calculator, CalculatorHelper)

    def teardown_method(self):
        print("\nTeardown method")
     #   del self.calculator


class TestCalculator(Base):

    # Testing the add method with multiple test cases
    @pytest.mark.parametrize("a, b, expected", [
        (3, 5, 8),
        (4, 1, 5),
        (-1, -1, -2),
        (0, 5, 5)
    ])
    def test_add(self, a, b, expected):
        result = self.calculator.add(a, b)
        assert result == expected, f"Expected {expected}, but got {result}"

    # Testing the subtract method with multiple test cases
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (10, 7, 3),
        (0, 1, -1),
        (-1, -1, 0)
    ])
    def test_subtract(self, a, b, expected):
        result = self.calculator.subtract(a, b)
        assert result == expected, f"Expected {expected}, but got {result}"

    # Testing the multiply method with multiple test cases
    @pytest.mark.parametrize("a, b, expected", [
        (3, 5, 15),
        (4, 0, 0),
        (-1, 1, -1),
        (2, -3, -6)
    ])
    def test_multiply(self, a, b, expected):
        result = self.calculator.multiply(a, b)
        assert result == expected, f"Expected {expected}, but got {result}"

    # Testing the divide method with multiple test cases
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (9, 3, 3),
        (-6, -2, 3),
        (5, 2, 2.5)
    ])
    def test_divide(self, a, b, expected):
        result = self.calculator.divide(a, b)
        assert result == expected, f"Expected {expected}, but got {result}"

    # Testing division by zero (should raise an error)
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(10, 0)
