from code_gen import Codes


inventory = {}

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.revenue = price  * quantity
        self.code = Codes.generate_code()
    
    @staticmethod
    def add_section():
        section_name = input("Enter section name: ").lower()
        if section_name not in inventory:
            inventory[section_name] = []
        else:
            print("Section already exists")
    
    @staticmethod
    def add_product():
        name = str(input("Enter product name: ")).lower()
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        section = input("In which section: ").lower()
        resulting_product = Product(name, price, quantity)
        if section not in inventory:
            confirm = input("Section does not exist, want to create a new one ? (yes/no): ").lower()
            while True:
                if confirm == "yes":
                    Product.add_section()
                    break
                elif confirm == "no":
                    print("Invalid section or does not exist, try again...")
                    break
        else:
            inventory[section].append(resulting_product)

    
    @staticmethod
    def display_section():
        section_name = input("Enter section name: ").lower()
        if section_name not in inventory:
            print("Section not found")
        else:
            print(f"Products in {section_name.capitalize()}:")
            for i in inventory[section_name]:
                print(f"Name: {i.name.capitalize()}, Price: ${i.price}, Quantity: {i.quantity}, Revenue: ${i.revenue}, Code: {i.code}")

    @staticmethod
    def display_inventory():
        sections = list(inventory.keys())
        print(f"Sections are {sections}")
        
        




Product.add_section()
Product.add_product()
Product.display_section()
Product.display_inventory()
   
    
    
        




