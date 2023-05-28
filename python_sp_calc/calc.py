import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import os

def graph(employee, covid):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir,f'../backend_sp_db/Database/project_SP.db')
    conn = sqlite3.connect(path)
   
   #set Filter depending on selected team
    teamFilter= ""

    rows1 = pd.read_sql_query("SELECT * FROM Covid_Data", conn)
    rows2 = pd.read_sql_query(f"SELECT * FROM [SP_Project_Sums{teamFilter}]", conn)

    conn.close()

    dates = rows1['date']
    employee_list = rows2.iloc[:, employee]
    covid_list = rows1.iloc[:, covid]

    employee_label = rows2.columns[employee]
    covid_label = rows1.columns[covid]

    # Create a line graph
    fig, ax1 = plt.subplots()
    

    ax1.plot(dates, employee_list, 'bo-', label=employee_label)
    ax1.set_xlabel('Time')
    ax1.set_ylabel(employee_label, color='b')

    ax2 = ax1.twinx()
    ax2.plot(dates, covid_list, 'ro-', label=covid_label)
    ax2.set_ylabel(covid_label, color='r')

    plt.title('COVID in Kanton Zürich and Employees Stadtspital Zürich ICU - Over Time')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.xticks(rotation=45)
    plt.xticks(range(0, len(dates), 3)) 
    imgPath = os.path.join(current_dir, f'../svelte_sp_interface/public/img/{teamFilter}/plot{employee}{covid}.png')
    plt.savefig(imgPath)
    plt.close()


#create all graph versions (per Team)
graph(1,1)
graph(2,1)
graph(3,1)
graph(4,1)
graph(5,1)
graph(6,1)
graph(7,1)
graph(1,2)
graph(2,2)
graph(3,2)
graph(4,2)
graph(5,2)
graph(6,2)
graph(7,2)
graph(1,3)
graph(2,3)
graph(3,3)
graph(4,3)
graph(5,3)
graph(6,3)
graph(7,3)
graph(1,4)
graph(2,4)
graph(3,4)
graph(4,4)
graph(5,4)
graph(6,4)
graph(7,4)
