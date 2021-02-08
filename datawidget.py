import sqlite3
from tabulate import tabulate

def add_project(val):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO project (Client_name, Project_desc, Total_amount, Start_date, End_date)VALUES (?,?,?,?,?)", val)
    conn.commit()
    conn.close()
    
def add_transaction():
    conn = sqlite3.connect('database.db')
    #c = conn.cursor()
    conn.commit()
    conn.close()

def view_all_projects():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * from project")
    project_list = c.fetchall()
    conn.commit()
    conn.close()
    return tabulate(project_list, headers = ['ProjectID', 'Client Name', 'Project Description', 'Total Amount', 'Start Date','End Date'], tablefmt='fancy_grid', stralign='left', numalign='center')

def view_all_transactions():
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("SELECT * from transactions")
    transaction_list = c.fetchall()
    conn.commit()
    conn.close()
    return tabulate(transaction_list, headers = ['ProjectID','TransactionID','Amount(Rs.)','Transaction_Date'], tablefmt='fancy_grid', stralign='left', numalign='center')
    

def search_transaction(prj_id):
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("SELECT * FROM transactions WHERE ProjectID = (?)",str(prj_id))
    transaction_list = c.fetchall()
    new_tranlist = []
    for t in transaction_list:
        new_tranlist.append([i for i in t[1:]]) 
    if len(transaction_list) == 0:
        print("No entries found. Invalid ProjectID.")
    else:
        print("ProjectID: ",prj_id)
        print(tabulate(transaction_list, headers = ['TransactionID','Amount(Rs.)','Transaction_Date'], tablefmt='fancy_grid'))
    conn.commit()
    conn.close()

def search_project(prj_id):
    conn = sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("SELECT * FROM project WHERE ProjectID = (?)",str(prj_id))
    project_list = c.fetchall()
    if len(project_list) == 0:
        print("No entries found. Invalid ProjectID.")
    print(tabulate(project_list, headers = ['ProjectID', 'Client_name','Project_Description','Total_Amount','Start_Date', 'End_Date'], tablefmt='fancy_grid'))
    conn.commit()
    conn.close()
