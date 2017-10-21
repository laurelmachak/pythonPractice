text = """
I live my life a quarter mile at a time. \
Nothing else matters: not the mortgage, not the store, \
not my team and all their bullshit. \
For those ten seconds or less, I’m free.

"""
words = text.split(" ")


letters = [i[0] for i in words]

print(letters)


word = "Welcomed"
#string = word
list_of_strings = []

for i in range(len(word)):
	#string.replace(word[0], "")
	
	list_of_strings.append(word[:i] + word[i+1:])
	
print(list_of_strings)

list = [word[:i] +word[i+1:] for i in range(len(word))]
print(list)
	
	