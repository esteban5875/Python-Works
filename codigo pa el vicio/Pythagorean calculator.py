import math
import sys

def pythagorean_(a, b):
    return math.sqrt(a**2 + b**2)

while True:
    val1 = input("Enter hypothenuse --optional--: ")
    val2 = input("Enter a leg: ")
    val3 = input("Enter 2nd leg --Only if no hypothenuse--: ")
    max_num = sys.float_info

    try:
        if (val1 == "" and val3 == "") or (val2 == ""):
            print("\n Error \n")
        else:
            if val1 != "":
                result = pythagorean_(float(val1), float(val2))
                print(f"\n The other leg is: {round(result, 10)} \n")
            else:
                result = pythagorean_(float(val2), float(val3))
                print(f"\n The hypothenuse: {round(result, 10)} \n")
    except ValueError:
        print("\n Invalid Input Error \n")
    except OverFlowError: 
        print(f"\n Result too large...Limit is: {max_num} \n")
