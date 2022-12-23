# -*- coding: utf-8 -*-

#Password Generator Project (100 Days of Code: The Complete Python Pro Bootcamp)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#random.choice(list)


inipasslist = []


for letter in range(nr_letters):
    pick_letter = random.choice(letters)
    inipasslist.append(pick_letter)

for symbol in range(nr_symbols):
    pick_symbol = random.choice(symbols)
    inipasslist.append(pick_symbol)

for num in range(nr_numbers):
    pick_num = random.choice(numbers)
    inipasslist.append(pick_num)

#print(inipasslist)

random.shuffle(inipasslist)

print(''.join(inipasslist))
Spyder Editor

This is a temporary script file.
"""

