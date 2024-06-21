#!/bin/bash
#Calculates user's yearly potential savings based on monthly income and expenses and 5% interest rate
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

savings = float(income - expenses)
projected_savings = float(savings * 12 + (savings * 12 * 0.05))

print("Your monthly savings are: $"+str(savings))
print("Projected savings after one year, with interest, is: $"+str(projected_savings))
