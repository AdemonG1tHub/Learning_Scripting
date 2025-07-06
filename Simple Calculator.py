# Simple Calculator
# Scripted by Adem U
# 06/07/25 (UK date format)

import math
import time

print("The Simple Calculator.\nFirstly, enter the two numbers you would like in the equation.")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("\nNow, what would you like to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

sign = int(input("\nEnter a number (1-4): "))

if sign == 1:
    answer = num1 + num2
    symbol = "+"
elif sign == 2:
    answer = num1 - num2
    symbol = "-"
elif sign == 3:
    answer = num1 * num2
    symbol = "*"
elif sign == 4:
    if num2 == 0:
        print("\nError: Cannot divide by zero.")
        exit()
    answer = num1 / num2
    symbol = "/"
else:
    print("Invalid choice. Exiting.")
    exit()

print(f"\n\nYour answer to {num1} {symbol} {num2} is {answer}")