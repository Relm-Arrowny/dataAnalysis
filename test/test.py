'''
Created on 8 Sep 2021

@author: wvx67826
'''
import functools
import operator
import time

seq1 = [1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,
        1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2,
        1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,
        1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2,
        1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,
        1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2, 3,1, 2, 1, 2]



tun = time.time()
def find_it1(seq1):
    seq = list(set(seq1))
    return (seq[list(map(lambda x:x%2, [seq1.count(i) for i in seq])).index(1)])


def find_it4(seq1):
    runSum = 0
    for ite in range(len(seq1)):
        runSum = seq1[ite]-runSum
    return runSum



def find_it2(xs):
    return functools.reduce(operator.xor, xs)
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
tun = time.time()

for i in range(10000):
    find_it2(seq1)

print (find_it2(seq1), tun - time.time())

tun = time.time()
for i in range(10000):
    find_it1(seq1)

print(find_it1(seq1),tun - time.time())
