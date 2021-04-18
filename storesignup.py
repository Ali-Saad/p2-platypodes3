import sqlite3 as sl


def insertsignup(mailadd, psswrd, pssrep):
    sulist = [mailadd, psswrd, pssrep]

    con = sl.connect('gwdata.db')
    c = con.cursor()

    # get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SUINFO' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists.')
    else:
        print('Table does not exist.')

        with con:  # table with all the different columns that will be used, and type of data
            con.execute("""               
                    CREATE TABLE SUINFO (
                        mail_address TEXT,
                        password TEXT,
                        pass_rep TEXT
                        );
                """)
    sql = 'INSERT INTO SUINFO (mail_address, password, pass_rep) values(?, ?, ?)'
    with con:
        con.execute(sql, sulist)
    with con:
        data = con.execute("SELECT * FROM SUINFO")
    for row in data:
        print(row)

    return


def logincheck(mailadd, psswrd):
    paramlst = []
    paramlst.append(mailadd)
    con = sl.connect('gwdata.db')
    c = con.cursor()

    sql = 'SELECT password FROM SUINFO WHERE mail_address=?'

    c.execute(sql, paramlst)
    stpw = c.fetchone()[0]
    if psswrd == stpw:
        return ("yes")
    else:
        return ("no")
    return