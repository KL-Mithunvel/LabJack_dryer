import time

import matplotlib.pyplot as plt
import numpy as np
#[[time,mm],[time,mm]]

def OG_plotGraph(lt):
    x = []
    y = []
    for i in lt:
        x.append(i[0])
        y.append(i[1])

    xpoints = np.array(x)
    ypoints = np.array(y)

    plt.plot(xpoints, ypoints)
    plt.xlabel('Time')
    plt.ylabel('distance in mm')

    plt.show()





def plotGraph(lt):
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    twin1 = ax.twinx()
    twin2 = ax.twinx()
    x = []
    y1 = []
    y2 = []
    y3 = []
    for i in lt:
        x.append(i[0])
        y1.append(i[1])
        y2.append(i[2])
        y3.append(i[3])
    xpoints = np.array(x)
    y1points = np.array(y1)
    y2points = np.array(y2)
    y3points = np.array(y3)


    twin2.spines.right.set_position(("axes", 1.2))

    p1, = ax.plot(xpoints, y1points, "C0", label="Density")
    p2, = twin1.plot(xpoints, y2points, "C1", label="Temperature")
    p3, = twin2.plot(xpoints, y3points, "C2", label="Velocity")

    ax.set(xlim=(min(xpoints),max(xpoints)), ylim=(min(y1points),max(y1points)), xlabel="Time", ylabel="Distance")
    twin1.set(ylim=(min(y2points),max(y2points)), ylabel="Temperature")
    twin2.set(ylim=(min(y3points),max(y3points)), ylabel="Weight")

    ax.yaxis.label.set_color(p1.get_color())
    twin1.yaxis.label.set_color(p2.get_color())
    twin2.yaxis.label.set_color(p3.get_color())

    ax.tick_params(axis='y', colors=p1.get_color())
    twin1.tick_params(axis='y', colors=p2.get_color())
    twin2.tick_params(axis='y', colors=p3.get_color())

    ax.legend(handles=[p1, p2, p3])

    plt.show()





if __name__ == "__main__":
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    twin1 = ax.twinx()
    twin2 = ax.twinx()

    # Offset the right spine of twin2.  The ticks and label have already been
    # placed on the right by twinx above.
    twin2.spines.right.set_position(("axes", 1.2))

    p1, = ax.plot([2,3,4], [0, 1, 2], "C0", label="Density")
    p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
    p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")

    ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
    twin1.set(ylim=(0, 4), ylabel="Temperature")
    twin2.set(ylim=(1, 65), ylabel="Velocity")

    ax.yaxis.label.set_color(p1.get_color())
    twin1.yaxis.label.set_color(p2.get_color())
    twin2.yaxis.label.set_color(p3.get_color())

    ax.tick_params(axis='y', colors=p1.get_color())
    twin1.tick_params(axis='y', colors=p2.get_color())
    twin2.tick_params(axis='y', colors=p3.get_color())

    ax.legend(handles=[p1, p2, p3])

    plt.show()