import pandas as pd
import matplotlib.pyplot as plt

cf = pd.read_csv('csv/urban_total.csv')

print(f"\n--- Smallest urban population countries of a selected year---")

while True:
    n = input(f"\nEnter preferred year (between 1960 and 2020) or 'Q' to exit: ")
    if n.lower() == "q":
        print("Exiting the program...")
        break
    elif n < "1960" or n > "2020":
        print("Incorrect input. Please enter a year between 1960 and 2020, or 'Q' to exit.")
    else:
        print(f"Preferred year: {n}")

        # Filter the data by year and sort by urban population
        cf_year = cf[['Country Name', n]].sort_values(n)

        # Display the first 5 rows of the resulting dataframe
        print(cf_year.head(5))

        # Plot a bar chart of the urban population for the top 5 smallest countries
        cf_year[:5].plot.bar(x='Country Name', y=n, title=f"Top 5 Smallest Urban Populations in {n}")
        plt.show()
