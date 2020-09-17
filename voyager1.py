import math

Input = input("Number of days after 9/25/09: ")
answer = int(Input)

km = 1.609344
AU = 92955887.6

v1 = 38241
v2 = km*v1
v3 = v1/AU

d = 16637000000

Distance_1 = round(24*(v1*answer) + d)
Distance_2 = round((24*v2*answer) + d*km)
Distance_3 = round((24*v3*answer) + d/AU)

print("Miles from the sun:" ,Distance_1)
print("Kilometers from the sun:" ,Distance_2)
print("AU from the sun:" ,Distance_3)
