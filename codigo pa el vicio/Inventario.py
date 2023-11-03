product_list = []
price_list = []

while True:
    user_action = str(input(">>> ")).lower()
    Question = None

    if user_action == "add":
        product_name = str(input("What product are you adding: "))
        price = float(input("What is the price (no dollar sign): "))
        product_list.append(product_name)
        price_list.append(price)
    elif user_action == "display":
        for item, price in zip(product_list, price_list) :
            print(f"Product: {item} Price: {price}")
        


            
        

        

