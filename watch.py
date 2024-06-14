import time
mins = 1
x=time.time()
t_end = time.time() + 60 * mins
while time.time() < t_end:
    print(int(time.time()-x))
    time.sleep(1)
