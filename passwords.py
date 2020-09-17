guess = str(input("Enter a new password: "))
counter = 0
counter4 = 0
guess_inv = 0
while guess != 'q':

    if len(guess) >= 6 and len(guess) <= 20:
        counter1 = 0
        counter2 = 0
        counter3 = 0
        for i in guess:
            if i.islower():
                counter1 += 1
            elif i.isupper():
                counter2 += 1
            elif i.isdigit():
                counter3 += 1
        if counter1 > 0 and counter2 > 0 and counter3 > 0:
            print('Valid password of length', len(guess))
            counter4 += 1
        elif counter1 > 0 and counter2 > 0:
            print('At least one number needed')
        elif counter1 > 0 and counter3 > 0:
            print('At least one upper case letter needed')
        elif counter2 > 0 and counter3 > 0:
            print('At least one lower case letter needed')
        elif counter1 > 0:
            print('At least one upper case letter needed')
            print('At least one number needed')
        elif counter2 > 0:
            print('At least one lower case letter needed')
            print('At least one number needed')
        elif counter3 > 0:
            print('At least one lower case letter needed')
            print('At least one upper case letter needed')
        else:
            print('At least one lower case letter needed')
            print('At least one upper case letter needed')
            print('At least one number needed')
    else:
        print('Invalid length')
    counter += 1
    guess = str(input("Enter a new password: "))
    guess_inv = counter - counter4
print('You tried {} passwords, {} valid, {} invalid'.format(counter,counter4,guess_inv))

