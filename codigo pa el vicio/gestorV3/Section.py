from Product_minimal import *

class SectionDoesNotExist(KeyError):
    def __init__(self, section_entered):
        self.section_entered = section_entered
        self.message = f"The section entered does not exist."



class Section:
    
    inventory = {}

    def __init__(self, name):
        self.name = name
        self.product_list = []
    
    def add_section(section_name):
        new_section = Section(name=section_name)
        Section.inventory[section_name] = new_section.product_list
    
    def add_product(self, product_name, product_price, product_quantity, section):
        if section not in Section.inventory:
            raise SectionDoesNotExist(section)
        else:
            product = Product(name=product_name, price=product_price, quantity=product_quantity)
            Section.inventory[section].append(product)
            
    def delete_product():
        pass

    def update_name(self, new_name):
        pass

    def get_products(self):
        return self.product_list