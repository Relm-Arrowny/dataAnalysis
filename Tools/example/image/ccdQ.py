'''
Created on 7 Dec 2023

@author: wvx67826
'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

beamCen = [1023,984]
tthRange = 11.5865705
pixDeg   = tthRange/2048
dz = 400
dx = 400
th = 20
wLen = 12.4/0.708
imLocP ="Z:/2023//mm35196-1//800838-pimte-files//pimte-00000.tiff"
imLocN ="Z:/2023//mm35196-1//800839-pimte-files//pimte-00000.tiff"


imP = Image.open(imLocP)
imN = Image.open(imLocN)
imarrayP = np.array(imP)[beamCen[0]-dz:beamCen[0]+dz,beamCen[1]-dx:beamCen[1]+dx]
imarrayN = np.array(imN)[beamCen[0]-dz:beamCen[0]+dz,beamCen[1]-dx:beamCen[1]+dx]
imdif    = imarrayP-imarrayN

thArr = np.array([])
omegaArr = np.array([]) 
imdifArr = np.array([])
x = np.array(range(-dx,dx))*pixDeg
for cter, z in enumerate (range(-dz,dz)):
    tth       = 4.0*np.pi/wLen*(np.cos(np.deg2rad((th*2.0 - z*pixDeg)-th)) - np.cos(np.deg2rad(th)))\
                -4.0*np.pi/wLen*(np.cos(np.deg2rad((th*2.0)-th)) - np.cos(np.deg2rad(th)))
    
    thArr    = np.append(thArr   , np.full((1,dz*2),tth))
    omegaArr = np.append(omegaArr, np.full((1,dx*2),4*np.pi/wLen*np.sin(np.deg2rad(x))))
    imdifArr = np.hstack((imdifArr, imdif[cter]))

plt.figure(1)
plt.ylim(-0.009, 0.009)
plt.xlim(-0.009, 0.009)
plt.tricontourf(thArr, omegaArr , imdifArr,30, cmap=plt.get_cmap('jet'))
plt.gca().set_aspect('equal')
plt.figure(2)
plt.imshow(imdif)
plt.show()
