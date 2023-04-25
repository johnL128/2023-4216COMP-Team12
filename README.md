# Computer Science Workshop: 2023-4216COMP-Team12
**Project: Data Visualisation of Urban/World Populations**

## Menu
When the program is run, the user is greeted with a menu in which they will be given a select number of choices to choose from.
To access each individual visualisation, the user will need to select a number to execute any of the desired visualisations provided by the authors within this project.

## Visualisation Descriptions

Each visualisation is listed in chronological order, according to the menu provided in the program (1-6):

| Menu Option | Option Description  | Author |
|----|------------- | ------------- |
|1| 5 Smallest urban population countries of a selected year  | **Chinell** |
|2| Compare a selected country's Urban Percentage total population between years  | **Dara** |
|3| 5 Smallest regions (total population) | **Adina** |
|4| Compare two countries total population over a time period | **Adun** |
|5| Countries with the Biggest Total Population in a selected year | **Ella** |
|6| Compare a selected country\'s urban/rural population over a selected time period | **John** |

### Chinell
The programme reads a CSV file containing urban population data and uses pandas to filter and sort the data. My fraction of the programme is to prompt the user to select a year between 1960 and 2020 and display the top 5 smallest urban populations for the selected year. The program sorts the data and displays the results in a table. The user can also visualise the data using a bar or pie chart. Finally, the program allows the user to exit or go back to the main menu.

### Dara
The user will be asked to pick a country that is in the list and after they will pick the two years they would like to comapre and once they do that the data is collected and then hence plotted on a scatter graph allowing the user to see an increase or decreas in poulation and in what specific time zone.

### Adina
The program that i have build works by asking the user to input a year of choice and what graph they want to use to analize the data view, they can chose between a Scatter Graph a Pie Graph and a Bar Char and it will show the 10 regions with the smallest population in the year selected with the graph selected. 

### Adun
The User will be given the option of choosing two countries, and if the countries are in the database, the user will then proceed to choosing a time period which the program will make a line graph explaining the data.

### Ella
The user will be asked to pick a year of their choice between 1960-2020 and it will show the data on a bar chart with the 10 countries with the biggest population in that selected year. 

### John
When the user accesses my section of the program, a number of questions will be asked in order to filter according to the requirements of the user. This will begin with asking for the country code, then asking for a beginning and end year **(1960-2020)** in order to take the neccessary data needed to plot. The program will then ask for a type of visualisation, either displaying seperate scatter graphs showing urban and rural individually, or a comparison line graph. The terminal will then print a statement providing the user with the data they requested for alongside the visualisation(s).
