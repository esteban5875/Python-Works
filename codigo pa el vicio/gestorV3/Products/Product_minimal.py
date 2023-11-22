from Codes.Code_Utils import *
import os

class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__code = Codes.generate_code()
        self._revenue = 0 

    def update_revenue(self):
        self._revenue = self.price * self.quantity  
    
    def update_product_name(self, new_name):
        self.name = new_name

    def update_product_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.update_revenue()

    def update_product_price(self, new_price):
        self.price = new_price
        self.update_revenue()
        
    def display_product(self):
        print("Name: " + self.name + ", Price: " + self.price)

            
    
        




