#import modules/packages

#display data from csv

#main menu
while (True):
    print("-----Menu-----\nSelect one of the choices to see a visualisation:\n")
    choice = input("1 - Visual\n2 - Visual2\n3 - Visual3\n4 - Visual4\n5 - Visual5\n6 - Visual6\nQ - Quit\n\nSelect: ")
    choice = choice.upper()

    match choice:
        case "1":
            print("calls function of visual 1")
        case "2":
            print("calls function of visual 2")
        case "3":
            print("calls function of visual 3")
        case "4":
            print("calls function of visual 4")
        case "5":
            print("calls function of visual 5")
        case "6":
            print("calls function of visual 6")
        case "Q":
            print("\nThank you for using the data visualisation program, Have a nice day!\n")
            break
        case _:
            print(f"\nInvalid input:{choice}, select one of the choices provided\n")
            continue
        

#everyones individual visualisations 