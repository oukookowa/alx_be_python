#!/bin/bash
#Calculates user's yearly potential savings based on monthly income and expenses and 5% interest rate
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 *  0.05)

print("Your monthly savings are: $"+str(round(monthly_savings, 2)))
print("Projected savings after one year, with interest, is: $"+str(round(projected_savings, 2)))
