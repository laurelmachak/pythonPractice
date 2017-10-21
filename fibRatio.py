fibbonacci = [1,1]

length = int(input("how many numbers in fibbonacci sequence?: "))

for i in range(length-2):
    next_number = fibbonacci[-1]+fibbonacci[-2]
    print(str(fibbonacci[-1]) + "/" + str(fibbonacci[-2]) + ":", fibbonacci[-1]/fibbonacci[-2])
    fibbonacci.append(next_number)

    
print(fibbonacci[0:-1])


