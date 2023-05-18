import sqlite3
import matplotlib.pyplot as plt

def graph(employee, covid):
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/mariusaffolter/Documents/GitHub/sp_project_janosh_marius/backend_sp_db/Database/project_SP.db')
    cursor = conn.cursor()

    # Execute a SELECT query to fetch data from a table
    cursor.execute(f"SELECT * FROM Combined_Data")
    rows1 = cursor.fetchall()

    cursor.execute(f"SELECT * FROM SP_Project_Sums")
    rows2 = cursor.fetchall()
    
    # Store the values in a list
    employee_list = []
    covid_list = []
    
    # Close the database connection
    conn.close()

    # Extract x and y values from the data
    x_values = [row[employee] for row in employee_list]  # Assuming x values are in the first column
    y_values = [row[covid] for row in covid_list]  # Assuming y values are in the second column

    # Create a line graph using Matplotlib
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('COVIDxEMPLOYEES')
    plt.show()

graph(2, 2)