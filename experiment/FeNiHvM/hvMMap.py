'''
Created on 19 Apr 2022

@author: wvx67826
'''

from Tools.Output.Output import Output
from Tools.ReadWriteData import ReadWriteData
import matplotlib.pyplot as plt
import numpy as np

op = Output()
op.add_clipboard_to_figures()
rWD = ReadWriteData()
import logging

start = 695772+1
end = 695845
folder ="Z:\\2022\\cm31127-2\\i10-"
field = np.array([])
intensity = np.array([])
lth = np.array([])
for i in range (start, end + 1, 5):
    #plt.figure()
    rWD.read_nexus_data(folder, i)
    tempField = rWD.get_nexus_data("/ui1ao3/value")*714
    th = np.full((1,len(tempField)),4.*np.pi/(12.4/0.707)*np.sin(np.deg2rad(rWD.get_nexus_data("/rasor/diff/theta"))))
    #print (th[0])
    lth = np.hstack((lth,th[0]))
    field = np.hstack((field,tempField))
    data = rWD.get_nexus_data("/rdeta/rnormdet")
    intensity = np.hstack((intensity,(data-np.min(data))/np.max(data)))
    logging.warn(i)
    #plt.plot(field, intensity)
    
plt.figure(1)
print (len(lth), len(field), len(intensity))
plt.tricontourf(lth, field , intensity, 30, interp = 'linear', cmap=plt.get_cmap('jet'))
#plt.title("Linear Horizontal Increasing", fontsize=18)
#plt.title("Linear Vertical Increasing", fontsize=18)
#plt.title("Linear Horizontal decreasing", fontsize=18)
plt.title("Linear Vertical decreasing", fontsize=18)
#plt.title("Positive Helicity Increasing", fontsize=18)
#plt.title("Negative Helicity Increasing", fontsize=18)
#plt.title("Positive Helicity decreasing", fontsize=18)
#plt.title("Negative Helicity decreasing", fontsize=18)
plt.xlabel("Theta (\u00b0)", fontsize=18)
plt.ylabel("Field (Gauss)", fontsize=18)
plt.colorbar()
plt.savefig("%i-refMap" %(i))
plt.show()