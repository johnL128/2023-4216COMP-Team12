import pandas as pd
import matplotlib.pyplot as plt
r_vfp = pd.read_csv ("csv/region_world.csv") 
while (True):
     user_input = input ("What year?")   
     if user_input >= "1960" and user_input <= "2020": 
          break
     else: 
          print ("The year entered is invalid. Please enter a year between 1960 and 2020")
year2 = r_vfp.nsmallest (10, user_input)
print(year2[["Region Name", "Region Code", user_input]]) 
year2.plot(x = "Region Code", y= user_input, kind = "bar", legend = None)
plt.xlabel ("Region Code", fontsize = 12)
plt.xticks ( fontsize = 8)
plt.ylabel ("Region Population", fontsize = 12)
plt.title (f"10 Smallest Regions of {user_input}", fontsize = 14)
plt.show()