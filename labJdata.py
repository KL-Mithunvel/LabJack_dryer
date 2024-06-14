import time
import CalcScale
from labjack import ljm
def data_fromJ():
    try:
        handle = ljm.openS("T7", "USB", "ANY")
    except ljm.ljm.LJMError:
        print("connection not made")
    else:
        print("Connuction made")
        READ = ljm.constants.READ
        lifetime=[]

        while True:
            value = ljm.eReadName(handle, "AIN0")
            lifetime.append(value)
            print("AIN0: ", value)
            percentage = CalcScale.scale(value)
            print("percentage: ", percentage)
            length = CalcScale.lenfromhome(percentage)
            print("len: ", length)

        else:
            ljm.close(handle)
            print("Connuction close")


