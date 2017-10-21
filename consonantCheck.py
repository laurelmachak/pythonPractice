vowels = ["a", "e", "i", "o", "u"]

def is_consonant(letter):
	for i in vowels:
		if i == letter:
			return False
		else:
			return True
			
user_letter = input("enter a letter: ").lower()

print(is_consonant(user_letter))


def pigGen(word):
	suffix = "ay"
	if is_consonant(word[0]):
		word = word[1:] + word[0] + suffix
	else:
		word = word + suffix
	return word
	

pizza = input("enter a word: ").lower()

print(pigGen(pizza))