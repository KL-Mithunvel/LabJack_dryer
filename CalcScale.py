'''len from home point in min len is "0 0"      10
max is                                       22
maxp=21
minp=10'''
import random
import time

import LJ_Acquire
import GUI
import config


def scale_ai_to_mm_MM1011(ai_val, ai_min=0, ai_max=5):
    ACTIVE_MM = 11
    per = (ai_val - ai_min) / (ai_max - ai_min) * 100
    mm = ACTIVE_MM*per/100
    return ACTIVE_MM-mm


def loadscale_to_kg(val1):

    max_kg=15
    min_kg=0
    I=(val1*8.475)-4
    print(I)
    per=I/20*100
    kg=(per*max_kg/100+min_kg)
    print(kg)
    return kg


def rtd_to_temp(val1, val2):
    R1 = (2.5 - val1) * 1000 / val1
    R2 = (2.5 - val2) * 1000 / val2
    Rnet = R2-R1
    Temp = (Rnet -100)/0.36
    return Temp

if __name__ == "__main__":
    ljc = config.LJ_Config()
    # read config from config.ini to ljc
    lj: LJ_Acquire = LJ_Acquire.LJAq(ljc)
    if not lj.open_device(ljc.DevType, ljc.ConType):
        GUI.MessageWindow("unable to open LJ." + str(lj.error))
        exit(1)
    while True:
        v5 = lj.read_ai_chl("AIN0")
        loadscale_to_kg(v5)
        time.sleep(1)