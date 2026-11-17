import pytest
from calculator import Calculator


def test_sum():
    calc = Calculator(5, 3)
    assert calc.sum() == 8


def test_subtract():
    calc = Calculator(5, 3)
    assert calc.subtract() == 2


def test_multiply():
    calc = Calculator(5, 3)
    assert calc.multiply() == 15


def test_divide():
    calc = Calculator(6, 3)
    assert calc.divide() == 2


def test_divide_by_zero():
    calc = Calculator(5, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()

def test_invalid_first_operand():
    with pytest.raises(TypeError):
        Calculator("abc", 5)


def test_invalid_second_operand():
    with pytest.raises(TypeError):
        Calculator(5, "abc")

def test_power():
    calc = Calculator(2, 3)
    assert calc.power() == 8


def test_power_zero_negative_exponent():
    calc = Calculator(0, -1)
    with pytest.raises(ZeroDivisionError): 
        calc.power()