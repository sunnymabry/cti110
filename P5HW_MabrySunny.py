#Sunny Mabry
#April. 27th, 2024
#CTI-110 P5HW-Math Quiz
#Use of loops, functions and module import to complete assignments
#
import random
def adddRandNums():
    num1 = random.radint(100,1000)
    num2 = random.radint(100,1000)
    print(" " + str(num1))
    print("+" = str(num2))
    user_input_sum = int(input())
    if(user_input_sum == (num1 + num2)):
        print("Congratulations! Your answeris correct.")
            else:
                print("sorry, your answer is incorrect")
                print("The coreect answer is " + str(num1+num2))
def subRandNums():
    num1 = random.randint(100,1000)
    num2 = random.randint(100,1000)
    print(" " + str(num1))
    print("-" + str(num2))
    user_input_sub = int(input())
    if(user_input_sub == (num1 - num2)):
        print("Congratulations! Your answer is correct>")
        else:
            print("Sorry, your answer is incorrect")
            print("The correct answer is " + str(num1-num2))
def main():
    user_menu_input = 0
    while user_menu_input != 3:
        print("\nMAIN MENU")
        print("--------------")
        print("1) Add Random Numbers")
        print("2) Subtract Random NUmbers")
        print("3) Exit")
        user_menu_input = int(input())
        if(user_menu_input == 1):
            addRandNums()
            elif(user_menu_input == 2):
                subRandNums()
start of the program main()
