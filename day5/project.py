#PASSWORD GENERATOR
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '(', ')']

pass_length = int(input("Enter pass length?: "))
symbol_length = int(input("Enter symbol number: "))
number_length = int(input("Enter number length: "))
alphabet_length = pass_length-number_length-symbol_length

password = ""

for alp in range(0, alphabet_length):
    password= password+random.choice(alphabets)

for sym in range(0, symbol_length):
    password= password+random.choice(characters)
for nbr in range(0, number_length):
    password = password  + str(random.choice(numbers))

print(password)

print("Now randomly changing the position of alphabets, number and symbols:")
pass_list = list(password)
random.shuffle(pass_list)
randomize_password=""
randomize_password = randomize_password.join(pass_list)
print(randomize_password)