'''len from home point in min len is "0 0"      10
max is                                       22
maxp=21
minp=10'''
import random



def scale_ai_to_mm_MM1011(ai_val, ai_min=0, ai_max=5):
    ACTIVE_MM = 11
    per = (ai_val - ai_min) / (ai_max - ai_min) * 100
    mm = ACTIVE_MM*per/100
    return ACTIVE_MM-mm


def loadscale_to_kg(val1, val2):
    return random.randint(1,4)


def rtd_to_temp(val1, val2):
    R1 = (2.5 - val1) * 1000 / val1
    R2 = (2.5 - val2) * 1000 / val2
    Rnet = R2-R1
    Temp = (Rnet -100)/0.36
    return Temp
