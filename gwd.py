import sqlite3

conn = sqlite3.connect('gwdata.db')

# creating cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE gwdata (

    user text,
    email text
    )
    """)

