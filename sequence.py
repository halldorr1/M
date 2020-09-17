#sp2
n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 0
n2 = 1
n3 = 2

for i in range(n):
    sum_n = n1 + n2 +n3
    n1 = n2
    n2 = n3
    n3 = sum_n
    print(n1)