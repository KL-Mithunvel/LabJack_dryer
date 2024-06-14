import labJdata
import watch
import threading
import plot
#T1=threading.Thread(target=labJdata.data_fromJ)
runenv=[]
T2 = threading.Thread(target=watch.timer, args=(1,runenv))
T2.start()
print(T2.join())
print(runenv)
plot.plotGraph(runenv)
print("klm")
