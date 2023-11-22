from Codes.Code_Utils import *
import os

inventory = {}

class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__code = Codes.generate_code()
        self._revenue = 0 

    @staticmethod
    def calculate_revenue(price, quantity):
        return price * quantity

    def update_revenue(self):
        self._revenue = self.calculate_revenue(self.price, self.quantity)    
    
    def add_section():
        section_name = str(input("\nEnter section name: ")).lower()
        if not section_name.isspace() and section_name not in inventory:
            inventory[section_name] = []
        elif section_name.isspace():
            print("\nEnter a section name\n")
        else:
            print("\nSection already exists\n")

    @staticmethod
    def add_product():
        name = str(input("\nEnter product name: ")).lower()
        product_duplicate = False
        for category, products in inventory.items():
            for existing_product in products:
                if existing_product == name:
                    product_duplicate = True
                
        if product_duplicate == True:
            print(f"\nDuplicate !!! {name.capitalize()} already found in {category}\n")
        else:
            try:
                for section, products in inventory.items():
                    for product in products:
                        if product.name == name:
                            print("\nProduct already exists!\n")
                            return  

                price = float(input("\nEnter product price: "))
                quantity = int(input("\nEnter product quantity: "))
                section = input("\nIn which section: ").lower()
                resulting_product = Product(name=name, price=price, quantity=quantity)

                if section not in inventory:
                    confirm = input("\nSection does not exist, want to create a new one? (yes/no): ").lower()
                    while True:
                        if confirm == "yes":
                            Product.add_section()
                            break
                        elif confirm == "no":
                            print("\nInvalid section or does not exist, try again...\n")
                            break
                else:
                    inventory[section].append(resulting_product)
                    
                resulting_product.update_revenue()

            except ValueError as e:
                e = "\nOops! There has been an error... Check your inputs and try again.\n"
                print(e)
    
    @staticmethod
    def display_section():
        section_name = input("\nEnter section name: ").lower()
        if section_name not in inventory or section_name.isspace():
            print("\nSection not found\n")
            
        else:
            number_of_product = len(inventory[section_name])
            if number_of_product == 0:
                print(f"\nNo products in {section_name.capitalize()}")
            else:
                for i in inventory[section_name]:
                    print(f"\nProducts in {section_name.capitalize()}:")
                    print(f"\nSection: {section_name.capitalize()}, Name: {i.name.capitalize()}, Price: ${i.price}, Quantity: {i.quantity}, Revenue: ${i._revenue}, Code: {i.__code}\n")
    

    @staticmethod
    def update_product_name():
        product_name = str(input("\nEnter product to update: ")).lower()
        found_product = False

        for category, products in inventory.items():
            for i in products:
                if i.name == product_name:
                    found_product = True
                    try:
                        new_name = str(input("\nEnter new name: ")).lower()
                        i.name = new_name
                        print(f"\nProduct: {product_name.capitalize()}...Updated in: {category.capitalize()}...Updated attribute: Name\n")
                    except Exception as e:
                        e = "\nOoops! There has been an error...Check your inputs and try again\n"
                        print(e)

        if found_product == False:
            print("Product not found")

    @staticmethod
    def update_product_quantity():
        product_name = input("\nEnter product to update: ")
        found_product = False
        for category, products in inventory.items():
            for product in products:
                if product.name == product_name:
                    found_product = True
                    try:
                        new_quantity = int(input("\nEnter new quantity: "))
                        product.quantity = new_quantity
                        product.update_revenue()
                        print(f"\nProduct: {product_name.capitalize()}...Updated in: {category.capitalize()}...Updated attribute: Quantity\n")
                    except Exception as e:
                        e = "\nOoops! There has been an error...Check your inputs and try again\n"
                        print(e)

        if found_product == False:
            print("Product not found")

    @staticmethod
    def update_product_price():
        product_name = input("\nEnter product to update: ").lower()
        found_product = False

        for category, products in inventory.items():
            for product in products:
                if product.name == product_name:
                    found_product = True
                    try:
                        new_price = float(input("\nEnter new price --No currency sign--: "))
                        product.price = new_price
                        product.update_revenue()
                        print(f"\nProduct: {product_name.capitalize()}...Updated in: {category.capitalize()}...Updated attribute: Price\n")
                    except Exception as e:
                        e = "\nOoops! There has been an error...Check your inputs and try again\n"
                        print(e)

        if found_product == False:
            print("\nProduct not found\n")
                
    
    def delete_section():
        section_name = input("\nEnter section name: ").lower()
        
        if section_name.isspace():
            print("\nEnter a section name!\n")
            
        else:
            keys_to_delete = []

            for i in inventory.keys():
                if section_name == i:
                    keys_to_delete.append(section_name)

            for key in keys_to_delete:
                inventory.pop(key, None)

            if not keys_to_delete:
                print("\nSection not found\n")
                
    @staticmethod
    def delete_product():
        product = input("\nWhich product: ").lower()
        if product.isspace():
            print("\nEnter a section name!\n")
            
        else:
            for category, products in inventory.items():
                for i in products:
                    if i.name == product:
                        inventory[category].remove(i)
                        print(f"\n{product.capitalize()} was deleted from {category}\n")
                        return
                    else:
                        print("\nProduct not found\n")
                

                    

    def display_inventory():
        section_num = 0
        num_of_sections = len(inventory)
        if num_of_sections == 0:
            print("\nNo products in inventory\n")
        else:
            for i in inventory:
                section_num += 1
                print(f"\nSection {section_num}: {i}\n")
    
    @staticmethod
    def search_product():
        product_to_search = input("\nWhich product to search: ").lower()
        for category, products in inventory.items():
            for i in products:
                if i.name == product_to_search:
                    print(f"\nSection: {category.capitalize()}...Name: {i.name.capitalize()}, Price: ${i.price}, Quantity: {i.quantity}, Revenue: ${i._revenue}, Code: {i.__code}\n")
                    return
        print("\nProduct not found\n")
        
    
    @staticmethod
    def export():
        name = input("\nName your file and its location --include the path...No extensions--: ")
        file_path = name

        with open(fr"{file_path}.txt", "w") as export_file:
            for section, products in inventory.items():
                export_file.write(f"\n{section}:\n")
                for product in products:
                    export_file.write(f"\nProduct: {product.name.capitalize()}, Price: {product.price}, Quantity: {product.quantity}, Revenue: {product._revenue}, Code: {product.__code}\n")
                export_file.write("\n")
        print("\nExport completed.\n")
        

            
    
        




