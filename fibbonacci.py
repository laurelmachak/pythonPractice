fibbonacci = [1,1]

length = int(input("print fibbonacci until: "))

for i in range(length):
    next_number = fibbonacci[-1]+fibbonacci[-2]
    if next_number>length:
        break
    fibbonacci.append(next_number)

    
print(fibbonacci)


last = fibbonacci[-1]
secondLast = fibbonacci[-2]

print(str(last) + "/" + str(secondLast) + ":", last/secondLast)

print(str(secondLast) + "/" + str(last) + ":", secondLast/last)

    