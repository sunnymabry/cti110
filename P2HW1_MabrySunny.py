#Sunny Mabry
#Date- Mar. 9th, 2024
#CTI-110 P2HW1-Travel
#Brief description: This project is used to calculate the travel expense. It uses basic arithmetic function to calculate the amount needed and we have formatted the output using printf
#
print("This program calculates and displays travel expenses")
amount=int(input("Enter budget:"))
dest=input("Enter your travel destination:")
gas=int(input("How much do you think you will spend on gas?"))
hotel=int(input("Approximately, how much will you need for accommodation/hotel?"))
food=int(input("Last, how much do you need for food?"))
#output
print("---------------Travel Expense---------------")
print(f"{'Location:':<20}",f"{dest:<20}")
print(F"{'Initial budget:':<20}",f"{'$'+str(float(amount)):<20}")
print(f"{'Fuel:':<20}",f"{'$'+str(float(gas)):<20}")
print(f"{'Accommodation:':<20}",f"{'$'+str(float(hotel)):<20}")
print(f"{'Food:':<20}",f"{'$'+str(float(food)):<20}")
#calculating the remaining balance
remaining = amount-(gas+hotel+food)
print("--------------------------------------------")
print(f"{'Remaining balance:':<20}",f"{'$'+str(float(remaining)):<20}")
