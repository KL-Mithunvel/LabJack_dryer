import sqlite3


def printall(cur):
    res = cur.execute("SELECT  time, mm FROM data;")
    x = res.fetchone()
    while x is not None:
        print(x)
        x = res.fetchone()


def add_data(cur, sno, data):
    #data->[time,mm]
    cmd = "INSERT INTO data VALUES({},{},{},{},{})".format(sno, data[0], data[1], data[2], data[3])
    cur.execute(cmd)


def create_table(cur):
    cur.execute("CREATE TABLE if not exists data(Sno,time, mm,temp, weight ) ")


def get_cursor(dfile):
    con = sqlite3.connect(dfile)
    cur = con.cursor()
    create_table(cur)
    return cur, con


def get_data(cur, sl):
    data = []
    cmd="SELECT  time, mm ,temp, weight FROM data WHERE Sno = {}".format(sl)
    res = cur.execute(cmd)
    x = res.fetchone()
    while x is not None:
        data.append(x)
        x = res.fetchone()

    return data

def flush(con):
    con.commit()


def close(con):
    con.close()


def test_testno(cur):
    while True:
        no = int(input("Enter Sl No. of Test:"))
        data = set()
        cmd = "SELECT  Sno FROM data"
        res = cur.execute(cmd)
        x = res.fetchone()
        while x is not None:
            data.add(x[0])
            x = res.fetchone()
        print(data)
        if no not in data:
            break
    return no

if __name__ == "__main__":
    con = sqlite3.connect("sample.db")
    cur = con.cursor()
    sl = input("Enter Sl No. of Test to view:")
    data = []
    res = cur.execute("SELECT  time, mm ,temp, weight FROM data WHERE Sno = {}".format(sl))
    x = res.fetchone()
    while x is not None:
        data.append(x)
        x = res.fetchone()
    print(data)
