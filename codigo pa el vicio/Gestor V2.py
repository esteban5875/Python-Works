import os

general_dict = {}

def add_to_dict():
    list_name = input("\nEnter name of the section: ").lower()
    
    if list_name in general_dict:
        print("\nSection already in Inventory\n")
    else:
        general_dict[list_name] = []

def  add_to_list():
    key = input("\nIn which section ? : ").lower()
    if key not in general_dict:
        print("\nSection does not exist\n")
    else:
        product_name = input("\nWhat is the name of the product ? : ").lower()
        price = float(input("\nWhat is the price ? : "))
        quantity = int(input("\nWhat is the quantity ? : "))
        product = (product_name, price, quantity)
        general_dict[key].append(product)
        
def update_product_price():
    product_section = input("Which section ? : ").lower()
    if product_section not in general_dict:
        print("\nSection not found\n")
    else:
        product_name = input("\nWhat product to update ? : ").lower()
        found = False
        for product, index in enumerate(general_dict[product_section]):
            if product[0] == product_name:
                found = True
        if found == True:
            print("\nPrice updated succesfully\n")
            new_price = float(input("\nEnter new price: "))
            new_product_price = (product[0], new_price, product[2])
            general_dict[product_section][index] = product
        else:
            print("\nProduct not found\n")   

def update_product_name():
    product_section = input("\nWhat section ? : ").lower()
    if product_section not in general_dict:
        print("\nSection not found\n")
    else:
        product_name = input("\nWhat product to update ? : ").lower()
        found = False
        for index, product in enumerate(general_dict[product_section]):
            if product[0] == product_name:
                found = True
        if found == True:
            new_name = input("\nEnter new name : ").lower()
            new_product_name = (new_name, product[1], product[2])
            general_dict[product_section][index] = new_product_name
            print("\nProduct updated succesfully\n")
        else:
            print("\nProduct not found\n")    

def update_product_quantity():
    product_section = input("\nWhat section ? : ").lower()
    if product_section not in general_dict:
        print("\nSection not found\n")
    else:
        product_name = input("\nWhat product to update ? : ").lower()
        found = False
        for index, product in enumerate(general_dict[product_section]):
            if product[0] == product_name:
                found = True
        if found == True:
            new_quantity = int(input("\nEnter new quantity: "))
            quantity_new = (product[0], product[1], new_quantity)
            general_dict[product_section][index] = quantity_new
        else:
            print("\nProduct not found\n")    

def display_products():
    section_display = input("\nIn which section ? : ").lower()
    if section_display not in general_dict:
        print("\nSection not found\n")
        list = general_dict[section_display]
    else:
        for product in general_dict[section_display]:
            name = product[0].capitalize()
            price = product[1]
            quantity = product[2]
            revenue = price * quantity
            print(f"\nProduct: {name} x {quantity}..Price: {price}...Revenue: {revenue}\n")
            
def clear():
  os_name = os.name
  if os_name == 'nt':
      os.system('cls')
  elif os_name == 'posix':
      os.system('clear')
  else:
      print("\nClear command only for linux/unix and windows systems, your os was not identified\n")    

    
def display_sections():
    
    for sections in general_dict:
        print(f"\n{sections.capitalize()}\n")

def export_():
    file_name = input(r"Name your file --Only txt is allowed for extension: ")
    def loop_iteration():
        for section in general_dict:
            yield section
    sections = loop_iteration()
    with open(fr"{file_name.capitalize()}.txt", "w") as b:
        for product in sections:
         name = product[0]
         price = product[1]
         quantity = product[2]
         revenue = price * quantity
         b.write(f"\nProduct: {name.capitalize()} x {quantity}..Price: {price}...Revenue: {revenue}\n")

def passing():
    pass        
        
def delete_sections():
    section_name = input("\nEnter section name: ").lower()
    if section_name not in general_dict:
        print("\nSection not found\n")
    else:
        general_dict.pop(section_name)
    
def delete_products():
    section_name = input("\nIn which section ? : ").lower()
    if section_name not in general_dict:
        print("\nSection not found\n")
    else:    
         product_name = input("\nEnter product to delete: ").lower()
         for product in general_dict[section_name]:
            if product[0] == product_name:
                section_name.pop(product[0], product[1], product[2])
            else:
                print("\nProduct not found\n")
             
def reset_():
    confirmation = input("Are you sure ? (yes/no) : ").lower()
    if confirmation == "yes":
        general_dict.clear()
        print("\nReset succesful\n")
    elif confirmation == "no":
        print("\nReset cancelled...\n")
    else:
        return                          
                                    
while True:
    user_action = input(">>> ").lower()
    if user_action == "exit":
        break
    try:
        if user_action == "create section":
            add_to_dict()
        elif user_action == "in section add product" :
            add_to_list()
        elif user_action == "display sections":
           display_sections()
        elif user_action == "in section display products":
            display_products()
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
        elif user_action == "delete section":
            delete_sections()
        elif user_action == "in section delete product":
            delete_products()
        elif user_action == "reset data":
            reset_()    
        else:
            passing()
    except ValueError:
        print("\nOops ! Value error, check your input and try again\n") 
    except FileNotFoundError:
        print("\nFile especified not found\n")

    
    
