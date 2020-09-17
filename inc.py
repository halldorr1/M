# def inc(num):
#     result = num + 1
#     return result

# number = int(input("Enter a number: "))
# nubmer_incremented  = inc(number)
# print(nubmer_incremented)

def func(x):
    total = 0
    for i in range(x):
        total += i * (i-1)
    return total

print(func(4))