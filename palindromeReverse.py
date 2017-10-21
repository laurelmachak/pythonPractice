#The next one is reversing a string and if it's a palindrome, say so 
#It uses a while loop to countdown and print each character of the string 

string = input("please enter your first name: ")
string = string.lower()

check_palindrome = string

length = len(string)

print(string[::-1])


reversed = ""

while length > 0:
	print(string[-1])
	reversed = reversed + string[-1]
	string = string[:-1]
	length = length - 1
	
print(reversed)

if reversed == check_palindrome:
	print("this word is a palindrome")
	
	
print(reversed[0].upper() + reversed[1:])


