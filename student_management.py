names = []
rolls = []

while True:

    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")

        names.append(name)
        rolls.append(roll)

        print("Student Added")

    elif choice == "2":

        i = 0

        for name in names:
            print("Name :", names[i])
            print("Roll :", rolls[i])
            print()
            i = i + 1

    elif choice == "3":

        print("Thank You")
        break

    else:

        print("Invalid Choice")
