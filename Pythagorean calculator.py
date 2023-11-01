import sys
import math

def pythagorean_(a, b):
    c = math.sqrt(a**2 + b**2)

def pythagorean_case2(a, b):
    c = math.sqrt(a**2 + b**2)

while True:
    val1 = input("Enter hypothenuse --optional--: ")
    val2 = input("Enter a leg: ")
    val3 = input("Enter 2nd leg --Only if no hypothenuse--: ")
    max_num = sys.float_info

    try:
        if (val1 == "") and (val3 == ""):
            print("\n Error \n")
        else:
            if (val1 == float(val2)) and (val2 == float(val2)):
                pythagorean_case2()