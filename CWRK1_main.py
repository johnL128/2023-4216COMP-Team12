import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#display data from csv (ensure that import has csv/"file name")

#EVERYONE'S VISUALISATION BELOW
#Chinells's Visualisation









#Dara's Visualisation









#Adina's Visualisation










#Adun's Visualisation
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



#Ella's Visualisation










#John's Visualisation
def compareUrbanRural():
    w_df = pd.read_csv("csv/world.csv")
    ut_df = pd.read_csv("csv/urban_total.csv")

    print(f"\n--- Compare a selected country\'s urban/rural population over a selected time period ---")
    print(f"\n--- Enter \'Q\' to quit the program ---")

    while (True):
        sel = input("\nEnter the Country Code: ")
        sel_code = sel.upper()
        
        if w_df["Country Code"].eq(sel_code).any() and ut_df["Country Code"].eq(sel_code).any():
            convert = w_df.loc[w_df["Country Code"] == sel_code]
            #converts the code into the name of the country
            cou_name = convert["Country Name"].values[0]
            break
        
        elif sel_code == "Q":
            exit()
        
        else:
            print(f"\nCountry Code doesn't exist within the database/\"{sel_code}\" isn't a real country")

    while (True):
        s_year = input("\nEnter a beginning year: ")

        if s_year >="1960" and s_year <= "2020":
            break
        
        else:
            print(f"\n{s_year} doesn't exist in this database!")
            
    while (True):
        s_year2 = input("\nEnter another year: ")
        
        if s_year >= "1960" and s_year <= "2020" and s_year2 != s_year and s_year2 > s_year:
            break
            
        else:
            print(f"\n{s_year} doesn't exist in this database!")


    #GATHER DATA
    ut = ut_df.loc[ut_df["Country Code"] == sel_code, s_year:s_year2]
    rur = w_df.loc[w_df["Country Code"] == sel_code, s_year:s_year2] - ut

    while (True):
        try:
            print("\nSelect a visualisation option:")
            graph_choice = int(input("\n1 - Compare Urban and Rural\n2 - Urban and Rural Population ONLY\nChoice: "))
        
        except ValueError as ve:
            print(f"\nInvalid choice, it must be a NUMBER!")
            continue
        
        fig, ax = plt.subplots(graph_choice)
        fig.suptitle(f"Urban and Rural Data for {cou_name} between {s_year}-{s_year2}", fontsize=20)
        fig.supxlabel("Years", fontsize=20)
        fig.supylabel("Population", fontsize=20)
        urb_leg = mpatches.Patch(color='red', label='Urban Population')
        rur_leg = mpatches.Patch(color='blue', label='Rural Population')
        
        if graph_choice == 1:
            ax.plot(ut.columns.T, ut.values.T, color='r')
            ax.plot(rur.columns.T, rur.values.T, color='b')
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            ax.tick_params('x',labelrotation=90)
            ax.legend(handles=[urb_leg, rur_leg])
            ax.grid()
            break
        
        elif graph_choice == 2:
            ax[0].plot(ut.columns.T, ut.values.T, color='r')
            ax[1].plot(rur.columns.T, rur.values.T, color='b')
            
            #format both graphs
            for i in range(graph_choice):
                ax[i].get_yaxis().get_major_formatter().set_scientific(False)
                ax[i].tick_params('x',labelrotation=90)
                ax[i].grid()
            
            #seperate legends for each graph (different values)
            ax[0].plot(ut.columns.T, ut.values.T, color='r')
            ax[0].legend(handles=[urb_leg])
            
            ax[1].plot(rur.columns.T, rur.values.T, color='b')
            ax[1].legend(handles=[rur_leg])
            break

    print(f"\n--- Urban Data for {cou_name} between {s_year}-{s_year2} ---\n")
    print(ut)
    print("")
    print(f"\n--- Rural Data for {cou_name} between {s_year}-{s_year2} ---\n")
    print(rur)
    plt.show()











#main menu
#for some reason python 3.9 doesnt have a switch case option, needs python 3.10
while (True):
    print("\n----- DATA VISUALISATION OF GLOBAL POPULATION (URBAN/RURAL/TOTAL) -----\n\n--------------------------------- MENU --------------------------------\n")
    #allow user to select a program
    choice = input("1 - Smallest urban population countries of a selected year\n2 - Compare a selected country \'s total population between years\n3 - Smallest total population Countries\n4 - Compare two countries total population over a time period.\n5 - Countries with the Biggest Total Population in a selected year\n6 - Compare a selected country\'s urban/rural population over a selected time period\nQ - Quit\n\nSelect an option from the above options: ")
    choice = choice.upper()

    if choice == "1":
        print(f"\n\nYou have selected option{choice}\n")
        #Add visualisation function here
        
    elif choice ==  "2":
        print(f"\n\nYou have selected option{choice}\n")
        #Add visualisation function here
        
    elif choice ==  "3":
        print(f"\n\nYou have selected option{choice}\n")
        #Add visualisation function here
        
    elif choice ==  "4":
        print(f"\n\nYou have selected option{choice}\n")
        comparingCountries()
        
    elif choice ==  "5":
        print(f"You have selected option{choice}")
        print("calls function of visual 5")
        
    elif choice ==  "6":
        print(f"You have selected option{choice}")
        compareUrbanRural()
        
    elif choice ==  "Q":
        print("\nThank you for using the data visualisation program, Have a nice day!\n")
        exit()
        
    else:
        print(f"\nInvalid input: \'{choice}\', select one of the choices provided\n")