class Calculator:
    def __init__(self, op1: float, op2: float):
        if not isinstance(op1, (int, float)):
            raise TypeError("First operand must be a number")

        if not isinstance(op2, (int, float)):
            raise TypeError("Second operand must be a number")

        self.__op1 = op1
        self.__op2 = op2

    def add(self):
        return self.__op1 + self.__op2

    def subtract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def divide(self):
        if self.__op2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.__op1 / self.__op2