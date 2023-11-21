from Products.Product_Utils import *
import os
system = os.name


while True:
    while True:
        op = input("\n>>> ").lower()

        if op == "add section":
            Product.add_section()

        elif op == "in section add product":
            Product.add_product()

        elif op == "display all sections":
            Product.display_inventory()

        elif op == "in section display products":
            Product.display_section()

        elif op == "update product name":
            Product.update_product_name()

        elif op == "update product price":
            Product.update_product_price()

        elif op == "update product quantity":
            Product.update_product_quantity()

        elif op == "delete section":
            Product.delete_section()

        elif op == "from section delete product":
            Product.delete_product()

        elif op == "search product":
            Product.search_product()

        elif op == "export inventory":
            Product.export()
        
        elif op == "delete product":
            Product.delete_product()
        
        elif op == "clear":
            if system == "nt":
                os.system("cls")
            elif system == "posix":
                os.system("clear")
            else:
                print("Clear command is only available for windows or linux/unix operating systems.")
                
                








        