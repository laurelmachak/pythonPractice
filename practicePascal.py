ow1 = [1]
row2 = [1,1]
row3 = [1,2,1]
row4 = [1,3,3,1]
row5 = [1,4,6,4,1]

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)

print("\nNow to try appending:\n")


current_row = row1

print(current_row)

for x in range(len(current_row)):
	current_row.append(current_row[x])
	
print(current_row)
#binomial coefficients. in the nth row, choose item number r

def factorial(n):
	factList = []
	while n != 0:
		factList.append(n)
		n = n-1
	result = 1
	for i in range(len(factList)):
		result = result*factList[i]
	return result
	
print(factorial(4))


