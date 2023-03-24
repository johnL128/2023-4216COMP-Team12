import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/world.csv')
print(df)

print(f"\n Compare two countries total population over a time period.")
print(f"\n Choose 'Q' to quit the program")
 
while (True):
    n = input(f"\n Enter chosen country name: ")
    if df["Country Name"].eq(n).any():
        print(f"1st Chosen county: {n}")
        break
    else:
        print("Please choose another country")

while(True):
    o = input(f"\n Enter chosen country name: ")
    if df["Country Name"].eq(o).any():
        print(f"2nd Chosen Country: {o}")
        break
    elif o == n:
        print("THIS COUNTRY HAS ALREADY BEEN SELECTED!")

    else:
        print("Please choose another country")

while(True):
    x = input(f"\n Choose a year: ")
    if x >= "1960" and x <= "2020":
        print(f"1st Chosen year: {x}")
        break
    else:
        print(f"This year is not valid. Choose another year.")

while (True):
    y = input(f"\n Choose a year: ")
    if y >= "1960" and y <= "2020":
        print(f"2nd Chosen year: {y} ")
        break
    else: 
        print(f"This year is not valid. Choose another year.")

a = df.loc[df[f"Country Name"] == n, x:y]
b = df.loc[df[f"Country Name"] == o, x:y]
print(a)
print(b)

fig, ax = plt.subplots()
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.plot(a.columns.T, a.T)
ax.plot(b.columns.T, b.T)

fig.suptitle(f"Total Population for {n} and {o} between {x} and {y}", fontsize = 20)
ax.set_xlabel("Years", fontsize = 14)
ax.set_ylabel("Population", fontsize = 14)

ax.xaxis.grid()
ax.yaxis.grid()

plt.show()
