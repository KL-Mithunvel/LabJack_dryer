import time

import matplotlib.pyplot as plt
import numpy as np
#[[time,mm],[time,mm]]






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



    twin2.spines.right.set_position(("axes", 1.2))

    p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
    p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
    p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")

    ax.set(xlim=x, ylim=y1, xlabel="Time", ylabel="Distance")
    twin1.set(ylim=y2, ylabel="Temperature")
    twin2.set(ylim=y3, ylabel="Weight")

    ax.yaxis.label.set_color(p1.get_color())
    twin1.yaxis.label.set_color(p2.get_color())
    twin2.yaxis.label.set_color(p3.get_color())

    ax.tick_params(axis='y', colors=p1.get_color())
    twin1.tick_params(axis='y', colors=p2.get_color())
    twin2.tick_params(axis='y', colors=p3.get_color())

    ax.legend(handles=[p1, p2, p3])

    plt.show()