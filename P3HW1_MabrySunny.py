#Sunny Mabry
#Mar. 16th, 2024
#P3HW1-Debugging
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1 ,mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

lg = min(grades)
hg = max(grades)
sg = sum(grades)
avg = sg/6

print("-----------------------------Results---------------------------")
print("Lowest grade:",lg)
print("Highest grade:",hg)
print("Sum of grades:",sg)
print("Average:%.2f"%avg)
print("---------------------------------------------------------------")
      

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
else:
    if avg > 80:
        print('Your grade is: B')
    if avg > 70:
        print('Your grade is: C')
    if avg < 70:
        print('Your grade is: F') 
