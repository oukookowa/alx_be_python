#!/bin/bash
#Converts temperature to degrees celsius and fahrenheit
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Function converts temperature from fahrenheit to celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    temprature_celcius = round((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR, 2)
    print(f"{fahrenheit}°F is {temprature_celcius}°C")

#Function converts temperature from celsius to fahrenheit 
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    temperature_fahrenheit = round(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32, 2)
    print(f"{celsius}°C is {temperature_fahrenheit}°F")

#Validation of user input for valid values and strings
def operation(): 
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return None             #when the function executes this returns value as None it stops since no calculation will go through
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if temperature_unit not in ["C", "F"]:
        print("Invalid entry. Enter a valid temperature unit (C/F)!")
        return None
    #Calling of the functions based on user's choice
    elif temperature_unit == "C":
        return convert_to_fahrenheit(temperature)
    else: 
        temperature_unit == "F"
        return convert_to_celsius(temperature)

#Calling the operation function     
operation()
while True:
    response = input("Do you want to continue? Enter Y to continue or Q to quit: ").upper()   
    if response not in ["Y", "Q"]:
        print("Invalid choice. Enter Y or Q!")
        pass
    elif response == "Q":
        print("Sad to see you go. Goodbye!")
        break
    else: 
        response == "Y"
        operation()
        pass