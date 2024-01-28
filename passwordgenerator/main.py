#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
str=''
lettersRan = random.choices(letters,weights=None,k=nr_letters)
lettersJoin = str.join(lettersRan)
str=''
symbolsRan = random.choices(symbols,weights=None,k=nr_symbols)
symbolsJoin = str.join(symbolsRan)
str=''
numbersRan = random.choices(numbers,weights=None,k=nr_numbers)
numbersJoin = str.join(numbersRan)
str=''
print(lettersJoin+symbolsJoin+numbersJoin)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(lettersRan)
print(symbolsRan)
print(numbersRan)
symbolsRan.extend(numbersRan)
lettersRan.extend(symbolsRan)
random.shuffle(lettersRan)
print(f'Your Password : {str.join(lettersRan)}')
