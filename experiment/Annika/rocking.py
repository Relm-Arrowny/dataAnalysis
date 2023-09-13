'''
Created on 15 Feb 2023

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

folder ="\\\data.diamond.ac.uk\\i10\\data\\2023\\mm31510-1\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\EuO\\"

scanNoStart = 749585
scanNoEnd = scanNoStart + 2

 
filename = list(range(scanNoStart ,scanNoEnd))

rWD.read_nexus_data(folder, filename[0]);
cpE  = rWD.get_nexus_data("/th/value")
cpdet = rWD.get_nexus_data("/rdeta/rnormdet")
#cp17 = rWD.get_nexus_data("/mcs17/data")/cp16
#cp18 = rWD.get_nexus_data("/mcs18/data")/cp16

rWD.read_nexus_data(folder, filename[1]);
cnE  = rWD.get_nexus_data("/th/value")
cndet = rWD.get_nexus_data("/rdeta/rnormdet")



plt.figure()
plt.semilogy()
plt.plot(cpE,cpdet)
plt.plot(cnE,cndet)


plt.figure()

plt.plot(cpE,cpdet-cndet)

plt.show()
