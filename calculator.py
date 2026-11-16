class Calculator:
    def __init__(self, op1: float, op2: float):
        if not isinstance(op1, (int, float)):
            raise TypeError("First operand must be a number")

        if not isinstance(op2, (int, float)):
            raise TypeError("Second operand must be a number")

        self.__op1 = op1
        self.__op2 = op2

    def sum(self):
        return self.__op1 + self.__op2

    def subtract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def divide(self):
        if self.__op2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.__op1 / self.__op2


if __name__ == "__main__":
    calc = Calculator(10, 2)
    print(f"10 + 2 = {calc.sum()}")
    print(f"10 - 2 = {calc.subtract()}")
    print(f"10 * 2 = {calc.multiply()}")
    print(f"10 / 2 = {calc.divide()}")
    try:
        calc_zero = Calculator(10, 0)
        print(f"10 / 0 = {calc_zero.divide()}")
    except ZeroDivisionError as e:
        print(f"10 / 0 --> error: {e}")
    try:
        calc_input = Calculator("abc", 2)
    except TypeError as e:
        print(f"Calculator('abc', 2) --> error: {e}")