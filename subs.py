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


def new(request):
    subs = request.form['emails']
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


def delete():
    # Connect to Database
    conn = sqlite3.connect('subs.db')

    # Create a cursor

    c = conn.cursor()

    subs = request.form['emails']

    c.execute("DELETE FROM subs", (subs,))
    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect('subs.db')
    c = conn.cursor()
    c.execute("UPDATE subs SET emails = ?", (subs))
    conn.commit()
    conn.close()
