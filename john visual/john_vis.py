#Compare a selected country’s urban and rural population over a time period
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

w_df = pd.read_csv("csv/world.csv")
ut_df = pd.read_csv("csv/urban_total.csv")

print(f"\n--- Compare a selected country’s urban and world population over a time period ---")
print(f"\n--- Enter \'Q\' to quit the program ---")

while (True):
    sel = input("\nEnter the Country Code: ")
    sel_code = sel.upper()
    
    if w_df["Country Code"].eq(sel_code).any() and ut_df["Country Code"].eq(sel_code).any():
        convert = w_df.loc[w_df["Country Code"] == sel_code]
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

#manipulate both csv files, get data
ut = ut_df.loc[ut_df["Country Code"] == sel_code, s_year:s_year2]
rur = w_df.loc[w_df["Country Code"] == sel_code, s_year:s_year2] - ut

print(f"\n--- Urban Data for {cou_name} between {s_year}-{s_year2} ---\n")
print(ut)
print(" ")
print(f"\n--- Rural Data for {cou_name} between {s_year}-{s_year2} ---\n")
print(rur)

#plot both lines on the graph
fig, ax = plt.subplots()
ax.plot(ut.columns.T, ut.values.T, color='r')
ax.plot(rur.columns.T, rur.values.T, color='b')

fig.suptitle(f"Urban and Rural Data for {cou_name} between {s_year}-{s_year2}", fontsize=20)
fig.supxlabel("Years", fontsize=20)
fig.supylabel("Population", fontsize=20)
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.xticks(rotation = (90))

w_leg = mpatches.Patch(color='red', label='Urban Population')
ut_leg = mpatches.Patch(color='blue', label='Rural Population')
plt.legend(handles=[w_leg, ut_leg])

plt.grid()
plt.show()