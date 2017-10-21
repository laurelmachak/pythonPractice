from random import randint
answer = (randint(1,100))
for i in range(10):
	guess = input('guess a number ')
	if answer==guess:
		print str(answer) + ' you win'
	elif abs(answer-guess)<15:
		print 'hot'
	else:
		print 'cold'
print 'the answer was ' + str(answer)
