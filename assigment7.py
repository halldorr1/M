# def inc(num):
#     result = num + 1
#     return result

# number = int(input("Enter a number: "))
# nubmer_incremented  = inc(number)
# print(nubmer_incremented)

#sp 1

# def string(input_str):
#     new_str = input_str[::2]
#     return new_str

# input_str = input('Enter a string: ')
# new_str = string(input_str)
# print('Every other character: ',new_str)

#sp 2

# def count_digits(digits):
#     counter = 0
#     for i in digits:
#         if i.isdigit():
#             counter += 1
#     return counter

# digits = input('Enter a string: ')

# digits_count = count_digits(digits)
# print('No. of digits:', digits_count)


#sp 3

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# third = int(input("Enter third number: "))

# def max_of_three(first,second,third):
#     if first >= second and first >= third:
#         maximum = first
#     elif second > first and second >= third:
#         maximum = second
#     else:
#         maximum = third
#     return maximum

# maximum = max_of_three(first, second, third)
# print('Maximum:', maximum)

#sp 4

# def is_prime(max_num):
#     counter = 0
#     num = 2
#     # print('asssss')
#     while counter < max_num-1:
#         if num > 1:
#             for i in range(2,num):
#                 if num%i == 0:
#                     print(num, 'is not a prime')
#                     break
#             else:
#                 print(num, 'is a prime')
#         else:
#             print(num, 'is not a prime')
#         num += 1
#         counter += 1
#     return num

# max_num = int(input('Input an integer greater than 1: '))
# num = is_prime(max_num)

#sp 5

# def pali(input_str):
#     stuff1 = input_str.replace(' ', '')
#     stuff1 = stuff1.replace("'",'')
#     stuff1 = stuff1.replace('"','')
#     stuff1 = stuff1.replace(',','')
#     stuff1 = stuff1.replace('!','')

#     stuff2 = stuff1[::-1]
#     stuff1 = stuff1.lower()
#     stuff2 = stuff2.lower()

#     if stuff1 == stuff2:
#         print('"{}" is a palindrome.'. format(input_str))
#     else:
#         print('"{}" is not a palindrome.'. format(input_str))

# input_str = input('Enter a string: ')
# strengur = pali(input_str)

#sp 6

# def valid_date(date_str):
#     if date_str.find('.') == 1:
#         new_list = date_str.split('.')
#         if int(new_list[0]) in range(1,32):
#             if int(new_list[1]) >= 1:
#                 if int(new_list[2]) in range(0,99+1):
#                     print('Date is valid')
#         else:
#             print('Date is invalid')
#     else:
#         print('Date is invalid')

# date_str = input("Enter a date: ")
# svarid = valid_date(date_str)







def valid_date(date):
    if date[0:1].isdigit() and date[3:4].isdigit() and date[6:7].isdigit():
        if 0 < int(date[0:1]) <= 31:
            if 0 < int(date[3:4]) <= 12:
                if -1 < int(date[6:7]) <= 99:
                    if date[2] and date[5] == '.':
                        return True
    return False    

date_str = input("Enter a date: ")
if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")
