from math import cos, sin, tan
class Math:
    def __init__(self):

        try:
            self.op = input("Enter Operator: ").lower()
        except ValueError:
            print("Value Error")
        self.val = None
        self.cos = None
        self.sin = None
        self.tan = None
        self.sum = None
        self.difference = None
        self.product = None
        self.coefficient = None
        self.num1 = 0
        self.num2 = 0
        
    

        if self.op not in ["+", "-", "/", "*", "sin", "cos", "tan", "bye"]:
            print("")
            print("Operator not valid")
            print("")
        elif self.op == "cos":
            try:
                self.val = float(input("Enter value to find cosine: "))
            except ValueError:
                print("Enter a valid input")
            self.cos = cos(self.val) 
        elif self.op == "tan":
            try:
                self.val = float(input("Enter value to find tangent: "))
            except ValueError as e:
                print(e)
            self.tan = tan(self.val)
        elif self.op == "sin":
            try:
                self.val = float(input("Enter a value to find sine: "))
            except ValueError as e:
                print(e)
            self.sin = sin(self.val)
        else:
            try:
                self.num1 = float(input("Enter 1st value: "))
            except ValueError as e:
                e = "Value Error"
                print(e)
            try:  
                self.num2 = float(input("Enter 2nd Value: "))
            except ValueError as e:
                e = "Value Error"
                print(e)  
              
    def add(self):
        self.sum = round(self.num1 + self.num2, 10)
        if self.sum == 0:
            pass
        else:
            return self.sum
    def substract(self):
        self.difference = round(self.num1 - self.num2, 10)
        if self.difference == 0:
            pass
        else:
            return self.difference
        return self.difference
    def divide(self):
        if self.num2 == 0:
            print("Cannot divide by zero")
        else:
            self.coefficient = round(self.num1 / self.num2, 10)
            if self.coefficient == 0:
                pass
            else:  
                return self.coefficient
    def multiply(self):
        self.product = round(self.num1 * self.num2, 10)
        if self.product == 0:
            pass
        else:
            return self.product
    
while True:
    math_calculator = Math()

    if math_calculator.op == "bye":
        break

    result = None

    if math_calculator.op in ["+", "-", "*", "/"]:
        result = math_calculator.add() if math_calculator.op == "+" else \
                 math_calculator.substract() if math_calculator.op == "-" else \
                 math_calculator.multiply() if math_calculator.op == "*" else \
                 math_calculator.divide()

        if result is not None:
            print("")
            print(f"Result: {result}")
            print("")

    elif math_calculator.op in ["sin", "cos", "tan"]:
        print(f"{math_calculator.op.upper()} of {math_calculator.val}: {getattr(math_calculator, math_calculator.op)}")