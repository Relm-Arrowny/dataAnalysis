'''
Created on 8 Mar 2021

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
from Tools.AreaDetector.ImageAnalysis import ImageAnalysis
import numpy as np
import matplotlib.pyplot as plt
from Tools.Output.Output import Output
import threading
op = Output()

op.add_clipboard_to_figures()
ima= ImageAnalysis()
rd = ReadWriteData()

folder = "C:\\Users\\wvx67826\\Desktop\\data\\i10-"#-pixis-files
output = "C:\\Users\\wvx67826\\Desktop\\"
start = 627932
end = start +234
print (end)
lfilename =  range(start ,end)   # 612856
tthData = np.array([])
tthSum = np.array([])
averagetthSum = np.array([])
cut = [175,-50]
lowerOverLap = 0
highOverLap = -1
tthRange = 11.5565705#11.5865705
ss = tthRange/2048.0

overlap = int(((tthRange - 10.0)) /ss-cut[0]+cut[1])
print (overlap)





def multiMeta(folder, scanNo, dataList, counter):
    data = rd.read_nexus_data(folder, scanNo)
    tempI =  rd.get_nexus_data("/pimte/data", nData = data)[0]
    
    tempList = [scanNo,rd.get_nexus_meta("/tth/tth", nData = data),\
                np.sum(tempI,axis=1),np.average(tempI,axis=1)]
    dataList.append(tempList)
    print(scanNo)
    
all_processes = []
list = []
print(list)
for i,j in enumerate(range(start, end)):
    p = threading.Thread(target = multiMeta, args=(folder, j, list, i))
    all_processes.append(p)
    p.start()
    
    
for p in all_processes:
    p.join()
print(list)

 #p = threading.Thread(rd.read_nexus_data(folder, i)

"""            rd.read_nexus_data(folder, k)
        oldtth = rd.get_nexus_meta("/tth/tth")
        tempI =  rd.get_nexus_data("/pimte/data")[0]
        imSum = np.sum(tempI,axis=1)# -np.min(np.sum(tempI,axis=1))
        imAverage =   np.average(tempI,axis=1)# - np.min(np.average(tempI, axis=1))
"""