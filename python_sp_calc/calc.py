import sqlite3
import matplotlib.pyplot as plt

def graph(table, datbase):
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/mariusaffolter/Documents/GitHub/sp_project_janosh_marius/backend_sp_db/Database/project_SP.db')
    cursor = conn.cursor()

    # Execute a SELECT query to fetch data from a table
    cursor.execute(f"SELECT {table} FROM {datbase}")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Store the values in a list
    data_list = []
    for row in rows:
        data_list.append(row)

    # Close the database connection
    conn.close()

    # Extract x and y values from the data
    x_values = [row[0] for row in data_list]  # Assuming x values are in the first column
    y_values = [row[1] for row in data_list]  # Assuming y values are in the second column

    # Create a line graph using Matplotlib
    plt.plot(x_values, y_values)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Graph')
    plt.show()
