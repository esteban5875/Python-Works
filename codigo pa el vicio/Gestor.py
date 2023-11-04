'''
This code creates an Inventory Management program.
The code starts by defining 4 empty lists.
The code then enters an infinite while loop.
The code will then create a user_action variable and set it to the user's input.
The code will then try to do the following:
If the user input "add", the code will add the product, price, and quantity entered by the user to the 4 empty lists.
If the user input "display", the code will print the list of products, prices, and quantities.
If the user input "delete", the code will allow the user to delete an item from the lists.
If the user input "update", the code will allow the user to update an item from the lists.
If the user input "reset" the code will reset all lists.
If the user input "clear" console is cleared.
If the user input "export", then an option to export as .txt will be used.
If there is a ValueError, the code will print "Oops! An error occurred while processing your request. Please check your input and try again."
'''
import os

product_list = []
price_list = []
quantity_list = []
total_price_list = []

def passing():
    pass



while True:
    user_action = str(input(">>> ")).lower()
    os_name = os.name
    try:
        if user_action == "exit":
            break
        elif user_action == "add":
            product_name = input("What product are you adding: ").lower()
            if product_name in product_list:
                print(f"Item already in list --Use update to change product already in list--")
            elif product_name == "":
                passing()
            else:
                price = float(input("What is the price (no dollar sign): "))
                quantity = int(input("What quantity (just number): "))
                product_list.append(product_name)
                quantity_list.append(quantity)
                total_price_list.append(price*quantity)
                price_list.append(price)
        elif user_action == "display":
            for item, price, quantity, total in zip(product_list, price_list, quantity_list, total_price_list):
                print(f"Product: {item.capitalize()} x {quantity}...Product...Price: {price}$...Revenue: {round(total, 3)}$")
        elif user_action == "delete":
            deletion = str(input("What are you deleting: ")).lower()
            if deletion not in product_list:
                print("Item not found")
            else:
                confirmation = str(input("Are you sure ? : ")).lower()
                if confirmation.lower() == "yes":
                    index_to_del = product_list.index(deletion)
                    price_list.pop(index_to_del)
                    total_price_list.pop(index_to_del)
                    quantity_list.pop(index_to_del)
                    product_list.pop(index_to_del)
                elif confirmation.lower() == "no":
                    print("Alright")
                else:
                    passing()
        elif user_action == "update":
            product_selection = str(input("Which: ")).lower()
            if product_selection not in product_list:
                passing()
            else:
                update_option = str(input("What property to update: ")).lower()
                if update_option not in ["name", "quantity", "price"]:
                    passing()
                else:    
                    if update_option == "name":
                        new_name = str(input("Enter new product name: ")).lower()
                        index_to_update = product_list.index(product_selection)
                        product_list[index_to_update] = new_name
                    elif update_option == "quantity":
                        index_to_update = product_list.index(product_selection)
                        new_quantity = int(input("Enter new product quantity: "))
                        quantity_list[index_to_update] = new_quantity
                        total_price_case = price_list[index_to_update] * new_quantity
                        total_price_list[index_to_update] = total_price_case 
                    elif update_option == "price":    
                        index_to_update = product_list.index(product_selection)
                        new_price = float(input("Enter new price: "))
                        price_list[index_to_update] = new_price
                        quantity_case = quantity_list[index_to_update]
                        total_price_case = float(new_price) * float(quantity_case)
                        total_price_list[index_to_update] = total_price_case
        elif user_action == "reset":
            confirmation_ = input("Are you sure ? : ").lower()
            if confirmation_ == "yes":
                product_list.clear()
                price_list.clear()
                quantity_list.clear()
            elif confirmation_ == "no":
                print("       ")
                print("Alright")
                print("       ")
            else:
                passing()
        elif user_action == "clear":
            if os_name == "posix":
                os.system('clear')
            elif os_name == "nt":
                os.system('cls')
            else:
                print("Your OS was not defined, --clear-- only works for Windows or Unix/Linux Systems")
        elif user_action == "export":
            name_file = input("Name your file and path --No extensions-- : ")
            with open(fr"{name_file}.txt", "x") as b:
                for item, price, quantity, total in zip(product_list, price_list, quantity_list, total_price_list):  
                    b.write(f"Product: {item} x {quantity}...Price: {price}...Revenue: {total}")
        elif user_action == "import":
            file_option = input("Which file to input: ")
            
            
    except ValueError:
        passing()
