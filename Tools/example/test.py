'''
Created on 8 Mar 2021

@author: wvx67826

parallel testing
'''
import multiprocessing

import numpy as np
import threading
import time

def spawn(num, list):
    
    time.sleep(np.random.randint(0,10))
    list[num] = num 
    print(list,num)
    return num+1

all_processes = []
list = np.zeros(25)
 
"""if __name__ == '__main__':
    list = np.zeros(25) 
    for i in range(25):
        ## right here
        p = multiprocessing.Process(target=spawn, args=(i,list))
        all_processes.append(p)
        p.start()
    for p in all_processes:
        p.join()
    print(list)
    
    """
    

for i in range(25):
    ## right here
    p = threading.Thread(target=spawn, args=(i,list))
    all_processes.append(p)
    p.start()
for p in all_processes:
    p.join()
print(list)


