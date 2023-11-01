import math
import sys

def pythagorean_(a, b):
    return math.sqrt(a**2 + b**2)

while True:
    val1 = input("Do you know the hypothenuse ? --1 if yes, any other key if not: ")
    max_num = sys.float_info

    try:

        if val1 == 1:
            val4 = float(input("\nEnter first leg: "))
            val5 = float(input("\nEnter second leg: "))
            result = pythagorean_(float(val4), float(val5))
            print(f"\nThe hypothenuse: {round(result, 10)}\n")
        else:
            val2 = float(input("\nEnter leg: "))
            val3 = float(input("\nEnter hypothenuse: "))
            result = math.sqrt(val3**2 - val2**2)
            print(f"\nThe other leg: {round(result, 10)}\n")
    except ValueError:
        print("\nInvalid Input Error\n")
    except OverflowError: 
        print(f"\nResult too large...Limit is: {max_num}\n")
