'''
Created on 11 Aug 2021

@author: wvx67826
'''

from Tools.ReadWriteData import ReadWriteData
from Tools.Output.Output import Output
from Tools.DataReduction.Reduction import Reduction
import matplotlib.pyplot as plt
import numpy as np
import os
op = Output()
rd = Reduction()
op.add_clipboard_to_figures()
rWD = ReadWriteData()

lScanable = ["/energyh/pgm_energy", "/mcsh16/data", "/mcsh17/data",  "/mcsh18/data"]
lMetaName = ["/id/polarisation",
                "/ips/field_set_point",
                "/itc3_device/sensor_temp",
                "/hfm/x",
                "/hfm/y",
                "/hfm/pitch",]
#folder = "C:\\Users\\wvx67826\\Desktop\\New folder\\data\\i10-"#-pixis-files
#To get the polarisation details

folder ="C:\\Users\\wvx67826\\Desktop\\data_nexus\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\EuO\\"

for filename in sorted(os.listdir("C:\\Users\\wvx67826\\Desktop\\data_nexus\\")): 
    scan = filename[4:-4]
    print(scan)
#for scan in range(692510,692793):
    rWD.read_nexus_data(folder, scan)
    data = np.array([])
    metaData = np.array([])
    i=0
    for dataName in lScanable:
        if i==0:
            data = rWD.get_nexus_data(dataName)
            i+=1
        else:
            tempData   = rWD.get_nexus_data(dataName)
            data = np.vstack((data ,tempData))

    for metaName in lMetaName:
        tempData   = rWD.get_nexus_data(metaName)
        
        metaData = np.append(metaData,tempData)

    rWD.write_ascii("i10-%s.dat" %scan, lScanable, data, lMetaName, metaData)

