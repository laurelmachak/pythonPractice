#2-1. If statements
#The mythical island nation of Laskoatu has a rather simple tax code. The first $1000 of income is taxed at 5%. 
#The next $1000 is taxed at 10%. Any income beyond the first $2000 is taxed at 15%. 
#Complete the following script so that it asks the user for his or her income and outputs the amount of tax owed.
#In [24]:

# Enter your code here

income = float(input("please enter your total income: "))

first_1000 = 1000.0
second_1000 = 1000.0
over_2000 = None
tax = None

if income <= 1000.0:
	tax = income * .05
elif income <= 2000.0:
	second_1000 = income - first_1000
	tax = (first_1000 * .05) + (second_1000 * .10)
else:
	over_2000 = income - 2000.0
	tax = (first_1000 * .05) + (second_1000 * .10) + (over_2000 * .15)

print("tax: " + str(tax))


# Sample output below
#Please enter your income:2500
#tax:  225.0