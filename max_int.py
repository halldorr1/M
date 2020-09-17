#sp1

list1 =[]
while True:
    x = num_int = int(input("Input a number: "))
    list1.append(x)
    if x <= 0:
        break
max_int = max(list1)
print("The maximum is", max_int)







