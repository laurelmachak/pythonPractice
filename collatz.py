initialNum = int(input('pick a number'))
print(initialNum)
number = initialNum
for i in range(10):
	if number%2==0:
		number = number/2
		print(number)
	else:
		number = number*3+1 
		print(number)
		

	
