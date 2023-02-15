'''
Created on 11 Aug 2021

@author: wvx67826
'''

from Tools.ReadWriteData import ReadWriteData
from Tools.Output.Output import Output
from Tools.DataReduction.Reduction import Reduction
import matplotlib.pyplot as plt
import numpy as np
op = Output()
rd = Reduction()
op.add_clipboard_to_figures()
rWD = ReadWriteData()

lScanable = ["/mcs17/data","/mcs18/data","/mcs16/data"]
lplot = [ "/mcs18/data", '/mcs18/data norm', '/mcs18/data corrected'\
        ,"/mcs17/data", '/mcs17/data norm', '/mcs17/data corrected'\
        ,'xmcd /mcs18/data norm', 'xmcd /mcs17/data norm',
        'xmcd /mcs18/data corrected', 'xmcd /mcs17/data corrected']
lMetaName = []
#folder = "C:\\Users\\wvx67826\\Desktop\\New folder\\data\\i10-"#-pixis-files
#To get the polarisation details

folder ="\\\data.diamond.ac.uk\\i10\\data\\2023\\mm31510-1\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\EuO\\"

scanNoStart = 749563
scanNoEnd = scanNoStart +2
scanJump = 1
for i in range(scanNoStart,scanNoEnd,scanJump):
    scanNo = i
    filename = np.arange(scanNo, scanNo+2,1)
    
    lFinalDataName, lFinalData , lCpMetaName, lCpMeta, lCnMetaName, lCnMeta  = rd.get_xmcd(folder, filename,  lScanableName = lScanable, lMetaName = lMetaName)
    #rd.get_xmcd
   
    #print(lFinalDataName)
    
    #f1 = op.draw_plot([lData[0]],  lData,  lDataName, lYNameUse = lplot )
    temp = 8#int(((len(lFinalData)-3)/2))-1
    f1 = op.draw_plot([lFinalData[0],lFinalData[temp]],  lFinalData,  lFinalDataName,lplot , lMetaName=lCpMetaName, lMeta =lCpMeta, blocking = True )
    
    fileName = output + "%s_sample.dat" %(i)
    rd.write_ascii(fileName, lFinalDataName, lFinalData, lCnMetaName, lCnMeta) 
    f1.savefig("%s.jpg" %(fileName[:-4]))


