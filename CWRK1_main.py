import pandas as pd
import matplotlib.pyplot as plt

#display data from csv (ensure that import has csv/"file name")

#EVERYONE'S VISUALISATION
def comparingCountries():

    df = pd.read_csv('csv/world.csv')
    print(df)

    print(f"\n Compare two countries total population over a time period.")
    print(f"\n Choose 'Q' to quit the program")
    
    while (True):
        n = input(f"\n Enter chosen country name: ") #the user picks a county of their choice
        if df["Country Name"].eq(n).any():
            print(f"1st Chosen county: {n}")
            break
        elif n == 'Q':
            exit()
        else:
            print("Please choose another country") #if the way the user wrote the country name is not accepted, the user has to write the code again

    while(True):
        o = input(f"\n Enter chosen country name: ") #the user enters a second country name
        if df["Country Name"].eq(o).any():
            print(f"2nd Chosen Country: {o}") 
            break
        elif o == n:
            print("THIS COUNTRY HAS ALREADY BEEN SELECTED!") #if the country the code chose has already been selected before

        else:
            print("Please choose another country")

    while(True):
        x = input(f"\n Choose a year: ") #the user has to choose the year they want the code to read from
        if x >= "1960" and x <= "2020":
            print(f"1st Chosen year: {x}")
            break
        else:
            print(f"This year is not valid. Choose another year.") #if the year the user chooses, is not in the time period of the code

    while (True):
        y = input(f"\n Choose a year: ") #the user chooses another year
        if y >= "1960" and y <= "2020":
            print(f"2nd Chosen year: {y} ")
            break
        else: 
            print(f"This year is not valid. Choose another year.")

    a = df.loc[df[f"Country Name"] == n, x:y] #plots the information for the country name and the year
    b = df.loc[df[f"Country Name"] == o, x:y]
    print(a)
    print(b)

    fig, ax = plt.subplots() #plots the data entered by the user on the graph
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.plot(a.columns.T, a.values.T, label = n, color = 'black') #changes the color of the line plotted for the graph to black
    ax.plot(b.columns.T, b.values.T, label = o, color = 'red')

    fig.suptitle(f"Total Population for {n} and {o} between {x} and {y}", fontsize = 20) # displays the title of the graph with the two countries and the two years
    ax.set_xlabel("Years", fontsize = 14)
    ax.set_ylabel("Population", fontsize = 14)

    ax.xaxis.grid()
    ax.yaxis.grid()

    ax.legend(loc="upper right") # puts the legend of the graph at the upper right of the graph

    plt.show()


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
        comparingCountries()
        break
        
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