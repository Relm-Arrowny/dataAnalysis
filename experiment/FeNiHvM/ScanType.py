'''
Created on 19 Apr 2022

@author: wvx67826
'''


from Tools.ReadWriteData import ReadWriteData
import matplotlib.pyplot as plt
import numpy as np
from gevent.libev.corecext import NONE
rWD = ReadWriteData()

folder ="Z:\\2022\\cm31127-2\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\"

f = open("scanType.dat", "w")

for scan in range(694804,696246):

    try:
        rWD.read_nexus_data(folder, scan)
        sType = rWD.get_scan_type()
        print(sType)
        pol = rWD.get_nexus_data("/id/polarisation")
        energy = rWD.get_nexus_data("/pgm/energy")
        #temp = rWD.get_nexus_meta("/setT/setT")
    except:
        print("bad scan = %s"%scan)
        pol = None
        energy = None
        temp = None
        
    f.write("scan No = %s, pol = %s, energy = %.s, type = %s\n" %(scan, pol, energy, sType))
    print("scan No = %s, pol = %s, energy = %s, type = %s" %(scan, pol, energy, sType))
f.close()