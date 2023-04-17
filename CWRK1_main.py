import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#display data from csv (ensure that import has csv/"file name")

#EVERYONE'S VISUALISATION BELOW
#Chinells's Visualisation

def smallestPop():
    import pandas as pd
    import matplotlib.pyplot as plt

    cf = pd.read_csv('csv/urban_total.csv')

    print(f"\n--- Smallest urban population countries of a selected year---")

    while True:
        print("\n1. Enter a year (between 1960 and 2020) to view top 5 smallest urban populations")
        print("2. Exit the program")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                n = input("Enter preferred year (between 1960 and 2020) or 'Q' to go back to the main menu: ")
                if n.lower() == "q":
                    break

                elif n < "1960" or n > "2020":
                    print("Incorrect input. Please enter a year between 1960 and 2020, or 'Q' to go back to the main menu.")
                else:
                    print(f"Preferred year: {n}")

                    # Filter the data by year and sort by urban population
                    cf_year = cf[['Country Name', n]].sort_values(n)

                    # Display the first 5 rows of the resulting dataframe
                    print(cf_year.head(5))

                    # Ask the user which type of chart to plot
                    chart_type = input("Enter 'bar' or 'pie' to plot a bar chart or a pie chart respectively: ")

                    if chart_type == "bar":
                        # Plot a coloured bar chart of the urban population for the top 5 smallest countries
                        plt.figure(figsize=(8, 6))
                        plt.title(f"Top 5 Smallest Urban Populations in {n}", fontsize=16)
                        plt.bar(cf_year[:5]['Country Name'], cf_year[:5][n], color=['red', 'orange', 'yellow', 'green', 'blue'])
                        plt.xlabel("Country", fontsize=14)
                        plt.ylabel("Urban Population", fontsize=14)

                    elif chart_type == "pie":
                        # Plot a coloured pie chart of the urban population for the top 5 smallest countries
                        plt.figure(figsize=(8, 6))
                        plt.title(f"Top 5 Smallest Urban Populations in {n}", fontsize=16)
                        plt.pie(cf_year[:5][n], labels=cf_year[:5]['Country Name'], colors=['red', 'orange', 'yellow', 'green', 'blue'], autopct='%1.1f%%', startangle=90)

                    else:
                        print("Incorrect input. Please enter 'bar' or 'pie'.")

                    plt.show()

        elif choice == "2":
            print("Exiting the program...")
            break
        else:
            print("Incorrect input. Please enter 1 or 2.")








#Dara's Visualisation
def urbanPercentTime():
    #Compare a selected country ‘s total population between years
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv("csv/urban_percent.csv")
    print(data)

    while(True):
        x = input("Now u may enter the country you would first like to see: " )
        if data["Country Name"].eq(x).any():
            print(f"Ok you have chosen {x}")
            break
        else:  
            print("The country you have chosen is not in this data sheet or you have spelt it wrong, please try again:")

    while(True):
        y = input("Can you please enter the first year you would like to view betweeen 1960-2020: " )
        if y >= "1960" and y <= "2020":
            print(f"you hacve selected the year {y}")
            break
        else:
            print(f"The value {y} you have entered is not within the alloted range please try again")

    while(True):
        z = input("Can you please enter the second year you would like to view betweeen 1960-2020: " )
        if z >= "1960" and z <= "2020":
            print(f"you hacve selected the year {z}")
            break
        else:
            print(f"The value {z} you have entered is not within the alloted range please try again")

    Country = data.loc[data["Country Name"] == x, y:z]
    print (Country)

    #need x and y axis- titles
    #need main title
    #get rid of 1e9 part
    ##chaneg font size and make em smaller
    fig, ax = plt.subplots()
    plt.plot(Country.columns.T, Country.values.T, 'r+',)
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    plt.xticks(rotation = (90))

    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    plt.xlabel("Year",fontdict = font1)
    plt.ylabel("Urban%",fontdict = font1)
    plt.title(f"{x},{y} - {z} Urban% population",fontdict = font2)
    plt.grid()
    plt.show()










#Adina's Visualisation
def rpopulatio():
    
    r_vfp = pd.read_csv ("csv/region_world.csv") 
    while (True):
        user_input = input ("What year?")   
        if user_input >= "1960" and user_input <= "2020": 
            break
        else: 
            print ("The year entered is invalid. Please enter a year between 1960 and 2020")
    year2 = r_vfp.nsmallest (10, user_input)
    print(year2[["Region Name", "Region Code", user_input]]) 

    while (True):
        print("Chose what graph you would like to view the data with:")
        #allow user to select a program
        choice = input("1 - Scatter Graph \n2 - Pie Graph \n3 - Bar Chart\nselect: ")
        choice = choice.upper()

        if choice == "1": 
            print(f"\n\nYou have selected option {choice}\n")
            year2.plot(x = "Region Code", y= user_input, kind = "scatter", legend = None)
            plt.xlabel ("Region Code", fontsize = 12)
            plt.xticks ( fontsize = 8)
            plt.ylabel ("Region Population", fontsize = 12)
            break
            
        elif choice ==  "2":
            print(f"\n\nYou have selected option {choice}\n")
            plt.figure(figsize=(8,6))
            plt.pie(year2 [:10][user_input], labels=year2 ['Region Name'], colors=['red', 'pink', 'yellow', 'blue', 'green', 'black', 'purple', 'orange', 'turquoise', 'indigo'])
            break
            
            
        elif choice ==  "3":
            print(f"\n\nYou have selected option {choice}\n")
            year2.plot(x = "Region Code", y= user_input, kind = "bar", legend = None)
            plt.xlabel ("Region Code", fontsize = 12)
            plt.xticks ( fontsize = 8)
            plt.ylabel ("Region Population", fontsize = 12)
            break
        
        else:
            print("Error")
        
    plt.title (f"10 Smallest Regions of {user_input}", fontsize = 14)
    plt.show()









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
#Countries with the biggest total population in a selected year
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv ("csv/world.csv")
print (f"\n---Countries with the biggest population in a selected year---")

