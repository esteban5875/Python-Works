import os

general_dict = {}

def add_to_dict():
    list_name = input("Enter name of the section: ").lower()
    
    if list_name in general_dict:
        print("Section already in Inventory")
    else:
        general_dict[list_name] = []

def  add_to_list():
    key = input("In which section ? : ").lower()
    if key not in general_dict:
        print("Section does not exist")
    else:
        product_name = input("What is the name of the product ? : ").lower()
        price = float(input("What is the price ? : "))
        quantity = int(input("What is the quantity ? : "))
        product = (product_name, price, quantity)
        general_dict[key].append(product)
        
def update_product_price():
    product_section = input("Which section ? : ").lower()
    if product_section not in general_dict:
        print("Section not found")
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
    product_section = input("What section ? : ").lower()
    if product_section not in general_dict:
        print("Section not found")
    else:
        product_name = input("What product to update ? : ").lower()
        found = False
        for product in general_dict[product_section]:
            if product[0] == product_name:
                found = True
        if found == True:
            new_name = input("Enter new name : ").lower()
            new_product_name = (new_name, product[1], product[2])
            print("Product updated succesfully")
        else:
            print("Product not found")    

def update_product_quantity():
    product_section = input("What section ? : ").lower()
    if product_section not in general_dict:
        print("Section not found")
    else:
        product_name = input("What product to update ? : ").lower()
        found = False
        for product in general_dict[product_section]:
            if product[0] == product_name:
                found = True
        if found == True:
            new_quantity = int(input("Enter new quantity: "))
            quantity_new = (product[0], product[1], new_quantity)
        else:
            print("Product not found")    

def display_products():
    section_display = input("In which section ? : ").lower()
    if section_display not in general_dict:
        print("Section not found")
        list = general_dict[section_display]
    else:
        for product in general_dict[section_display]:
            name = product[0].capitalize()
            price = product[1]
            quantity = product[2]
            revenue = price * quantity
            print(f"Product: {name} x {quantity}..Price: {price}...Revenue: {revenue} \n")
            
def clear():
  os_name = os.name
  if os_name == 'nt':
      os.system('cls')
  elif os_name == 'posix':
      os.system('clear')
  else:
      print("Clear command only for linux/unix and windows systems, your os was not identified")    

    
def display_sections():
    
    for sections in general_dict:
        def product_count():
            for sections in product:
                product_counting = 
        product_counting = product_count()
        print(f"\n{sections.capitalize()} x {product_counting} Products\n")

def export_():
    file_name = input(r"Name your file --Only txt is allowed for extension: ")
    def loop_iteration():
        for section in general_dict:
            yield section
    sections = loop_iteration()
    with open(f"{file_name.capitalize()}.txt", "w") as b:
        for product in sections:
         name = product[0]
         price = product[1]
         quantity = product[2]
         revenue = price * quantity
         b.write(f"Product: {name.capitalize()} x {quantity}..Price: {price}...Revenue: {revenue}\n")

def passing():
    pass        
        
while True:
    user_action = input(">>> ").lower()
    if user_action == "exit":
        break
    try:
        if user_action == "create section":
            add_to_dict()
        elif user_action == "in section add" :
            add_to_list()
        elif user_action == "display sections":
           display_sections()
        elif user_action == "in section display products":
            display_sections()
        elif user_action == "in section update name":
                update_product_name()
        elif user_action == "in section update price":
            update_product_price()
        elif user_action == "in section update quantity":
            update_product_quantity()
        elif user_action == "clear":
            clear()
        elif user_action == "export":
            export_()
        else:
            passing()
    except ValueError:
        print("Oops ! Value error, check your input and try again") 
    except FileNotFoundError:
        print("File especified not found")    

    
