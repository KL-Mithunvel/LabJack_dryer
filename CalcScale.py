def scale(val):
    high=5
    low=0
    return (val-low)/(high-low)*100
#len from home point in min len is "0 0"      10
#max is                                       22
def lenfromhome(p):
    maxp=21
    minp=10
    return (0.11*p)+minp