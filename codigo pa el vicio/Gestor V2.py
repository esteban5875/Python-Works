general_dict = {

}

def add_to_dict():
    list_name = input("Enter name of the section: ")
    
    if list_name in general_dict:
        print("Section already in Inventory")
    else:
        general_dict[list_name] = []

def  add_to_list():
    key = input("In which section ? : ")
    if key not in general_dict:
        print("Section does not exist")
    else:
        product_name = input("What is the name of the product ? : ")
        price = float(input("What is the price ? : "))
        quantity = int(input("What is the quantity ? : "))
        product = (product_name, price, quantity)
        general_dict[key].append(product)
        
def update_product_price():
    product_section = input("Which section ? : ").lower()
    if product_section not in general_dict:
        print("Section not found").lower()
    else:
        product_name = input("What product to update ? : ").lower()
        found = False
        for product in general_dict[product_section]:
            if product[0] == product_name:
                found = True
        if found == True:
            print("Price updated succesfully")
            new_price = float(input("Enter new price: "))
            product = (product[0], new_price, product[2])
        else:
            print("Product not found")   

def update_product_name():
    product_section = input("What section ? : ")
    if product_section not in general_dict:
        print("Section not found")
    else:
        product_name = input("What product to update ? : ")
        found = False
        for product in general_dict[product_section]:
            if product[0] == product_name:
                found = True
        if found == True:
            new_name = input("Enter new name : ")
            new_product_name = (new_name, product[1], product[2])
            print("Product updated succesfully")
        else:
            print("Product not found")    

def update_product_quantity():
    product_section = input("What section ? : ")
    if product_section not in general_dict:
        print("Section not found")
    else:
        product_name = input("What product to update ? : ")
        found = False
        for product in general_dict[product_section]:
            if product[0] == product_name:
                found = True
        if found == True:
            new_quantity = int(input("Enter new quantity: ")

def display_section():
    for i in general_dict:
        print(f"{i}\n")

def display_products():
    section_display = input("In which section ? : ")
    if section_display not in general_dict:
        print("Section not found")
    else:
        for i in general_dict[section_display]:
            print(f"{i}\n")

    
