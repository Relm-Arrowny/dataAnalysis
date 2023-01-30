'''
Created on 19 Apr 2022

@author: wvx67826
'''

from Tools.Output.Output import Output
from Tools.ReadWriteData import ReadWriteData
from win32api import GetSystemMetrics
import matplotlib.pyplot as plt
import numpy as np

op = Output()
op.add_clipboard_to_figures()
rWD = ReadWriteData()


start =695139
end = start +1
folder ="Z:\\2022\\cm31127-2\\i10-"
field = np.array([])
intensityInc = np.array([])
intensityDec = np.array([])
lth = np.array([])
myDpi = 100
screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)
#p1 =plt.figure(1, figsize=(screenWidth/myDpi, screenHeight/myDpi), dpi=myDpi)
plt.figure(1, figsize=(screenWidth/myDpi, screenHeight/myDpi), dpi=myDpi)

#plt.figure(2)
for i in range (start, end, 3):
    rWD.read_nexus_data(folder, i)
    field = rWD.get_nexus_data("/ui1ao3/value")*714
    data = rWD.get_nexus_data("/rdeta/rnormdet")
    data1 = rWD.get_nexus_data("/rdeta/rnormfluo")
    if i == start:
        intensityInc = data
    else:
        intensityInc = intensityInc + data

    
    
    plt.plot(field, data)
    #plt.figure(2)
    #plt.plot(field, data1)
    rWD.read_nexus_data(folder, i+1)
    tempField = rWD.get_nexus_data("/ui1ao3/value")*714
    th = rWD.get_nexus_data("/rasor/diff/theta")
    print (th)
    data = rWD.get_nexus_data("/rdeta/rnormdet")
    data1 = rWD.get_nexus_data("/rdeta/rnormfluo")
    if i == start:
        intensityDec = data
    else:
        intensityDec = intensityDec + data

    #plt.figure(1)
    #th = 10
    plt.title("Sigma-Sigma \u03B8 = %i\u00b0" %th, fontsize=20)
    #plt.title("Linear Horizontal \u03B8 = %i\u00b0" %th, fontsize=20)
    #plt.title("Linear Vertical \u03B8 = %i\u00b0" %th, fontsize=20)
    #plt.title("Positive Helicity",fontsize=50)
    #plt.title("Negative Helicity",fontsize=50)
    plt.ylabel("Reflectivity (arb. units)", fontsize=48)
    plt.xlabel("Field (Gauss)", fontsize=48)
    plt.plot(tempField, data, linestyle="solid", linewidth=1.0)
    plt.xticks(fontsize = 40)
    plt.yticks(fontsize = 40)
    plt.savefig("output\\%i-th=%i_ref" %(i,th), bbox_inches='tight')
    plt.show()
    plt.close()
"""    plt.figure(2)
    plt.xlabel(th)
    plt.plot(tempField, data1)
    plt.savefig("output\\%i-th=%i_fluo" %(i,th))
    plt.close()"""