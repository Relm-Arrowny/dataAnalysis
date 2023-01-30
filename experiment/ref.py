'''
Created on 8 Sep 2021

@author: wvx67826
'''
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

lScanable = ["/mcs17/data","/mcs18/data","/mcs19/data","/mcs16/data"]
lplot = ["/mcs19/data", '/mcs19/data norm', '/mcs19/data corrected' ,"/mcs18/data", '/mcs18/data norm', '/mcs18/data corrected'\
        ,"/mcs17/data", '/mcs17/data norm', '/mcs17/data corrected'\
        ,'xmcd /mcs19/data norm', 'xmcd /mcs18/data norm', 'xmcd /mcs17/data norm',
        'xmcd /mcs18/data corrected', 'xmcd /mcs19/data corrected', 'xmcd /mcs17/data corrected']
lMetaName = ["/setT/setT"]
#folder = "C:\\Users\\wvx67826\\Desktop\\New folder\\data\\i10-"#-pixis-files
#To get the polarisation details

folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-3\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\EuO\\"

scanNoStart = 655782
scanNoEnd = scanNoStart +1
scanJump = 2
for i in range(scanNoStart,scanNoEnd,scanJump):
    scanNo = i
    filename = range(scanNo, scanNo+scanJump)
    
    lFinalDataName, lFinalData , lCpMetaName, lCpMeta, lCnMetaName, lCnMeta  = rd.get_xmcd(folder, filename,  lScanableName = lScanable, lMetaName = lMetaName, cutoffs = [10,25,-40,-20])
    #rd.get_xmcd
   
    #print(lFinalDataName)
    
    #f1 = op.draw_plot([lData[0]],  lData,  lDataName, lYNameUse = lplot )
    temp = int(((len(lFinalData)-3)/2))-1
    f1 = op.draw_plot([lFinalData[0],lFinalData[temp]],  lFinalData,  lFinalDataName,lplot , lMetaName=lCpMetaName, lMeta =lCpMeta, blocking = True )
    
    fileName = output + "%s_sample.dat" %(i)
    rd.write_ascii(fileName, lFinalDataName, lFinalData, lCnMetaName, lCnMeta) 
    f1.savefig("%s.jpg" %(fileName[:-4]))


