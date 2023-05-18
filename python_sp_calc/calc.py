import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

def graph(employee, covid):
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/mariusaffolter/Documents/GitHub/sp_project_janosh_marius/backend_sp_db/Database/project_SP.db')

    # Read data from tables using pandas
    rows1 = pd.read_sql_query("SELECT * FROM Covid_Data", conn)
    rows2 = pd.read_sql_query("SELECT * FROM SP_Project_Sums", conn)

    # Close the database connection
    conn.close()

    # Store the values in separate lists
    dates = rows1['date']  # Assuming the date column is named 'date' in the Covid_Data table
    employee_list = rows2.iloc[:, employee]
    covid_list = rows1.iloc[:, covid]

    # Create a line graph using Matplotlib with dual y-axes
    fig, ax1 = plt.subplots()

    ax1.plot(dates, employee_list, 'bo-', label='Employees')
    ax1.set_xlabel('Dates')
    ax1.set_ylabel('Employees', color='b')

    ax2 = ax1.twinx()  # Create a secondary y-axis
    ax2.plot(dates, covid_list, 'ro-', label='COVID')
    ax2.set_ylabel('COVID', color='r')

    # Set title and legends
    plt.title('COVID and Employees Over Time')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

graph(6,1)
