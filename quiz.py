# sp 1
# a_str = input("Input a string: ")

# first = a_str[0]
# last = a_str[-1]
# print(first + " " + last)

# sp 2
# a_str = input("Input a string: ")
# b_str = a_str[-2:]
# a_str = a_str[:-2]

# print(b_str+a_str)

# sp3
# a_str = input("Input a string: ")

# counter1 = 0
# counter2 = 0

# for i in a_str:

#     if i.isupper():
#         counter1 += 1
#     elif i.islower():
#         counter2 += 1
#     else:
#         pass
# print(counter2)
# print(counter1)

# sp4


# a_str = float(input("Input a float: "))

# a_str = round(a_str,2)
# new_str = str(a_str)
# print("     " + new_str)


#sp 5

a_str = str(input("Input a string: "))

counter = 0
counter2 = 1
for i in a_str:
    if i.find(' ') != -1:
        counter2 += 1
    elif i.islower() or i.isupper() or i.isdigit():
        counter += 1
print('No. of letters: {}, no. of words: {}'.format(counter,counter2))

#sp 6
# name = input("Input a name: ")

# split_str = name.split(sep = ', ', maxsplit=2)
# stuff = split_str[1]
# letter = stuff[0]
# upper_letter = letter.upper()

# stuff2 = split_str[0]
# letter2 = stuff2[0]
# upper_letter2 = letter2.upper()
# rest = stuff2[1:]


# print(upper_letter + '. ' + upper_letter2+rest)

#sp 7
# my_int = int(input('Give me an int >= 0: '))

# a = 1
# bin_str = " "
# new_int = my_int

# while a > 0:
#     if new_int % 2 == 1:
#         bin_str += "1"
#     elif new_int % 2 == 0:
#         bin_str += "0"
#     a = new_int // 2
#     new_int = a

# bin_str = bin_str [::-1]

# if bin_str != "0":
#     for i in bin_str:
#         break

# print("The binary of {} is {}".format(my_int,bin_str))