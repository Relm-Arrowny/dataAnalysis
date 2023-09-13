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

scanNoStart = 749563
scanNoEnd = scanNoStart + 2

 
filename = list(range(scanNoStart ,scanNoEnd))

rWD.read_nexus_data(folder, filename[0]);
cpE  = rWD.get_nexus_data("/energy/pgm_energy")
cp16 = rWD.get_nexus_data("/mcs16/data")
cp17 = rWD.get_nexus_data("/mcs17/data")/cp16
cp18 = rWD.get_nexus_data("/mcs18/data")/cp16

rWD.read_nexus_data(folder, filename[1]);
cnE  = rWD.get_nexus_data("/energy/pgm_energy")
cn16 = rWD.get_nexus_data("/mcs16/data")
cn17 = rWD.get_nexus_data("/mcs17/data")/cn16
cn18 = rWD.get_nexus_data("/mcs18/data")/cn16

cn17cor = np.interp(cpE, cnE, cn17)
cn18cor = np.interp(cpE, cnE, cn18)

plt.figure()
plt.plot(cpE,cp17)
plt.plot(cpE,cn17cor)

plt.figure()
plt.plot(cpE,cp18)
plt.plot(cpE,cn18cor)


plt.figure()

plt.plot(cpE,cp17-cn17cor)

plt.figure()
plt.plot(cpE,cp18-cn18cor)

plt.show()
