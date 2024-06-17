import time
import LJ_Acquire
import threading

def timer(mins,train):

    x = time.time()
    sec = 0
    t_end = time.time() + 60 * mins
    while time.time() < t_end:
        # print(time.time()-x)
        l = LJ_Acquire.read_ai_chl("AIN1")
        print(sec)
        sec += 1
        time.sleep(1)
        train.append([sec, l])


