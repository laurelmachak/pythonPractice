
first_Word = input("enter first word: ").lower()
second_Word = input("enter second word: ").lower()

same_letters =[]
for i in first_Word:
	for x in second_Word:
		if i in x:
			if i not in same_letters:
				same_letters.append(i)

same_letters.sort()
print(same_letters)
