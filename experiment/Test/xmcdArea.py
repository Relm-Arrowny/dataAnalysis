'''
Created on 15 Feb 2023

@author: wvx67826
'''

from Tools.ReadWriteData import ReadWriteData
from Tools.AreaDetector.ImageAnalysis import ImageAnalysis
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib.animation as animation
ima= ImageAnalysis()
rd = ReadWriteData()

folder ="\\\data.diamond.ac.uk\\i10\\data\\2023\\mm31510-1\\i10-"

filename =  749582   # 350k 537521
imlist = []
imcorr = []
imdiff = []
imcrosscorr = []
picture = []
picture2 = []
picture3 = []
rd.read_nexus_data(folder, filename)
#time = rd.get_nexus_data("/t/t")

imfile = rd.get_nexus_image_filename ()
print(imfile[0])
#Image.open("\\\data.diamond.ac.uk\\i10\\data\\2023\\mm31510-1\\749582-pimte-files\\pimte-00000.tiff")
im = Image.open("\\\data.diamond.ac.uk\\" +imfile[0].decode("utf-8")[5:].replace("/","\\"))
imarray = np.array(im)
imlist.append(imarray[:,500:1500])#imarray[1180:1260,820:940])
plt.imshow(imlist[0])
plt.show()
im.close()

"""
for i, k in enumerate (imfile[0:-1:1]):        
    temp = "//dc" +k#.split('/dls')[1]
    print (temp)
    im = Image.open(temp)
    imarray = np.array(im)
    print (imarray[0][0])
    imlist.append(imarray[:,500:1500])#imarray[1180:1260,820:940])
    im.close()

for i, k in enumerate (imlist):
    imcorr.append(ima.corr_r(imlist[0], k))
    imcrosscorr.append( ima.cross_correlation(imlist[0],k))
    imdiff.append( ima.im_dif(imlist[0],k))
    fig1 = plt.figure(1)
    picture.append((plt.imshow(k,vmin=600,vmax= 6000),))
    fig2 = plt.figure(2)
    picture2.append((plt.imshow(imcrosscorr[i]),))
    fig3 = plt.figure(3)
    #plt.colorbar(mappable, cax, ax)
    picture3.append((plt.imshow(imdiff[i]),))

im_ani = animation.ArtistAnimation(fig1, picture, interval=1000, repeat_delay=3000, blit=True)
#im_ani.save('537542.mp4')
im_ani2 = animation.ArtistAnimation(fig2, picture2, interval=1000, repeat_delay=3000, blit=True)
#im_ani.save('537542cc.mp4')
im_ani3 = animation.ArtistAnimation(fig3, picture3, interval=1000, repeat_delay=3000, blit=True)
#im_ani.save('537542cc.mp4')
plt.show()
"""