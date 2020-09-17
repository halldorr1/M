#project 2

while True:
    print("Welcome to car rentals!")
    yorn = input("Would you like to continue (y/n)?")

    if yorn == "y":
        bord = input("Customer code (b or d): ")
        num = int(input("Number of days: "))
        odoS = int(input("Odometer reading at the start: "))
        odoE = int(input("Odometer reading at the end: "))
        miles = int(odoE - odoS)
        #miles2 = int(miles - 100)
        print("Miles driven:" , miles)
        if bord == 'b':
            charge = round((40 * num) + (0.25 * miles), 1)
        else:
            charge = round((60 * num) + (0.25 * (miles / 3)), 1)
        print("Amount due: " ,charge)