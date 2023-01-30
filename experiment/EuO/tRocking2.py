'''
Created on 16 Sep 2021

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
from Tools.Output.Output import Output
from Tools.DataReduction.Reduction import Reduction
from Tools.DataReduction.DataCorrection import AngleToQ
from numpy import array, full,vstack,hstack,interp,max,minimum
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
from sqlalchemy.sql.expression import except_

op = Output()
Rd = Reduction()
op.add_clipboard_to_figures()
rWD = ReadWriteData()

folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-4\\i10-"

lMeta = ["/setT/setT", "/pgm_energy/pgm_energy"]
lData = ["/rdeta/rdet", "/rdeta/rmirror"]
plotList = ["/rdeta/rdet corrected"]
#plotList = None


cutoffs = [1,10,"MAX",0]
outPutFolder = "C:\All my tools\java-mars\pyworkspace\Experiments\Experiment\\Fe2o3\\data\\"


#scanNo = 657575
lScanNo = []#range(657575,657614+1,2)

for i in range(657425, 657434,1):
    
    try:
        rWD.read_nexus_data(folder, i)
        if rWD.get_scan_type() == "th":
            lScanNo.append(i)
    except:
        pass
        
print (lScanNo)
    
plt.figure()
for scanNo in lScanNo:
    
    lCpDataName, lCpData, lCpMetaName, lCpMeta = Rd.get_ref(folder, scanNo, lData, lMeta, cutoffs) 

    
    #f1 =op.draw_plot([lCpData,[0],lCpData,[0]],  lCpData,  lFinalDataName, plotList, lCpMeta, lCpMetaName, logY = True, blocking = False )
    fileName = "%i_%s%i_%.1f" %(scanNo,lCpMetaName[1].split("/")[-1],lCpMeta[1],lCpMeta[2])
    #f1.savefig("%s.jpg" %(scanNo))
    print(lCpMeta[2])
    Rd.write_ascii(fileName+".dat", lCpDataName, lCpData, lCpMetaName, lCpMeta)
    plt.semilogy()
    plt.xlabel("Theta (degree")
    plt.ylabel("Intensity (A.U.")
    plt.plot(lCpData[0],lCpData[1], )
    #f1.show()
    #plt.show(block = False)


plt.show()
    