'''len from home point in min len is "0 0"      10
max is                                       22
maxp=21
minp=10'''
import time

import LJ_Acquire


def scale_ai_to_mm_MM1011(ai_val, ai_min=0, ai_max=5):
    ACTIVE_MM = 11
    per = (ai_val - ai_min) / (ai_max - ai_min) * 100
    mm = ACTIVE_MM*per/100
    return ACTIVE_MM-mm


def loadscale_to_kg(val1, val2):
    return 0


def rtd_to_temp(val1,val2):
    R1 = (2.5 - val1) * 10000 / val1
    R2 = (2.5 - val2) * 10000 / val2
    return 30


if __name__ == "__main__":
    h=LJ_Acquire.open_device("T7","USB")
    while True:
        l=LJ_Acquire.read_ai_chl(h,"AIN0")
        l2=LJ_Acquire.read_ai_chl(h,"AIN1")
        print(l)
        print(l2)
        print(scale_ai_to_mm_MM1011(l2,0,l))
        #rtd_to_temp(l,l2)


        time.sleep(1)
