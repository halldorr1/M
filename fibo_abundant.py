faorb = input("Input f|a|b (fibonacci, abundant or both): ",)

if faorb == 'f' or faorb == 'b':
    length_f = int(input("Input the length of the sequence: ")) # Do not change this line
    print('Fibonacci Sequence:')
    print('-------------------')
    num_1 = 0
    num_2 = 1
    print(0)
    for i in range(length_f-1):
        sum_n = num_1 + num_2
        num_1 = num_2
        num_2 = sum_n
        print(num_1)

if faorb == 'a' or faorb == 'b':
    max_num = int(input("Input the max number to check: "))

    print('Abundant numbers:')
    print('-----------------')
    summan = 0
    for i in range(1,max_num+1): 
        for j in range(1,i):
            if i % j == 0:
                summan = summan + j 
        if summan > i:
            print(i)
        summan = 0