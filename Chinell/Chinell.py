import pandas as pd
import matplotlib.pyplot as plt

cf = pd.read_csv('csv/urban_total.csv')

print(f"\n--- Smallest urban population countries of a selected year---")

while True:
    print("\n1. Enter a year (between 1960 and 2020) to view top 5 smallest urban populations")
    print("2. Exit the program")
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            n = input("Enter preferred year (between 1960 and 2020) or 'Q' to go back to the main menu: ")
            if n.lower() == "q":
                break

            elif n < "1960" or n > "2020":
                print("Incorrect input. Please enter a year between 1960 and 2020, or 'Q' to go back to the main menu.")
            else:
                print(f"Preferred year: {n}")

                # Filter the data by year and sort by urban population
                cf_year = cf[['Country Name', n]].sort_values(n)

                # Display the first 5 rows of the resulting dataframe
                print(cf_year.head(5))

                # Ask the user which type of chart to plot
                chart_type = input("Enter 'bar' or 'pie' to plot a bar chart or a pie chart respectively: ")

                if chart_type == "bar":
                    # Plot a coloured bar chart of the urban population for the top 5 smallest countries
                    plt.figure(figsize=(8, 6))
                    plt.title(f"Top 5 Smallest Urban Populations in {n}", fontsize=16)
                    plt.bar(cf_year[:5]['Country Name'], cf_year[:5][n], color=['red', 'orange', 'yellow', 'green', 'blue'])
                    plt.xlabel("Country", fontsize=14)
                    plt.ylabel("Urban Population", fontsize=14)

                elif chart_type == "pie":
                    # Plot a coloured pie chart of the urban population for the top 5 smallest countries
                    plt.figure(figsize=(8, 6))
                    plt.title(f"Top 5 Smallest Urban Populations in {n}", fontsize=16)
                    plt.pie(cf_year[:5][n], labels=cf_year[:5]['Country Name'], colors=['red', 'orange', 'yellow', 'green', 'blue'], autopct='%1.1f%%', startangle=90)

                else:
                    print("Incorrect input. Please enter 'bar' or 'pie'.")

                plt.show()

    elif choice == "2":
        print("Exiting the program...")
        break
    else:
        print("Incorrect input. Please enter 1 or 2.")
