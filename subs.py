import sqlite3
from flask import request


def createTable():
    # Connect to Database
    conn = sqlite3.connect('subs.db')

    # Create a cursor

    c = conn.cursor()

    # Create a Table
    c.execute("""CREATE TABLE subs (
            email text 
        )""")

    # Commit the command
    conn.commit()

    # Close the Connection
    conn.close()

def dummy():

    # Connect to Database
    conn = sqlite3.connect('subs.db')

    # Create a cursor

    c = conn.cursor()
    print("writing dummy data")
    c.execute("INSERT INTO subs VALUES (platypodes@gmail.com) ")
    print("data added")
    # Commit the command
    conn.commit()

    # Close the Connection
    conn.close()

def new():
    subs = request.form['subscribers']
    # Connect to Database
    conn = sqlite3.connect('subs.db')

    # Create a cursor

    c = conn.cursor()
    print("Adding Data")
    c.execute("INSERT INTO subs VALUES (?) ", subs)
    print("Data Added")
    # Commit the command
    conn.commit()

    # Close the Connection
    conn.close()


def getData():
    # Connect to Database
    conn = sqlite3.connect('subs.db')

    # Create a cursor

    c = conn.cursor()
    print("Getting Data")
    c.execute("SELECT * FROM subs")

    items = (c.fetchall())
    print("Email Addresses")
    print("----------------")
    for item in items:
        print(item)
        print("----------------")