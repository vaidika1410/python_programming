# ask the user to select a day number from 1 to 7, and print the corresponding day of the week

day = int(input("enter day number from 1 to 7:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")