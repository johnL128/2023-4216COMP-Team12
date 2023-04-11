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

while (True):
    print("Chose what graph you would like to view the data with:")
    #allow user to select a program
    choice = input("1 - scatter Graph \n2 - Pie Graph \n3 - Bar Chart\nselect: ")
    choice = choice.upper()

    if choice == "1": 
        print(f"\n\nYou have selected option {choice}\n")
        year2.plot(x = "Region Code", y= user_input, kind = "scatter", legend = None)
        plt.xlabel ("Region Code", fontsize = 12)
        plt.xticks ( fontsize = 8)
        plt.ylabel ("Region Population", fontsize = 12)
        break
        
    elif choice ==  "2":
        print(f"\n\nYou have selected option {choice}\n")
        plt.figure(figsize=(8,6))
        plt.pie(year2 [:10][user_input], labels=year2 ['Region Name'], colors=['red', 'pink', 'yellow', 'blue', 'green', 'black', 'purple', 'orange', 'turquoise', 'indigo'])
        break
        
        
    elif choice ==  "3":
        print(f"\n\nYou have selected option {choice}\n")
        year2.plot(x = "Region Code", y= user_input, kind = "bar", legend = None)
        plt.xlabel ("Region Code", fontsize = 12)
        plt.xticks ( fontsize = 8)
        plt.ylabel ("Region Population", fontsize = 12)
        break
    
    else:
        print("Error")
       
plt.title (f"10 Smallest Regions of {user_input}", fontsize = 14)
plt.show()