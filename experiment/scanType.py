'''
Created on 8 Sep 2021

@author: wvx67826
'''

from Tools.ReadWriteData import ReadWriteData
import matplotlib.pyplot as plt
import numpy as np
from gevent.libev.corecext import NONE
rWD = ReadWriteData()

folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-3\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\"

f = open("Tenp.dat", "w")

for scan in range(638453,638913):
    
    rWD.read_nexus_data(folder, scan)

    try:
        pol = rWD.get_nexus_meta("/pol/pol")
        energy = rWD.get_nexus_meta("/pgm_energy/pgm_energy")
        temp = rWD.get_nexus_meta("/setT/setT")
    except:
        print("bad scan = %s"%scan)
        pol = None
        energy = None
        temp = None
        
    f.write("scan No = %s, pol = %s, energy = %.s, temp = %s\n" %(scan, pol, energy, temp))
    print("scan No = %s, pol = %s, energy = %s, temp = %s" %(scan, pol, energy, temp))
f.close()