while (True):
    n = input(f"\n Enter a year between 1960 and 2020 and view the top 10 countries with the biggest total population")
    if n <= "2020" and n >="1960":
        break
    else:
        print("Error Message")

#pandas manipulation
var = df.nlargest(10,n)

print(var[["Country Name", "Country Code", n]])


var.plot(x="Country Code", y=n, kind='bar')

plt.xlabel ("Country Code ", fontsize =20) 

plt.xticks (fontsize = 8)

plt.title(f"Countries with the biggest population in {n}", fontsize = 20)

plt.show()










#John's Visualisation
def compareUrbanRural():
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    ut_df = pd.read_csv("csv/urban_total.csv")
    w_df = pd.read_csv("csv/world.csv")

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

    #GATHER DATA, SET PARAMETERS TO AVOID NaN VALUES
    wrl = w_df.loc[w_df["Country Code"] == sel_code, s_year:s_year2]
    ut = ut_df.loc[ut_df["Country Code"] == sel_code, s_year:s_year2]
    wrl.reset_index(drop=True, inplace=True)
    ut.reset_index(drop=True, inplace=True)
    rur = wrl - ut

    while (True):
        try:
            print("\nSelect a visualisation option:")
            graph_choice = int(input("\n1 - Compare Urban and Rural\n2 - Urban and Rural Population ONLY\n\nChoice: "))
        
        except ValueError as ve:
            print(f"\nInvalid choice, it must be a NUMBER!")
            continue
        
        
        if graph_choice == 1:
            fig, ax = plt.subplots(graph_choice)
            ax.plot(ut.columns.T, ut.values.T, 'r')
            ax.plot(rur.columns.T, rur.values.T, 'b')
            #removes scientific values and uses "large numbers" instead
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            ax.tick_params('x',labelrotation=90)
            fig.supxlabel("Years", fontsize=20)
            fig.supylabel("Population", fontsize=20)
            fig.suptitle(f"Urban and Rural Comparison for {cou_name} between {s_year}-{s_year2}", fontsize=20)
            
            #Set legend
            urb_leg = mpatches.Patch(color='red', label='Urban Population')
            rur_leg = mpatches.Patch(color='blue', label='Rural Population')
            ax.legend(handles=[urb_leg, rur_leg])
            break
        
        elif graph_choice == 2:
            fig, ax = plt.subplots(graph_choice)
            ax[0].set_title(f"Urban Data for {cou_name} between {s_year}-{s_year2}", fontsize=18)
            ax[0].scatter(x = ut.columns.T, y = ut.values.T, marker = 'x', c = '#FF0000')
            ax[1].set_title(f"Rural Data for {cou_name} between {s_year}-{s_year2}", fontsize=18)   
            ax[1].scatter(x = rur.columns.T, y = rur.values.T, marker = 'x', c = '#0000FF')
            
            #format both graphs
            for i in range(graph_choice):
                ax[i].get_yaxis().get_major_formatter().set_scientific(False)
                ax[i].tick_params('x',labelrotation=90)
                ax[i].set_xlabel("Years", fontsize=18)
                ax[i].set_ylabel("Population", fontsize=18)
                ax[i].grid()
                
            plt.tight_layout()
            break
        
        else: 
            print(f"\n\'{graph_choice}\' is not an option, please select from the above")

    #Show Dataframe and visualisation
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
    choice = input("1 - Smallest urban population countries of a selected year\n2 - Compare a selected country \'s total population between years\n3 - Smallest Regions total population \n4 - Compare two countries total population over a time period.\n5 - Countries with the Biggest Total Population in a selected year\n6 - Compare a selected country\'s urban/rural population over a selected time period\nQ - Quit\n\nSelect an option from the above options: ")
    choice = choice.upper()

    if choice == "1":
        print(f"\n\nYou have selected option{choice}\n")
        smallestPop()
        
    elif choice ==  "2":
        print(f"\n\nYou have selected option{choice}\n")
        urbanPercentTime()
        
    elif choice ==  "3":
        print(f"\n\nYou have selected option{choice}\n")
        rpopulatio()
        
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