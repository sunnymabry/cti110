# This program calculates and displays travel expenses

# 02/23/2024

# CTI-110 P1HW2 - Travel Expense

# Sunny Mabry

#
budget=int(input("Enter the budget:")) #Asking user to enter his budget
destination=input("Enter your destination:") #Asking user to enter his destination
gas=int(input("Enter amount that you will spend on gas:")) #Asking user to enter the amount he spends on gas
accomodation=int(input("Enter amount that you will spend on accomodation:")) #Asking user to enter the amount he spends on accomodation
food=int(input("Enter amount that you will spend on food:"))#Asking user to enter amount he spends on food
expenses=gas+accomodation+food#Calculating total expenses
result=budget-expenses#subtracting expenses from budget
print("The result after subtracting your expenses from your budget for your",destination,"trip is:",result)#printing the result
