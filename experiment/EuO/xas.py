'''
Created on 8 Oct 2021

@author: wvx67826
'''
657039

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

folder ="\\\data.diamond.ac.uk\\i10\\data\\2021\\cm28168-4\\i10-"

rWD.read_nexus_data(folder, 657039)
x = rWD.get_nexus_data("\mcs17\data")
y = rWD.get_nexus_data("\energy\energy")

plt.figure()
plt.plot(x,y)
plt.show()