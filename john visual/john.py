#Countries that have under 50% urban population in a selected year
#import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#gather selected information needed
urban_df = pd.read_csv("/Users/johnlouie/Desktop/github stuff/2022-4216COMP-Team12/csv/urban_percent.csv")

#get user input using a menu
while (True):
    select_year = input("\nEnter a year between 1960-2020: ")
    if select_year >= "1960" and select_year <= "2020":
        break
    
    else:
        print(f"\nInvalid Input: {select_year}")

#import user input into filters
show_data = urban_df.loc[urban_df[select_year] < 50]
useful = show_data[["Country Name", "Country Code", select_year]]
print(useful)

#create visualisation
#plotting
useful.plot(select_year, "Country Code", kind="scatter")

#annotating each scatter point
for idx, row in urban_df.iterrows():
    plt.annotate(row['Country Code'], (row[select_year], row["Country Code"]))

#fig settings
plt.title(f'Countries that have less than 50% urban population in {select_year}', fontsize=18)
#set xticks scale
x = np.random.randint(low=0, high=50, size=50)
plt.xticks(np.arange(0, len(x)+1, 5))
plt.xlabel("Urban % Population", fontsize=12)

plt.ylabel("")
plt.yticks([])

plt.grid()
plt.show()