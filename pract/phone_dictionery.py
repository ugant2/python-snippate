def print_menu():
    print('1. Print Ph number')
    print('2.Add Ph number')
    print('3.Remove Ph no')
    print('4. Lookup a Ph no')
    print('5. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice !=5:
    try:
        menu_choice = int(input("Type number (1-5):"))
        if menu_choice == 1:
            print("Phone Number:")
            for x in numbers.keys():
                print("Name: ", x, "\tNumber", numbers[x])
            print()
        elif menu_choice == 2:
            print("Add Name and Number")
            name = input("Name: ")
            phone = input("Phone: ")
            numbers[name] == name
        elif menu_choice == 3:
            print("Remove name and number")
            name = input("Name: ")
            if name in numbers:
                del numbers[name]
            else:
                print(name, "Not found")
        elif menu_choice == 4:
            print("look up Number")
            name = input("Name: ")
            if name in numbers:
                print("The number is", numbers[name])
            else:
                print(name,"not found")
        elif menu_choice !=5:
            print_menu()
    except ValueError:
        print("no a number.")
