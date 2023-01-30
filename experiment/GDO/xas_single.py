'''
Created on 8 Mar 2022

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
from Tools.Output.Output import Output
from Tools.DataReduction.Reduction import Reduction
import matplotlib.pyplot as plt

op = Output()
Rd = Reduction()
op.add_clipboard_to_figures()
rWD = ReadWriteData()

folder ="Z:\\2021\\cm28168-3\\i10-"
#638937
scanNoStart = [638943]

for y in scanNoStart:
    rWD.read_nexus_data(folder, y)
    
    en = rWD.get_nexus_meta("/pgm_energy/pgm_energy")
    sx = rWD.get_nexus_meta("/sx/sx")
    sz = rWD.get_nexus_meta("/sz/sz")
    print(sx,sz,en)
    x = rWD.get_nexus_data("/energy/energy")
    y0 = rWD.get_nexus_data("/mcs16/data")
    y1 = rWD.get_nexus_data("/mcs18/data")
    y2 = rWD.get_nexus_data("/mcs19/data")
    y3 = rWD.get_nexus_data("/mcs17/data") 
    
    rWD.read_nexus_data(folder, y+1)
    
    en = rWD.get_nexus_meta("/pgm_energy/pgm_energy")
    sx = rWD.get_nexus_meta("/sx/sx")
    sz = rWD.get_nexus_meta("/sz/sz")
    print(sx,sz,en)
    x1 = rWD.get_nexus_data("/energy/energy")
    y01 = rWD.get_nexus_data("/mcs16/data")
    y11 = rWD.get_nexus_data("/mcs18/data")
    y21 = rWD.get_nexus_data("/mcs19/data")
    y31 = rWD.get_nexus_data("/mcs17/data") 
    yF1 = Rd.average_w_corr(x, x1, y1/y0, y11/y01)
    yF2 = Rd.average_w_corr(x, x1, y2/y0, y21/y01)
    yF3 = Rd.average_w_corr(x, x1, y3/y0, y31/y01)

plt.figure()
plt.suptitle(sx)
plt.subplot(311)
plt.plot(x,yF1)
plt.subplot(312)
plt.plot(x,yF2)
plt.subplot(313)
plt.plot(x,yF3)
sample = "DyGd2o3"
plt.savefig("output\\sample=%s_E=%.1f.png" %(sample, x[0]))
f = open("output\\sample=%s_E=%.1f.dat" %(sample,x[0]), 'w+')
f.write("Energy\tFlou\n")
for j in range (0,len(x)):
    f.write("%f \t %f \n" %(x[j],yF2[j]))
f.close()

plt.show()