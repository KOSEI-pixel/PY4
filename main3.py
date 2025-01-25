print("select a ride:-")
print("1. bike\n")
print("2. car\n")

choice = int(input("enter your choice:- "))
if choice == 1:
    print("which type of bike")
    print('1. BMX\n')
    print('2. scooter\n')

    choice2 = int(input("enter your choice:- "))
    if choice2 == 1:
        print("you selected BMX")
    elif choice2 == 2:
        print("you selected scooter")
    else:
        print("invalid choice!")
elif choice == 2:
    print("which type of car")
    print("1. sedan\n")
    print("2. SUV\n")

    choice3 = int(input("enter your choice:- "))
    if choice3 == 1:
        print("you selected sedan")
    elif choice3 == 2:
        print("you selected SUV")
    else:
        print("invalid choice!")
else:
    print("invalid choice!")






