import operator

class Calculator:
    def __init__(self):
        # Define supported operations
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '**': operator.pow
        }

    def calculate(self, num1, op, num2):
        # Check for division or modulo by zero
        if op in ('/', '%') and num2 == 0:
            raise ValueError("Error! Division or modulo by zero is not allowed.")
        return self.operations[op](num1, num2)

    def run(self):
        print("Simple Python Calculator")
        print("Available operations: +, -, *, /, %, **")

        while True:
            try:
                num1 = input("Enter first number: ").strip()
                if not num1:
                    print("No input provided. Please enter a number.\n")
                    continue
                num1 = float(num1)

                op = input("Enter operation: ").strip()
                if op not in self.operations:
                    print("Invalid operation. Try again.\n")
                    continue

                num2 = input("Enter second number: ").strip()
                if not num2:
                    print("No input provided. Please enter a number.\n")
                    continue
                num2 = float(num2)

                # Perform calculation
                result = self.calculate(num1, op, num2)
                print(f"Result: {num1} {op} {num2} = {result}\n")

            except ValueError as e:
                print(f"Invalid input. {e}\n")

            cont = input("Do you want to continue? (yes/no): ").strip().lower()
            if cont not in ('yes', 'y'):
                print("Calculator exiting. Goodbye!")
                break

if __name__ == "__main__":
    # Create Calculator instance and run it
    calc = Calculator()
    calc.run()
