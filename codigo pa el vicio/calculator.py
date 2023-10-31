#Imported two essential modules, math, and sys, explanations below

import sys 
import math

#Title print, so it looks aesthetic :]

print("==========")
print("Calculator")
print("==========")

result = None #Result variable in global scope so that it can be used anywhere, equals a Nonetype for now but it will be used later

"""added 4 fundamental functions, exponents, radicals, addition, substraction,
   division, and multiplication to have a complete calculator"""

def add(a, b):
    return a + b

"""addition function, a and b represen the values that will be inputed and we use a and b as a demonstration for the function
   to understand what it has to do (a + b) in this case"""

def subtract(a, b): #Substraction function, in this function we give the program a substraction feature (a - b)
    return a - b

def multiply(a, b): #Same here, we give the program a function to multiply (a * b)
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero not possible"
    else: 
        return a / b

    """this is an interesting one, we give the program a function to divide (a / b) but as you saw
       we have a conditional IF so that if the divisor is 0, [which in a division when the divisor is
        0 is imposible to do], then the result will be an error"""
    

def expo(a, b):
    return a ** b

"""added a function here so that we can do exponents, " a to the power of b " but there is a limit
to the result because things can get big, the limit is below """


def radical(a, b):
    return math.pow(a, 1.0/b)

"""here we finally used the math module, to do radicals, in here we use the power function, but we give it
   a formula, the formula is (a to the power of 1 divided b), this way, we reverse the power, and we get a radical """
    
        

while True:

    try:

            
        max_number = sys.float_info.max #In here we used the sys module to see what is the maximum number the computer can display, use is below

        #Here we stored the error message for a ValueError in a variable so that it is easier to recall and print
        
        valid_values = "<Value Error> Operators: [+, -, /, *, expo, root], whole numbers and decimals are allowed --No letters, special characters, nor irrationals or things like '√' or 'π'--"

        #This is the OP input, in here we especify what we want to do, the operator
        
        op = input("Enter an operator [+, -, /, *, expo, root] or enter 'bye' to exit: ")

        #In this IF conditional, we say that if the input for the operator is 'bye', the program will be exited

        if op == "bye":
            break

        #In here we use a list and a IF conditional to say that if the OP input is not within this value, then display an error

        if op not in ["+", "-", "*", "/", "expo", "root", "bye"]:
            print(valid_values)

        #If the previous IF conditional is not met, then the code within the ELSE will be run

        else:

            #In here, val1 and val2 will be the values the calculator will work with
            
            val1 = float(input("Enter the first value, exponent base, or number to root: "))

            val2 = float(input("Enter the second value, exponent value or root value: "))

        #The functioning of the calculator, here we start using the result variable that was a Nonetype previously

            if op == "+":
                result = add(val1, val2) #Addition functioning, IF the op is "+" then the addition function will be called
                print("    ")
                print(f"Result is: {round(result, 10)}")
                print("    ")
            elif op == "-":
                result = subtract(val1, val2) #Substraction function, IF the op is "-" then the substraction function will be called
                if val1 < 0 and val2 < 0:
                    result = abs(result) #Absoloute values in multiplication and substraction to follow the minus minus plus rule. Absolute values to ensure the result number is positive
                else:
                    print("    ")
                    print(f"Result is: {round(result, 10)}") #Used an f string in the result to interpolate variables and the decimals greater than 10 values are rounded to 10 values only
                    print("    ")
                    
            elif op == "*":
                result = multiply(val1, val2) #Multiplication function, IF the op is "*" then the substraction function will be called
                if val1 < 0 and val2 < 0:
                    result = abs(result) #Absolute values in multiplication and substraction to follow the minus minus plus rule. Absolute values to ensure the result number is positive
                else:
                    print("    ")
                    print(f"Result is: {round(result, 10)}") #Used an f string in the result to interpolate variables and the decimals greater than 10 values are rounded to 10 values only
                    print("    ")
            elif op == "/":
                result = division(val1, val2) #Division function, IF the op is "/" then the division function will be called
                print("    ")
                print(f"Result is: {round(result, 10)}") #Used an f string in the result to interpolate variables and the decimals greater than 10 values are rounded to 10 values only
                print("    ")
            elif op == "expo":
                result = expo(val1, val2)#Exponent function, IF the op is "expo" then the exponent function will be called
                print("    ")
                print(f"Result is: {round(result, 10)}") #Used an f string in the result to interpolate variables and the decimals greater than 10 values are rounded to 10 values only
                print("    ")
                    
            elif op == "root":
                result = radical(val1, val2) #Radical function, IF the op is "root" then the radical function will be called
                print("    ")
                print(f"Result is: {round(result, 10)}")#Used an f string in the result to interpolate variables and the decimals greater than 10 values are rounded to 10 values only
                print("    ")
                    
            else:
                print("    ") #If neither of this statements was run and the error is not handled here, then this ELSE statement will display an "Unknown Error"
                print("Unknown Error...Maybe try restarting ?")
                print("    ")

    #In here we use exceptions to handle two common errors in the code, a ValueError, and a OverflowError
    
    except ValueError:  #If there is a invalid input in the val1, val2, or op inputs, then there will be a value error and the valid_values variable will be printed
        print("           ")
        print(valid_values)
        print("           ")

    except OverflowError:
        """Remember the sys function ?, we used it to gather information about the maximum numerical the computer can display, and if there is an
           OverflowError,  where the result exceeds this limit, then the following message with the sys function will be printed""" 

        print("                ")
        print(f"Result too large...Limit is: {max_number}") #Max number is the result of the sys module stored in a variable, used an f string to interpolate variables into the string
        print("                ")
