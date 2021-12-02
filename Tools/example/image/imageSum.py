'''
Created on 2 Dec 2021

@author: wvx67826
'''

#I10 special to load data
from Tools.ReadWriteData import ReadWriteData
#deal with images
from PIL import Image
import numpy as np
from matplotlib.colors import LogNorm
import re
import time
from os import listdir

Rd = ReadWriteData()
#data folder location
folder = "Z:\\2021\mm28915-1\\"
scanStart = 675968
scanEnd =  675971

for scanNo in range(scanStart,scanEnd):
    imarray = np.zeros((2048,2048), dtype = int)
    imageDir = folder + "%i-pixis-files\\" %scanNo
    #try and only load file if the folder exist
    try:
        arImage =  np.array(listdir(imageDir))
        
        for imPath in arImage:
            
            im = Image.open(imageDir+imPath)
            imarray = imarray + np.array(im)/arImage.size
        saveImage = Image.fromarray(imarray)
        saveImage.save(folder +"\\processing\\%i_SUMMED.tiff" %scanNo)
        print ("%i" %scanNo)
        
    except FileNotFoundError:
        print ("I do not care %i" %scanNo)
        
        




        

    