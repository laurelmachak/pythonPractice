## Bisection Search to Find a Square Root

x = float(input("enter a number:"))
epsilon = 0.00001
num_guesses = 0
low = float(0.0)
high = x
ans = (high + low)/2.0
while high - low >= 2.0 * epsilon:
    print("low =",low,"high =", high)
    num_guesses += 1
    if ans ** 2.0 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)