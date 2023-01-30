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
#657309 
folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-4\\i10-"

lMeta = ["/setT/setT", "/pgm_energy/pgm_energy"]
lData = ["/rdeta/rdet", "/rdeta/rmirror"]
plotList = ["/rdeta/rdet corrected", "xmcd /rdeta/rdet corrected", "xmcd ratio /rdeta/rdet corrected" ]
#plotList = None


cutoffs = [1,10,"MAX",0]
outPutFolder = "C:\All my tools\java-mars\pyworkspace\Experiments\Experiment\\Fe2o3\\data\\"


#scanNo = 657575
lScanNo = []#range(657575,657614+1,2)

"""for i in range(657196,657276):
    
    try:
        rWD.read_nexus_data(folder, i)
        if rWD.get_scan_type() == "energy":
            lScanNo.append(i)
    except:
        pass"""
lScanNo = range(657321,657420)
print (lScanNo)
    
plt.figure()
plt.figure(1)
for scanNo in lScanNo[::8]:
    print(scanNo)
    lCpDataName, lCpData, lCpMetaName, lCpMeta = Rd.get_ref(folder, scanNo, lData, lMeta, cutoffs) 
    
    lCnDataName, lCnData, lCnMetaName, lCnMeta = Rd.get_ref(folder, scanNo+1, lData, lMeta, cutoffs) 

    lResult = []
    lResultName = []
    lScanableName = lData
    for i,j in enumerate(lCpDataName[len(lScanableName)+1:]):
        
        lResult.append( Rd.xmcd_w_corr(lCpData[0], lCnData[0], lCpData[i + len(lScanableName)+1], lCnData[i + len(lScanableName)+1]))
        lResultName.append("xmcd %s" %j)
        lResult.append( Rd.xmcd_ratio_w_corr(lCpData[0], lCnData[0], lCpData[i + len(lScanableName)+1], lCnData[i + len(lScanableName)+1]))
        lResultName.append("xmcd ratio %s" %j)
    print (scanNo)
    lFinalDataName = hstack((lCpDataName, lCnDataName, lResultName))
    lFinalData     = vstack((lCpData, lCnData, lResult))
    
    f1 =op.draw_plot([lFinalData[0],lFinalData[0]],  lFinalData,  lFinalDataName, plotList, lCpMeta, lCpMetaName, logY = True, blocking = False )
    fileName = "%i_%s%i" %(scanNo,lCpMetaName[1].split("/")[-1],lCpMeta[1])
    f1.savefig("%s.jpg" %(scanNo))
    
    Rd.write_ascii(fileName+".dat", lFinalDataName, lFinalData, lCpMetaName, lCpMeta)
    
    #f1.show()
    #plt.show(block = False)
input()
    