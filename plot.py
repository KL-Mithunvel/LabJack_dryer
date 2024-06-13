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
    plt.show()






plotGraph([[5,6],[8,7]])