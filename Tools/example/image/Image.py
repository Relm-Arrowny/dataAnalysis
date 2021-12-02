'''
Created on 23 Aug 2019

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
import matplotlib.pylab as plt
from PIL import Image
import numpy as np
from Tools.Output.Output import Output
from matplotlib.colors import LogNorm
import time
op = Output()
op.add_clipboard_to_figures()
start = time.time()

Rd = ReadWriteData()

folder = "Z:\\2021\cm28168-4\\i10-"
scanStart = 657404
scanEnd =  657405
#k = Rd.get_nexus_data("/hkl_ccd/k")

plt.figure()

for scanNo in range(scanStart,scanEnd):
    # temperature, field(encm), sx,sz 
    Rd.read_nexus_data(folder, scanNo)
    """    temperature = Rd.get_nexus_meta("/ls340/Channel0Temp")
    sx = Rd.get_nexus_meta("/sx")
    sz = Rd.get_nexus_meta("/sz")
    field = Rd.get_nexus_meta("/emecy1")"""
    
    arImage = Rd.get_nexus_data("/pixis/data")[0]
    
    """    plt.figure()
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 32}
    matplotlib.rc('font', **font)
    """
    print(arImage)
    """    imagePath = arImage#"Z:\\2021\mm28790-1\\%i-pimte-files\pimte-00000.tiff" %scanNo
    im = Image.open(imagePath)
    """
    imarray = np.array(arImage)
    
    imA = imarray#imarray[500:1500,500:1500]
    #plt.imshow(im, vmin=100, vmax=2000,  norm=LogNorm() )
    plt.imshow(imA, norm=LogNorm() )
    #plt.suptitle("T = %.1f, x = %.1f, , z = %.1f field = %.1f" %(temperature, sx, sz, field))
    #plt.savefig("C:\\Users\\wvx67826\\Desktop\\images\\%i.jpg" %scanNo)
plt.show()
    
    
