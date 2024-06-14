import labJdata
import threading
T1=threading.Thread(target=labJdata.data_fromJ)
T1.start()
T1.join()
print("klm")