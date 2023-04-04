import pandas as pd 
import matplotlib.pyplot as plt
r_vfp = pd.read_csv ("csv/region_world.csv") 
user_input = input ("What year?")   
year2 = r_vfp.nsmallest (10, user_input)
print(year2[["Region Name", "Region Code", user_input]])