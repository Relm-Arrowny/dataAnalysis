'''
Created on 15 Sep 2021

@author: wvx67826
'''

from Tools.ReadWriteData import ReadWriteData
from Tools.Output.Output import Output
from Tools.DataReduction.Reduction import Reduction
from Tools.DataReduction.DataCorrection import AngleToQ
from numpy import array, full,vstack,hstack,interp,max,minimum
import matplotlib.pyplot as plt
import matplotlib.cm as cmx

op = Output()
rd = Reduction()
op.add_clipboard_to_figures()
rWD = ReadWriteData()


from matplotlib import ticker
Rd = ReadWriteData()
A2Q = AngleToQ()


def getQandIntensity(data):
    th  = Rd.get_nexus_data("/th/th")
    ref = Rd.get_nexus_data("/rdeta/rnormdet")
    ref = (ref)/max(ref)
    
    fluo = Rd.get_nexus_data("/rdeta/rnormfluo")
    energy = Rd.get_nexus_meta("/pgm_energy/pgm_energy")
    tth = full((1,len(ref)),Rd.get_nexus_meta("/tth/tth"))
    qz = A2Q.cal_qz(tth, th, energy, 0) 
    qx = A2Q.cal_qx(tth, th, energy, 0) 
    allData = vstack((qz,qx,ref,fluo))
    
    plt.figure(1)
    plt.semilogy()
    plt.plot(qx[0],ref)
    print (energy,  Rd.get_nexus_meta("/pol/pol"), Rd.get_nexus_meta("/tth/tth"))
    return allData
pcData = array([])
ncData = array([])
folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-4\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\EuO\\"
scanNo = range(657566, 657575)
#scanNo = range(561420, 561447, 2)
#scanNo = range(561448, 561475, 2)
#scanNo = range(561476, 561503, 2)


for i, scan in enumerate (scanNo):
        if i == 0: 
            data   = Rd.read_nexus_data(folder, scan)
            pcData = getQandIntensity(data)
        else:
            data   = Rd.read_nexus_data(folder, scan)
            pcData = hstack((pcData,getQandIntensity(data)))

        
plt.figure(2)
plt.title("PC")
plt.xlabel("Qz")
plt.ylabel("Qx")
plt.tricontourf(pcData[0], pcData[1] , pcData[2], 30, interp = 'linear',locator=ticker.LogLocator(), cmap=plt.get_cmap('jet'))
plt.colorbar()
plt.show()


