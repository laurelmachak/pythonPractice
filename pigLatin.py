print("please don't put a space in front ")
fullName = input("What is your name?")


space = fullName.find(" ")
fullName = fullName.lower()
firstName = fullName[0:space]
lastName = fullName[space+1:]

def pigGen(word):
	firstLetter = word[0]
	suffix = firstLetter + "ay"
	word = word[1].upper() + word[2:] + suffix
	return word
	
print (pigGen(firstName) + " " + pigGen(lastName))