import sqlite3
from scipy.optimize import curve_fit




def printall(cur):
    res = cur.execute("SELECT  time, mm FROM data;")
    x = res.fetchone()
    while x is not None:
        print(x)
        x = res.fetchone()


def add_data(cur, sno, data, con):
    #data->[time,mm]
    cmd = "INSERT INTO data VALUES({},{},{},{},{})".format(sno, data[0], data[1], data[2], data[3])
    cur.execute(cmd)
    flush(con)


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


def test_testno(no):
    con = sqlite3.connect("sample.db")
    cur = con.cursor()
    data = []
    res = cur.execute("SELECT  Sno FROM data")
    x = res.fetchone()
    while x is not None:
        data.append(x)
        x = res.fetchone()
    if no in data:
        return True
    else:
        return False


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Sample data
    x_data = np.array([0, 1, 2, 3, 4, 5])
    y_data = np.array([0, 2.1, 4.5, 70, 10.8, 14.2])


    # Define a polynomial model (2nd degree polynomial in this case)
    def polynomial_model(x, a, b, c):
        return a * x ** 2 + b * x + c


    # Curve fitting
    params, covariance = curve_fit(polynomial_model, x_data, y_data)

    # Create a smooth line using the fitted parameters
    x_smooth = np.linspace(x_data.min(), x_data.max(), 500)
    y_fit = polynomial_model(x_smooth, *params)

    # Plotting
    plt.scatter(x_data, y_data, color='red', label='Data Points')
    plt.plot(x_smooth, y_fit, color='blue', label='Fitted Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    # Print the parameters
    print(f'Fitted parameters: {params}')
