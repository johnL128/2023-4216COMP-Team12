import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("csv/world.csv")
print(data)

x = input("Now u may enter the country you would first like to see: " )
if data["Country Name"].eq(x).any():
    print(f"Ok you have chosen {x}")
else:  
    print("The country you have chosen is not in this data sheet or you have spelt it wrong, please try again:")

y = input("Can you please enter the first year you would like to view betweeen 1960-2020: " )
if y < "1960" and y > "2020":
    print("The value {y} you have entered is not within the alloted range please try again")
else:
    print(f"you hacve selected the year {y}")

z = input("Can you please enter the final year you would like to view betweeen 1960-2020: " )
if z < "1960" and z > "2020":
    print("The value {z} you have entered is not within the alloted range please try again")
else:
    print(f"you hacve selected the year {z}")

Country = data.loc[data["Country Name"] == x, y:z]
print (Country)

