#Countries that have <50% urban population in a selected year

#import modules
import pandas as pd
import matplotlib.pyplot as plt

#gather selected information needed
urban_df = pd.read_csv("/Users/johnlouie/Desktop/github stuff/2022-4216COMP-Team12/csv/urban_percent.csv")

#get user input
while (True):
    select_year = input("\nEnter a year between 1960-2020: ")
    if select_year >= "1960" and select_year<= "2020":
        show_data = urban_df.loc[urban_df[select_year] > 50]
        useful = show_data[["Country Name", "Country Code", select_year]]
        print(useful)
        break
    else:
        print(f"\nInvalid Input: {select_year}")

#create visualisation
plt.plot(useful.head(), useful.T, 'ro')

plt.title(f'Countries that have less than 50% urban population in {select_year}', fontsize=18)
plt.xlabel("Years", fontsize=12)
plt.ylabel('Urban % Population', fontsize=12)

plt.grid()
plt.show()

#menu