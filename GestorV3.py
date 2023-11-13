import random

class Codes:
    def __init__(self):
        self.codes_generated = []
    def generate_code(self):
        while True:
            self.result_code = random.randint(10000000000, 99999999999)
            if self.result_code not in self.codes_generated:
                break

class Product:
    def __init__(self):
        try:
            self.name = str(input("Enter product name: "))
            if self.name == "":
                print("Product name cannot be empty --You can use spaces though--")
        except Exception as e:
            print(e)
        try:
            self.price = float(input("Enter product price: "))
        except ValueError:
            print("Oops ! there appears to be a value error, try again...")
        except Exception as e:
            e = "Oops ! there appears to be an error, try again..."
            print(e)
        try:
            self.quantity = float(input("Enter product quantity: "))
        except ValueError:
            print("Oops ! there appears to be a value error, try again...")
        except Exception as e:
            e = "Oops ! there appears to be an error, try again..."
            print(e)
        try:
            self.revenue = self.price * self.quantity
        except Exception as e:
            e = "Oops ! there appears to be an error, try again..."
            print(e)
            

class Gestor:
    def __init__(self):
        self.inventario = {}
    
    def section_add(self):
        self.section = input("Enter section name: ")
        if self.section not in self.inventario:
            self.inventario[self.seccion] = []
        else:
            print("Section already exists")

    def product_add(self):
        self.section = input("In which section: ")
        if self.section not in self.inventario:
            print("Section does not exist")
        else:
            result = Product()
            self.inventario[self.section].append(result)

Gestor.section_add()
Gestor.product_add()