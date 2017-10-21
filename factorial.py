def factorial(n):
	result = 1
	while n>=1:
		result = result * n
		n = n -1
	return result
	
number = int(input("enter a number to find its factorial: "))

print (factorial(number))