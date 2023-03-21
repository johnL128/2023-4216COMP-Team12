#Compare a selected country’s urban and world population over a time period
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

w_df = pd.read_csv("csv/world.csv")
ut_df = pd.read_csv("csv/urban_total.csv")

print(f"\n--- Compare a selected country’s urban and world population over a time period ---")
print(f"\n--- Enter \'Q\' to quit the program ---")

while (True):
    sel = input("\nType in the name of a country: ")
    select_count = sel.title()
    
    if w_df["Country Name"].eq(select_count).any() and ut_df["Country Name"].eq(select_count).any():
        break
    
    elif select_count == "Q":
        exit()
    
    else:
        print(f"\nCountry doesn't exist within the database or {select_count} isn't a real country")

while (True):
    s_year = input("\nEnter a year: ")

    if s_year >="1960" and s_year <= "2020":
        break
    
    elif select_count == "Q":
        exit()
    
    else:
        print(f"\n{s_year} doesn't exist in this database!")
        
while (True):
    s_year2 = input("\nEnter another year: ")
    
    if s_year >= "1960" and s_year <= "2020":
        break
    
    elif select_count == "Q":
        exit()
    
    else:
        print(f"\n{s_year} doesn't exist in this database!")

#manipulate both csv files, get data
world = w_df.loc[w_df["Country Name"] == select_count, s_year:s_year2]
ut = ut_df.loc[ut_df["Country Name"] == select_count, s_year:s_year2]

print(f"--- World Data for {select_count} between {s_year}-{s_year2} ---")
print(world)

print(f"\n--- World Data for {select_count} between {s_year}-{s_year2} ---")
print(ut)

#plot both lines on the graph
fig, ax = plt.subplots()
line1 = ax.plot(world.columns.T, world.T, color='r')
line2 = ax.plot(ut.columns.T, ut.T, color='b')

fig.suptitle(f"Data for {select_count} between {s_year}-{s_year2}")

w_leg = mpatches.Patch(color='red', label='World Population')
ut_leg = mpatches.Patch(color='blue', label='Urban Population')
plt.legend(handles=[w_leg, ut_leg])
plt.grid()
plt.show()