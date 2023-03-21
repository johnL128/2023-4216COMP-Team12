#Compare a selected country’s urban and world population over the whole time span
import pandas as pd
import matplotlib.pyplot as plt

w_df = pd.read_csv("csv/world.csv")
ut_df = pd.read_csv("csv/urban_total.csv")

while (True):
    select_count = input("\nType in the name of a country: ")
    
    if w_df["Country Name"].eq(select_count).any() and ut_df["Country Name"].eq(select_count).any():
        break
    
    else:
        print(f"\nCountry doesn't exist within the database or {select_count} isn't a real country")

#manipulate both csv files, get data

#plot both lines on the graph