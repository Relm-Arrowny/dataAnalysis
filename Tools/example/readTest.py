'''
Created on 25 Aug 2021

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
import matplotlib.pyplot as plt

folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-3\\i10-"
rWD = ReadWriteData()

scanNoStart = 655780
rWD.read_nexus_data(folder, scanNoStart)
x = rWD.get_nexus_data("/energy/energy")
y = rWD.get_nexus_data("/mcs17/data")
y = rWD.get_nexus_meta("/chi/chi")
plt.figure()
plt.plot(x,y)
plt.show()
rWD.write_ascii("filename.dat", ["energy", "det"], [x,y])

print(x)