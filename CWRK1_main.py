import pandas as pd

#display data from csv
df = pd.read_csv("")

#EVERYONE'S VISUALISATION

#main menu
#for some reason python 3.9 doesnt have a switch case option, needs python 3.10
while (True):
    print("-----Menu-----\nSelect one of the choices to see a visualisation:\n")
    choice = input("1 - Visual\n2 - Visual2\n3 - Visual3\n4 - Visual4\n5 - Visual5\n6 - Visual6\nQ - Quit\n\nSelect: ")
    choice = choice.upper()

    if choice == "1":
        print("calls function of visual 1")
        
    elif choice ==  "2":
        print("calls function of visual 2")
        
    elif choice ==  "3":
        print("calls function of visual 3")
        
    elif choice ==  "4":
        print("calls function of visual 4")
        
    elif choice ==  "5":
        print("calls function of visual 5")
        
    elif choice ==  "6":
        print("calls function of visual 6")
        
    elif choice ==  "Q":
        print("\nThank you for using the data visualisation program, Have a nice day!\n")
        exit()
        
    else:
        print(f"\nInvalid input:{choice}, select one of the choices provided\n")
        continue