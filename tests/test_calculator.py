import pytest
from src.calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_sum(self):
        assert self.calc.sum(2, 3) == 5
        assert self.calc.sum(-1, 1) == 0
    
    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 10) == 0
    
    def test_multiply(self):
        assert self.calc.multiply(4, 5) == 20
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide(self):
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)