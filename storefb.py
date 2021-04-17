import sqlite3 as sl


def insertfeedback(fname, lname, mailid, service, opinion):
    fdlist = [fname, lname, mailid, service, opinion]
    print(fdlist)

    con = sl.connect('gwdata.db')
    c = con.cursor()

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='FDINFO' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists.')
    else:
        print('Table does not exist.')

        with con:  # table with all the different columns that will be used, and type of data
            con.execute("""               
                    CREATE TABLE FDINFO (
                        first_name TEXT,
                        last_name TEXT,
                        mail_id TEXT,
                        service TEXT,
                        opinion TEXT
                        );
                """)
    sql = 'INSERT INTO FDINFO (first_name, last_name, mail_id, service, opinion) values(?, ?, ?, ?, ?)'
    with con:
        con.execute(sql, fdlist)
    with con:
        data = con.execute("SELECT * FROM FDINFO")
    for row in data:
        print(row)

    return


'''
con = sl.connect('platypodes.db')
with con:
    data = con.execute("SELECT * FROM FDINFO")
    for row in data:
        print(row)
'''