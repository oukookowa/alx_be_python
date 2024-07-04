#!/usr/bin/env python3
#Contains a function that performs basic arithmetic operations
def perform_operation(num1, num2, operation):
    if operation == 'add':
        result = round(float(num1 + num2), 2)
    elif operation == 'subtract':
        result = round(float(num1 - num2), 2)
    elif operation == 'multiply':
        result = round(float(num1 * num2), 2)
    else: 
        operation == 'divide'
        if num2 == 0:
            result = "Wrong entry. You cannot divide by 0!"
        else:
            result = round(float(num1 / num2), 2)
    return result