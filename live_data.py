import time
import LJ_Acquire
import config
import threading
import GUI
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_live():
    fig, ax = plt.subplots()
    twin1 = ax.twinx()
    twin2 = ax.twinx()
    twin2.spines.right.set_position(("outward", 60))

    x = []
    y1 = []
    y2 = []

    line1, = ax.plot([], [], "C0", label="Shrinking (in mm)")
    line2, = twin1.plot([], [], "C1", label="Temperature")

    def init():
        ax.set_xlim(0, 30)
        ax.set_ylim(0, 100)
        twin1.set_ylim(0, 100)
        return line1, line2

    def update(frame):
        x.append(frame)
        y1.append(l[0])
        y2.append(l[1])

        line1.set_data(x, y1)
        line2.set_data(x, y2)

        if len(x) > 0:
            current_time = x[-1]
            ax.set_xlim(max(current_time - 30, 0), current_time)

        if len(y1) > 0:
            ax.set_ylim(min(y1), max(y1))
        if len(y2) > 0:
            twin1.set_ylim(min(y2), max(y2))

        return line1, line2

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=False, interval=1000)

    ax.set_xlabel("Time")
    ax.set_ylabel("Shrinking (in mm)")
    twin1.set_ylabel("Temperature")

    ax.legend(loc="upper left")

    plt.show()

#set up
ljc = config.LJ_Config()

lj: LJ_Acquire = LJ_Acquire.LJAq(ljc)
if not lj.open_device(ljc.DevType, ljc.ConType):
    GUI.MessageWindow("unable to open LJ."+str(lj.error))
    exit(1)

lv_data = lj.read_once()
print(lv_data[0])
print(lv_data[1])
plot_live(lv_data)
