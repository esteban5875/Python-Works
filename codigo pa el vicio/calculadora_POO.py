from math import sin, cos, tan, sqrt

class Sine:
    def __init__(self):
       self.result = 0
       try:
            self.value = float(input("Enter value to find sine: "))
       except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def find_sine(self):
        try:    
            self.result = sin(self.value)
            return round(self.result, 10)
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)

class Cosine:
    def __init__(self):
        self.result = 0
        try:
            self.value = float(input("Enter a value to find cosine: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def find_cosine(self):
        try:    
            self.result = cos(self.value)
            return round(self.result, 10)
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)

class Tan:
    def __init__(self):
        self.result = 0
        try:
            self.value = float(input("Enter a value to find tangent: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def find_tangent(self):
        try:
            self.result = tan(self.value)
            return round(self.result, 10)
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)

class Sum:
    def __init__(self):
        self.result = 0
        try:
            self.val1 = float(input("Enter first value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
        
        try:
            self.val2 = float(input("Enter second value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def add(self):
        try:
            self.result = float(round(self.val1 + self.val2, 10))
            return self.result
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)

class Diff:
    def __init__(self):
        self.result = 0
        try:
            self.val1 = float(input("Enter first value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
        
        try:
            self.val2 = float(input("Enter second value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def substract(self):
        try:
            self.result = float(round(self.val1 - self.val2))
            return self.result
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)
            
class Product:
    def __init__(self):
        self.result = 0
        try:
            self.val1 = float(input("Enter first value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
        
        try:
            self.val2 = float(input("Enter second value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def multiply(self):
        try:
            self.result = float(round(self.val1 * self.val2, 10))
            return self.result
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)

class Div:
    def __init__(self):
        self.result = 0
        try:
            self.val1 = float(input("Enter first value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
        
        try:
            self.val2 = float(input("Enter second value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def divide(self):
        try:
            self.result = float(round(self.val1 / self.val2, 10))
            return self.result
        except ZeroDivisionError as b:
            b = "Cannot divide by zero"
            print(b)
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)
    
class sqroot:
    def __init__(self):
        self.result = 0
        try:
            self.val = float(input("Enter value to find square root: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def sqr(self):
        try:
            self.result = sqrt(self.val)
            return round(self.result, 10)
        except Exception as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
            
class Exponent:
    def __init__(self):
        self.result = 0
        try:
            self.val1 = float(input("Enter base value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
        try:
            self.val2 = float(input("Enter exponent value: "))
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
    def expo(self):
        try:
            self.result = float(round(self.val1 ** self.val2, 10))
            return round(self.result, 10)
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)
        

class Math:    
    def add():
        find_sum = Sum()
        result = find_sum.add()
        print(f"\nResult is: {result}\n")
        
    def substract():
        find_diff = Diff()
        result = find_diff.substract()
        print(f"\nResult is: {result}\n")

    def multiply():
        find_product = Product()
        result = find_product.multiply()
        print(f"\nResult is: {result}\n")

    def divide():
        find_coefficient = Div()
        result = find_coefficient.divide()
        print(f"\nResult is: {result}\n")

    def pow():
        find_expo = Exponent()
        result = find_expo.expo()
        print(f"\nResult is: {result}\n")

    def sqroot():
        find_sqrt = sqroot()
        result = find_sqrt.sqr()
        print(f"\nResult is: {result}\n")

    def sine():
        find_sine = Sine()
        result = find_sine.find_sine()
        print(f"\nResult is: {result}\n")

    def cosine():
        find_cosine = Cosine()
        result = find_cosine.find_cosine()
        print(f"\nResult is: {result}\n")

    def tangent():
        find_tangent = Tangent()
        result = find_tangent.find_tangent()
        print(f"\nResult is: {result}\n")


while True:
    op = input("Enter operator: ").lower()
    if op not in ["+", "-", "/", "*", "sin", "cos", "tan", "sqroot", "expo", "bye"] or op.isspace():
        print("Enter a valid operator")
    elif op == "bye":
        break
    else:
        try:
            if op == "+":
                Math.add()
            elif op == "-":
                Math.substract()
            elif op == "*":
                Math.multiply()
            elif op == "/":
                Math.divide()
            elif op == "expo":
                Math.pow()
            elif op == "sqroot":
                Math.sqroot()
            elif op == "sin":
                Math.sine()
            elif op == "cos":
                Math.cosine()
            elif op == "tan":
                Math.tangent()
        except ValueError as e:
            e = "Oops ! There seems to be a value error, check your input and try again"
            print(e)
        except Exception as e:
            e = "There seems to be an error, check your inputs and try again"
            print(e)
