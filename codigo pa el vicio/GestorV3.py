import random

class Codes:
    def __init__(self):
        self.codes_generated = set()
    @staticmethod
    def generate_code():
        while True:
            result_code = random.randint(10000000000, 99999999999)
            if result_code not in Codes.codes_generated:
                Codes.codes_generated.add(result_code)
                break

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.revenue = self.price  * self.quantity
        self.code = Codes.generate_code()
            
class Gestor:
    def __init__(self):
        self.inventory = {}
    
    def section_add(self):
        self.section = input("Enter section name: ").lower()
        if self.section.isspace():
            print("Section name cannot be empty")
        if self.section not in self.inventory:
            self.inventory[self.section] = []
        else:
            print("Section already exists")

    def product_add(self):
        self.section = input("In which section: ")
        if self.section not in self.inventory:
            print("Section does not exist")
        elif self.section.isspace():
            print("Section name cannot be empty")
        else:
            self.name = input("Enter product name: ")
            if self.name.isspace():
                print("Product name cannor be empty")
            else:
                while True:    
                    try:
                        self.price = float(input("Enter price --No currency sign--: "))
                        break
                    except ValueError:
                        print("Oops ! There seems to be a value error, try again...")
                    except Exception as e:
                        e = "There seems to be an error, try again"
                        print(e)
                while True:
                    try:
                        self.quantity = int(input("Enter product quantity: "))
                        break
                    except ValueError:
                        print("Oops ! There seems to be a value error, try again...")
                    except Exception as e:
                        e = "There seems to be an error, try again"
                        print(e)
            product = Product(self.name, self.price, self.quantity, self.revenue, Codes.self.code)
            self.inventory[self.section].append(product)
                    
    
    class Update:
        def update_name(self):
            pass


