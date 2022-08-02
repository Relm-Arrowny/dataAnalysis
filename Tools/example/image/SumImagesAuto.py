'''
Created on 2 Dec 2021

@author: wvx67826
'''

#I10 special to load data
from Tools.ReadWriteData import ReadWriteData
#deal with images
from PIL import Image
import numpy as np
import re
import time
from os import listdir


def sumImages(folder,lastScanNo,newScanNo):
    for scanNo in range(lastScanNo,newScanNo+1,1):
        imarray = np.zeros((2048,2048), dtype = int)
        try:
            imageDir = folder + "%i-pixis-files\\" %scanNo
            arImage =  np.array(listdir(imageDir))
            
            for imPath in arImage:
                
                im = Image.open(imageDir+imPath)
                imarray = imarray + np.array(im)/arImage.size
            saveImage = Image.fromarray(imarray)
            saveImage.save(folder +"\\processing\\%i_SUMMED.tiff" %scanNo)
            print ("Summing %i" %scanNo)
    
        except FileNotFoundError:
            print ("I do not care %i" %scanNo)



Rd = ReadWriteData()
#data folder location
folder = "Z:\\2022\mm30601-1\\"
# This part is an infinite loop to keep checking for the latest scan
newScanNo =  713949
lastScanNo = 713940
timeOut = 0
while timeOut < 24*3600:
    if newScanNo == lastScanNo:
        try:
            lastScanNo = int(re.split("-|.nxs" ,sorted([f for f in listdir(folder) if f.endswith('.nxs')]) [-1])[1])
            if timeOut>180:
                sumImages(folder,lastScanNo,newScanNo)
            time.sleep(66.6666666)
            timeOut = timeOut+66.66666666
            newScanNo = int(re.split("-|.nxs" ,sorted([f for f in listdir(folder) if f.endswith('.nxs')]) [-1])[1])
            print ("waiting %i" %newScanNo)
        except FileNotFoundError:
            print("bad %i" %lastScanNo)
            time.sleep(66.6666666)
            timeOut = timeOut+66.66666666
    else:
       
        timeOut = 0
        sumImages(folder,lastScanNo,newScanNo)
        lastScanNo = newScanNo

