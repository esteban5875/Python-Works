import math

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
            self.result = math.sin(self.value)
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
            self.result = math.cos(self.value)
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
            self.result = math.tan(self.value)
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
            self.result = math.sqrt(self.val)
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
        


