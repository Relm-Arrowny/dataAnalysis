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

lScanable = ["mcsh16/energyh", "/mcsh16/data", "/mcsh17/data",  "/mcsh18/data"]
lMetaName = ["/instrument/id/polarisation",
                "/instrument/ips/field_set_point",
                "/instrument/itc3_device/sensor_temp",
                "/instrument/hfm/x",
                "/instrument/hfm/y",
                "/instrument/hfm/pitch",]
#folder = "C:\\Users\\wvx67826\\Desktop\\New folder\\data\\i10-"#-pixis-files
#To get the polarisation details

folder ="C:\\Users\\wvx67826\\Desktop\\data_nexus\\i10-"
output = "C:\\Users\\wvx67826\\Desktop\\EuO\\"

scanNoStart = 692510
plt.figure()
k = rWD.read_nexus_data(folder, scanNoStart)
y = rWD.get_nexus_data("/mcsh17/data")
y1 = rWD.get_nexus_data("/mcsh16/data")
x = rWD.get_nexus_data("/energyh/pgm_energy")
plt.plot(x,y/y1)
scanNoStart = 69251192793
k = rWD.read_nexus_data(folder, scanNoStart)
y = rWD.get_nexus_data("/mcsh17/data")
y1 = rWD.get_nexus_data("/mcsh16/data")
x = rWD.get_nexus_data("/energyh/pgm_energy")

plt.plot(x,y/y1)
plt.show()
