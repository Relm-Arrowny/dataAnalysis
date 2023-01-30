import numpy as np

import time

def mult(a,b):
        return a*b


def bMult(a,b):
    return np.bitwise_and(a,b)


def lMult(a,b):
    return np.logical_and(a,b)

def rMult(a,b):
    return a[b]

a = np.full((10000,10000), True)
b = np.full((10000,10000), False)



start = time.time()
for i in range(0,100):
    lMult(a,b)
print (start - time.time())
print(bMult(a,b))
start = time.time()
for i in range(0,100):
    bMult(a,b)
print (start - time.time())


