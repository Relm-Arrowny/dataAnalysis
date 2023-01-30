'''
Created on 6 Oct 2021

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

folder ="C:\\Users\\wvx67826\\Desktop\\data\\i10-"

lMeta = ["/setT/setT", "/pgm_energy/pgm_energy"]
lScanable = ["/mcs17/data","/mcs18/data","/mcs16/data"]
lplot = ["/mcs17/data", '/mcs17/data norm', '/mcs17/data corrected', "/mcs17/data",
         '/mcs18/data norm', "/mcs18/data corrected" ]

oldEnergy = 0.0
oldPos = 0
x= [0]
y= [0]
y1 = [0]
for scanNoStart in range(638938,639138):
    rWD.read_nexus_data(folder, scanNoStart)
    if abs(oldEnergy - rWD.get_nexus_meta("/pgm_energy/pgm_energy"))>0.5:
        
        plt.figure()
        plt.suptitle(oldPos)
        plt.subplot(121)
        plt.plot(x,y)
        plt.subplot(122)
        plt.plot(x,y1)
        
        #plt.savefig("sample=%.1f_E=%.1f.png" %(scanNoStart,oldEnergy))
        f = open("sample=%.1f_E=%.1f.dat" %(scanNoStart,oldEnergy), 'w+')
        f.write("Energy\tDrain\tFlou\n")
        for j in range (0,len(x)):
            f.write("%f \t %f \t %f \n" %(x[j],y[j],y1[j]))
        f.close()
        
        oldPos = rWD.get_nexus_meta("/sz/sz")
        oldEnergy = rWD.get_nexus_meta("/pgm_energy/pgm_energy")
        
        
        oldEnergy = rWD.get_nexus_meta("/pgm_energy/pgm_energy")
        y = rWD.get_nexus_data("/mcs18/data")
        y1 = rWD.get_nexus_data("/mcs19/data")
        y0 = rWD.get_nexus_data("/mcs16/data")
        y = y/y0
        y1 = y1/y0
        x = rWD.get_nexus_data("/energy/energy") 
        print (scanNoStart, oldEnergy)
        
        plt.savefig("sample=%.1f_E=%.1f.png" %(scanNoStart,oldEnergy))
        oldPos = scanNoStart#rWD.get_nexus_meta("/sz/sz")
        oldEnergy = rWD.get_nexus_meta("/pgm_energy/pgm_energy")
        
        plt.close()
    else:
        rWD.read_nexus_data(folder, scanNoStart)
        yNew = rWD.get_nexus_data("/mcs18/data")/rWD.get_nexus_data("/mcs16/data")
        xNew = rWD.get_nexus_data("/energy/energy")
        y = Rd.average_w_corr(x, xNew, y, yNew)
    
        y1New = rWD.get_nexus_data("/mcs19/data")/rWD.get_nexus_data("/mcs16/data")
        xNew = rWD.get_nexus_data("/energy/energy")
        y1 = Rd.average_w_corr(x, xNew, y1, y1New)


plt.figure()
plt.suptitle(oldPos)
plt.subplot(121)
plt.plot(x,y)
plt.subplot(122)
plt.plot(x,y1)

plt.savefig("output//sample=%.1f_E=%.1f.png" %(oldPos,oldEnergy))
f = open("sample=%.1f_E=%.1f.dat" %(oldPos,oldEnergy), 'w+')
f.write("Energy\tDrain\tFlou\n")
for j in range (0,len(x)):
    f.write("%f \t %f \t %f \n" %(x[j],y[j],y1[j]))
f.close()

oldPos = rWD.get_nexus_meta("/emy/emy")
oldEnergy = rWD.get_nexus_meta("/pgm_energy/pgm_energy")

plt.show()
        
