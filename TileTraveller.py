""" user_input = input("Yo put some fucking input") """

array = [1,1]

while array != [3,1]:
    if array == [1,1]:
        print("You can travel: (N)orth.")
        user_inp = input("Direction: ").lower()

        if user_inp == 'n':
            array = [1,2]
            
        else:
            print('Not a valid direction!')
    elif array == [1,2]:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        user_inp = input('Direction: ').lower()
        
        if user_inp == 'n':
            array = [1,3]
            
        elif user_inp == 's':
            array = [1,1]
            
        elif user_inp == 'e':
            array = [2,2]
            
        else:
            print('Not a valid direction!')
            
    elif array == [2,2]:
        print('You can travel: (S)outh or (W)est.')
        user_inp = input('Direction: ').lower()

        if user_inp == 's':
            array = [2,1]
            
        elif user_inp == 'w':
            array = [1,2]
            
        else:
            print('Not a valid direction!')
    
    elif array == [2,1]:
        print('You can travel: (N)orth.')
        user_inp = input('Direction: ').lower()

        if user_inp == 'n':
            array = [2,2]
            

    elif array == [1,3]:
        print('You can travel: (E)ast or (S)outh.')
        user_inp = input('Direction: ').lower()

        if user_inp == 'e':
            array = [2,3]
            
        elif user_inp == 's':
            array = [1,2]
            
        else:
            print('Not a valid direction!')

    elif array == [2,3]:
        print('You can travel: (E)ast or (W)est.')
        user_inp = input('Direction: ').lower()

        if user_inp == 'e':
            array = [3,3]
            
        elif user_inp == 'w':
            array = [1,3]
            
        else:
            print('Not a valid direction!')

    elif array == [3,3]:
        print('You can travel: (S)outh or (W)est.')
        user_inp = input('Direction: ').lower()

        if user_inp == 's':
            array = [3,2]
            
        elif user_inp == 'w':
            array = [2,3]
            
        else:
            print('Not a valid direction!')

    elif array == [3,2]:
        print('You can travel: (N)orth or (S)outh.')
        user_inp = input('Direction: ').lower()

        if user_inp == 'n':
            array = [3,3]
            
        elif user_inp == 's':
            array = [3,1]
            
        else:
            print('Not a valid direction!')
print('Victory!')


       
    
        
    

