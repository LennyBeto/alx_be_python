# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b

def main():
    # Perform calculations
    sum_result = Calculator.add(5, 3)
    print(f"Sum: {sum_result}")

    product_result = Calculator.multiply(4, 6)
    print(f"Product: {product_result}")

if __name__ == "__main__":
    main()
#main.py
from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
