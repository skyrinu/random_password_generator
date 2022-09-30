# Because it's a random password generator program.
import random

# Greetings make the program interactive.
print("Welcome to the Random Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_range = int(input("How many letters would you like in your "
                          "password?\n"))
numbers_range = int(input(f"How many numbers would you like?\n"))
symbols_range = int(input(f"How many symbols would you like?\n"))

# Accumulators for storing result of each iteration of for loop done on a
# value.
password_letters = ""
password_numbers = ""
password_symbols = ""

# Picks specified numbers of random characters from pools of letters, numbers
# and characters.
for value in range(0, letters_range):
    password_letters += random.choice(letters)
for value in range(0, numbers_range):
    password_numbers += random.choice(numbers)
for value in range(0, symbols_range):
    password_symbols += random.choice(symbols)

# Picked characters are joined together and stored as a list for shuffling
# their order.
password = list(f"{password_letters}{password_numbers}{password_symbols}")

# Shuffles the order of characters of password.
random.shuffle(password)

# Joins each character of shuffled password list together and prints as a
# string.
randomized_order_password = ""
for character in password:
    randomized_order_password += character
print(randomized_order_password)
