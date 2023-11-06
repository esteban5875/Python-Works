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
        "Section not found"
    else:
        product_name = input("What is the name of the product ? : ")
        price = float(input("What is the price ? : "))
        quantity = int(input("What is the quantity ? : "))
        product = ("", "", "")
        general_dict[key].append(product)



    