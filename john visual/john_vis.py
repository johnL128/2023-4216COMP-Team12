import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
    
    
    if graph_choice == 1:
        fig, ax = plt.subplots(graph_choice)
        ax.plot(ut.columns.T.all, ut.values.T.all, 'r')
        ax.plot(rur.columns.T.all, rur.values.T.all, 'b')
        ax.get_yaxis().get_major_formatter().set_scientific(False)
        ax.tick_params('x',labelrotation=90)
        #Set legend
        urb_leg = mpatches.Patch(color='red', label='Urban Population')
        rur_leg = mpatches.Patch(color='blue', label='Rural Population')
        ax.legend(handles=[urb_leg, rur_leg])
        
        fig.supxlabel("Years", fontsize=20)
        fig.supylabel("Population", fontsize=20)
        fig.suptitle(f"Urban and Rural Comparison for {cou_name} between {s_year}-{s_year2}", fontsize=20)
        ax.grid()
        break
    
    elif graph_choice == 2:
        fig, ax = plt.subplots(graph_choice)
        ax[0].plot(ut.columns.T, ut.values.T, 'r')
        ax[0].set_title(f"Urban Data for {cou_name}", fontsize=20)
        ax[1].plot(rur.columns.T, rur.values.T, 'b')
        ax[1].set_title(f"Rural Data for {cou_name}", fontsize=20)
        
        #format both graphs
        for i in range(graph_choice):
            ax[i].get_yaxis().get_major_formatter().set_scientific(False)
            ax[i].tick_params('x',labelrotation=90)
            ax[i].set_xlabel("Years", fontsize=20)
            ax[i].set_ylabel("Population", fontsize=20)
            ax[i].grid()
            
        fig.tight_layout()
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