import time

import matplotlib.pyplot as plt
import numpy as np
#[[time,mm],[time,mm]]

def plotGraph(lt):
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





def Live_plotGraph(lt):
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
    time.sleep(10)
    plt.close()
