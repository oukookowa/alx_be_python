#takes 2 numbers as input from user & divides 1st number by 2nd number
def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    try:
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")

    #perform division operation with potential errors
    try: 
            result = numerator / denominator
            print(f"The result of the division is {result}")
    #handle ZeroDivisionError when dividing by zero
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    #handles the exception in case invalid input is entered
    except UnboundLocalError:
        return "You entered the wrong value(s), cannot proceed operation!"
    except TypeError:
        return "Unsupported operand type(s) for division"   
   #finally:
        #return "Division operation complete..."