'''
Created on 19 Apr 2022

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
from Tools.Output.Output import Output
from Tools.DataReduction.Reduction import Reduction
import matplotlib.pyplot as plt
from numpy import hstack, vstack

op = Output()
Rd = Reduction()
op.add_clipboard_to_figures()
rWD = ReadWriteData()
folder ="Z:\\2022\\cm31127-2\\i10-"
lMeta = ["/id/polarisation"]
lData = ["/rdeta/rdet","/rdeta/rfluo", "/rdeta/rmirror"]
plotList = ["/rdeta/rdet corrected", "xmcd /rdeta/rdet corrected", "xmcd ratio /rdeta/rdet corrected" ]
#plotList = None
scanNo = 694856
lScanNo = [scanNo,scanNo+1]

cutoffs = [1,10,"REF",0]
outPutFolder = "output\\"
plt.figure()


for i,scanNo in enumerate (lScanNo):
    if i == 0: 
        lCpDataName, lCpData, lCpMetaName, lCpMeta = Rd.get_ref(folder, scanNo, lData, lMeta, cutoffs) 
    else:
        lCnDataName, lCnData, lCnMetaName, lCnMeta = Rd.get_ref(folder, scanNo, lData, lMeta, cutoffs) 

lResult = []
lResultName = []
lScanableName = lData
for i,j in enumerate(lCpDataName[len(lScanableName)+1:]):
    
    lResult.append( Rd.xmcd_w_corr(lCpData[0], lCnData[0], lCpData[i + len(lScanableName)+1], lCnData[i + len(lScanableName)+1]))
    lResultName.append("xmcd %s" %j)
    lResult.append( Rd.xmcd_ratio_w_corr(lCpData[0], lCnData[0], lCpData[i + len(lScanableName)+1], lCnData[i + len(lScanableName)+1]))
    lResultName.append("xmcd ratio %s" %j)

lFinalDataName = hstack((lCpDataName, lCnDataName, lResultName))
lFinalData     = vstack((lCpData, lCnData, lResult))

f1 =op.draw_plot([lFinalData[0],lFinalData[0]],  lFinalData,  lFinalDataName, plotList, lCpMeta, lCpMetaName, logY = True )
fileName = "%s%i_%s%s" %(outPutFolder,scanNo,lCpMetaName[1].split("/")[-1],lCpMeta[1])
f1.savefig("%s.jpg" %(fileName))
    
Rd.write_ascii(fileName+".dat", lFinalDataName, lFinalData, lCpMetaName, lCpMeta)
f1.show()
plt.show()