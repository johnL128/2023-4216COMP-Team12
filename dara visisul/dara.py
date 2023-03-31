#Compare a selected country ‘s total population between years
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("csv/world.csv")
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
plt.ylabel("Population",fontdict = font1)
plt.title(f"{x},{y} - {z} Population",fontdict = font2)
plt.grid()
plt.show()

