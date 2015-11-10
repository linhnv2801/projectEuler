__author__ = 'linh.nv'
import time
def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]

start = time.time()*1000
n = route_num(20)
elapsed = (time.time()*1000 - start)
print "%s found in %s miliseconds" % (n,elapsed)