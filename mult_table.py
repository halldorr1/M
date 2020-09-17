# number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
# how_often = int(input("Input how often to multiply: ")) # Do not change this line
# counter = 0
# for i in range (0, how_often):
#     counter += 1
#     draslid = counter * number_to_multiply
#     print(draslid)



# sp3

# dog_age = int(input("Input dog's age: ")) # Do not change this line

# human_age = 24
# if dog_age in range(0,17):
#     if dog_age == 1:
#         print("Human age: 15")
#     else:
#         human_age = 4 * dog_age + 16
#         print("Human age: ",human_age)

# else:
#     print("Invalid age")


# sp4
import math

start_int = int(input("Input starting integer: "))

while start_int >= 2:
    start_int = math.sqrt(start_int)
    print(round(start_int, 4))


# sp5

# max_int = int(input("Input max integer: ",))

# counter = 1
# for i in range(1,max_int+1):
#     counter += 1
#     for j in range(1,counter):
#         print(j, end=' ') # í staðinn fyrir að enda línuna kemur bara bil
#     print("") # gerir loksins nyja linu þegar j-lykkjan er buin
