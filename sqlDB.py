import sqlite3


def printall(cur):
    res = cur.execute("SELECT  time, mm FROM data;")
    x = res.fetchone()
    while x is not None:
        print(x)
        x = res.fetchone()


def add_data(cur, sno, data):
    #data->[time,mm]
    cur.execute("INSERT INTO data VALUES({},{},{})".format(sno, data[0], data[1]))


def create_table(cur):
    cur.execute("CREATE TABLE if not exists data(Sno,time, mm) ")


def get_cursor(dfile):
    con = sqlite3.connect(dfile)
    cur = con.cursor()
    create_table(cur)
    return con


def get_data(cur, sl):
    data = []
    res = cur.execute("SELECT  time, mm FROM data ")
    x = res.fetchone()
    while x is not None:
        data.append(x)
        x = res.fetchone()
    return data


def close(con):
    con.close()


if __name__ == "__main__":
    print(get_data(get_cursor("sample.db"), "456"))
