#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lst_num = number % 10
    if lst_num < 6 and lst_num != 0:
        print(f"Last digit of {number} is {lst_num} and is\
                less than 6 and not 0")
    elif lst_num > 5:
        print(f"Last digit of {number} is {lst_num} and is greater than 5")
    else:
        print(f"Last digit of {number} is {lst_num} and is 0")
else:
    lst_num = abs(number) % 10
    print(f"Last digit of {number} is -{lst_num} and is less than 6 and not 0")
