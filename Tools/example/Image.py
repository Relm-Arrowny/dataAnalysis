'''
Created on 23 Aug 2019

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
import matplotlib.pylab as plt
import matplotlib.image as mpimg
import matplotlib
import numpy as np
from Tools.Output.Output import Output
import time
op = Output()
op.add_clipboard_to_figures()
start = time.time()

Rd = ReadWriteData()

folder = "Z:\\2021\cm28168-4\\i10-"
scanStart = 657406
scanEnd =  657408
#k = Rd.get_nexus_data("/hkl_ccd/k")


for scanNo in range(scanStart,scanEnd):
    
    Rd.read_nexus_data(folder, scanNo)
    arImage = Rd.get_nexus_data("/pixis/data")
    plt.figure()
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 32}

    matplotlib.rc('font', **font)
    #plt.imshow(im, vmin=200, vmax=1000)
    plt.imshow(arImage[0], vmin=2000, vmax=20000 )
    
    plt.colorbar()
    plt.savefig("%i.jpg" %scanNo)
plt.show()
    
    
