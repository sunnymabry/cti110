#Sunny Mabry
#April. 13th, 2024 
#P4HW2-Salary Calculator 
#Assignment assess student ability to edit and enhance exiting programs
#
numOfemp = 0
totalOverTimePay = 0
totalRegPay = 0
totalGrossPay = 0
while True:
    name = input("Enter employee's name or \"Done\" to terminate: ")
    if name == "Done":
        break
    else:
            numOfEmp += 1
            hours = float(input("Howmany hours did " + name + " worked? "))
            rate = float(input("What is " + name + "\' pay rate? "))
            overtime = 0
            overtimePay = 0
            regularPay = 0
            grossPay = 0
            if hours > 40:
                overtime = hours - 40
                overtimePay = overtime * rate * 1.5
                regularPay = 40*rate
                grossPay = regularPay + overtimePay
        else:
                regularPay = hours*rate
grossPay = regularPay
totalOverTimePay += overtimePay
toatlRegPay += regularPay
totalGrossPay += grossPay
print("|nEmployee name: " + name +"\n")
print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<29}".format("Hours Worked", "Pay Rate", "OverTime Pay", "RegHour Pay", "Gross Pay"))
print("--------------------------------------------")
print("{:<20.1f}{:20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours, overtime, overtimePay, regularPay, grossPay))
print()
print()
print("Total number of employees entered:", numOfEmp)
print("Total amount paid for over time: $" + '{:.2f}'.format(totalOverTimePay))
print("Total amount paid for regular hours: $" + '{:.2f}'.format(totalRegPay))
print("Total amount paid in gross: $" + '{:.2f}'.format(totalGrossPay))
                    
