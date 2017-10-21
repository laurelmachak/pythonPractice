
valid = False

while valid == False:

    try:
        x = float(input("Enter a number: "))
        print("The reciprocal of your number is", 1/x)
        valid = True
    except ValueError:
        print("You did not enter a valid number.")
    except ZeroDivisionError:
        print("Zero does not have a reciprocal")
        exit()
    except:
        print("something else went wrong.")
        