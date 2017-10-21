
hours1 = int(input("first number of hours: "))
minutes1 = int(input("first number of minutes: "))
seconds1 = int(input("first number of seconds: "))

hours2 = int(input("second number of hours: "))
minutes2 = int(input("second number of minutes: "))
seconds2 = int(input("second number of seconds: "))

totalSeconds1 = (hours1*60*60) + (minutes1*60) + seconds1
totalSeconds2 = (hours2*60*60) + (minutes2*60) + seconds2

secondsPassed = totalSeconds2 - totalSeconds1
print(secondsPassed)
