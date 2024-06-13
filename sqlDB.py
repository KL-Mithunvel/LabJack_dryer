import sqlite3
def printall(cur):
    res = cur.execute("SELECT  time, mm FROM data;")
    x=res.fetchone()
    while x is not None:
        print(x)
        x = res.fetchone()

def add_data(cur,data):
    #[[time,mm],[time,mm]]
    for i in data:
        cur.execute("INSERT INTO data VALUES({},{})".format(i[0],i[1]))

def create_table(cur):
    cur.execute("CREATE TABLE data( time, mm)")


con = sqlite3.connect("sample.db")
cur = con.cursor()
create_table(cur)
add_data(cur,[[5,6],[5,7]])
printall(cur)
con.close()