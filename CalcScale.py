'''len from home point in min len is "0 0"      10
max is                                       22
maxp=21
minp=10'''


def scale_ai_to_mm_MM1011(ai_val, ai_min=0, ai_max=5):
    ACTIVE_MM = 11
    per = (ai_val - ai_min) / (ai_max - ai_min) * 100
    mm = ACTIVE_MM*per/100
    return mm
