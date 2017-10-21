#speed_of_light = 299792458 #meters/sec
#print speed_of_light
#print speed_of_light*100 #converted to cm/sec
#billionth = 1.0/1000000000
#nanostick = speed_of_light*billionth*100 #length light travels in a second in cm
#print nanostick
#Quiz 1: Given the variables defined here, write Python code that prints out
#the distance, in meters, that light travels in one processor cycle
speed_of_light=299792458 #meters per second
cycles_per_second=2700000000. #2.7 GHz
print speed_of_light/cycles_per_second
#can also store this in a variable, and then print it out
cycle_distance=speed_of_light/cycles_per_second
print cycle_distance
print cycle_distance*100 #cm
#you can change variables values
cycles_per_second=1800000000. #1.8 GHz
cycle_distance=speed_of_light/cycles_per_second
print cycle_distance
print cycle_distance*100

