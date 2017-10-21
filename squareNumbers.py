squares = []

for i in range(1,11):
	squares.append(i**2)
	
print(squares)


print([i**2 for i in range(1,11)])


#nested for loops

print([(row, column) for row in range(4) for column in range(4)])


#if statements in comprehensions

import string
word = input("enter a word: ")

letters = [a for a in string.ascii_lowercase if a in word]

print(letters)


print(400%3)
