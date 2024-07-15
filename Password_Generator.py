#Password Generator Project
#Created by: Madhup Kumar Tiwari
#LinkedIn: https://www.linkedin.com/in/madhup-t
#github: https://github.com/madhuptiwari
#Date: 14 Jul 2024

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Selection type

type_of_password = input("Do you want a easy or hard password?")
type_of_password = str.casefold(type_of_password)

#Eazy Level - Order not randomised:

if type_of_password == "easy":
  password = ""
  for letter in range(0, nr_letters+1):
    password += random.choice(letters)
  
  for symbol in range(0, nr_symbols+1):
    password += random.choice(symbols)
  
  for number in range(0, nr_numbers+1):
      password += random.choice(numbers)
  print(f"Your password is:{password}")

#Hard Level - Order of characters randomised:

elif type_of_password == "hard":
  password_list  = []
  for letter in range(0, nr_letters+1):
    password_list += random.choice(letters)
  
  for symbol in range(0, nr_symbols+1):
    password_list += random.choice(symbols)
  
  for number in range(0, nr_numbers+1):
      password_list += random.choice(numbers)
  print(password_list)
  random.shuffle(password_list)
  password = ""
  for char in password_list:
    password += char
  print(f"Your password is: {password}")
else:
  print("Please enter a valid input")
