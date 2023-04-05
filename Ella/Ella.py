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
plt.xlabel ("Country ", fontsize =12) 
plt.xticks (fontsize = 8)
plt.title(f"Countries with the biggest population in {n}", fontsize = 20)
plt.show()
