general_dict = {

}

def add_to_dict():
    list_name = input("Enter name of the section: ")
    
    if list_name in general_dict:
        print("Section already in Inventory")
    else:
        general_dict[list_name] = []

def  add_to_list():
    key = input("In which section ?: ")
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
    if sections not in general_dict:
        print("Section not found").lower()
    else:
        product_name = input("What product to update ? : ").lower()
        found = False
        for product in general_dict[sections]:
            if product[0] == products:
                new_price = float(input("Enter new price: "))
                product = (product[0], new_price, product[2])
                product_found = True
            else:
                found = False
        if found == True:
            print("Price updated succesfully")
        else:
            print("Product not found")    


    
