'''
Created on 19 Jul 2017
@author: wvx67826


@Description :
    Read and write data. For NEXUS and diamond old ascii format. The read function will read data 
    into memory and get function will get the data requested and store in an array. 
     
    For ascii format:
        Read_file(filename)    
        get_meta_value(self, metaName):
        get_data(self):
        return ascii formate data

    Nexus format:
        read_nexus_data(self,folder, filename):
        get_nexus_meta(self, subBranch, nData = 0, mainBranch ="/entry1/before_scan"):
        get_nexus_data(self, subBranch, nData = 0, mainBranch ="/entry1/instrument" ):
        get_scan_type(self, subBranch = "/scan_command", nData = 0, mainBranch ="/entry1" ):
        get list of data 
    Data output:
    write_ascii(self, filename, names, data)
        write data to file
        file name = output file name
        names is a list of name for the column data
        list of data 

    version 2:
        diamond change the NEXUS format and nexus2ascii no longer functional.
        update for the new NEXUS format.

'''
import numpy as np
import h5py    # HDF5 support
import os
from astropy.io import ascii
from PIL import Image

class ReadWriteData():
    def __init__(self):
        self.metadata = []
        self.data = []
        self.nexusData = []
#============================= old ascii format=======================================
    def read_file(self, filename, meta = True, metaStopKey = "&END"):
        with  open(filename,'r') as f:
            tMeta = []
            tData = []
            # break up the meta and data
            for line in f:
                if meta: tMeta.append(line) 
                if not meta:
                    tData.append(line)
                if metaStopKey in line:
                    meta = False
            self.metadata = tMeta
            self.data = tData
            
    def get_meta_value(self, metaName):
        for line in self.metadata:
            if metaName in line:
                if line.split("=",1)[0] == metaName: return float(line.split("=",1)[1])
                 
    def get_data(self):
        return ascii.read(self.data, delimiter='\t')
    

#============================= nexus =============================================
    #This load data to memory
    def read_nexus_data(self,folder, filename):
        self.nexusData = h5py.File(str(folder)+ str(filename) + '.nxs',  "r")
        return self.nexusData
    
    #This will get the meta data branch and return its value
    #set nData to a h5py object to read data outside class, otherwise it will read object store in self.nexusData
    #It will require the name of the scanable
    #No longer needed/required as they removed before scan in the nexus 
    def get_nexus_meta(self, subBranch, nData = 0, mainBranch ="/entry1/before_scan"):
        
        if nData == 0:
            nData = self.nexusData
        return nData[(mainBranch + subBranch)][()]
        
    #Get the actually data mainBranch is set for the current Neuxs format
    #requires scanable name. 
    def get_nexus_data(self, subBranch, nData = 0, mainBranch ="/entry/instrument" ):
        if nData == 0:
            nData = self.nexusData      
        return nData[(mainBranch + subBranch)][()]
    
    #This return scan command
    def get_scan_type(self, subBranch = "/scan_command", nData = 0, mainBranch ="/entry" ):
        if nData == 0:
            nData = self.nexusData
        temp = nData[mainBranch + subBranch][()].split()[1]          
        return temp

    #This take the filename and up to 4 arrays: names of the scanable, data array, optional metaName and meta array.
    #Out put data in old ascii format
    def write_ascii(self, filename, names, data, metaName = False, meta = False ):
        f = open(filename, 'w+')
        if metaName != False:
            for i in range(len(metaName)):
                f.write("%s = %s" %(metaName[i],meta[i]))
                f.write("\n" )
        for i in names:
            f.write("%s \t" %i)
        f.write("\n" )
        for j in range (0,len(data[0])):
            for k in range (0,len(data)):
                f.write("%.8g \t" %data[k][j])
               
            f.write("\n" )
        f.close()
        
#============== this part is nexus conversion back to ascii============================== 
    def nexus2ascii(self, outPutFilename, metaKey = "entry/diamond_scan/", dataKey = "entry/instrument/",
                     redundantKeyList = ["monochromator","name","source","description","id", "type","data_file", "local_name","beamline","end_station"]):
        #this effectively does all the conversion and write out the data 
        k = self.nexusData
        metaData = []
        data = []
        names = []
        """
        for key in k[metaKey]:
            meta = "%s%s" %(metaKey, key)
            for key1 in k[meta]:
                meta1  = meta +"/%s" %key1
                metaData.append("%s = %s" %(key1,k[meta1][()] ))
        """
        for key in k[dataKey]:
            tempData = "%s%s" %(dataKey, key)
            # removes key that are redundant 
            if key in redundantKeyList:
                pass
            else:
                
                for key1 in k[tempData]:
                    
                    if key1 in redundantKeyList:
                        pass
                    else:
                        tempData1  = tempData +"/%s" %key1
                        tempName = "%s/%s" %(key, key1)
                        print(k[tempData1])
                        names.append(tempName)
                        data.append(k[tempData1][()])
        f = open(outPutFilename, 'w+')
        for i in metaData:
            f.write("%s\n" %i)   
        for i in names:
            f.write("%s \t" %i)
        f.write("\n" )
        for j in range (0,len(data[0])):
            for k in range (0,len(data)):
                try:
                    f.write("%s \t" %data[k][j])
                except IndexError:
                    f.write("%s \t" %"None")
            f.write("\n" )
        f.close()
        return True
        
    def check_nexus_data(self, folder, outputFolder, filename, beamlineFile = "i10-"): #this part make sure the data exit before converting 
    
        filen = folder+ beamlineFile
        if filename[0:4] == beamlineFile:
            filename = filename[4:-4] #cutting the file name to fit read nexus
        print (filename)
        self.read_nexus_data(filen,filename)
        fulloutputname = "%s%s.dat" %(outputFolder,filename)
        
        self.nexus2ascii(fulloutputname)
        try:
            self.read_nexus_data(filen,filename)
            fulloutputname = "%s%s.dat" %(outputFolder,filename)
            self.nexus2ascii(fulloutputname)
        except:
            print ("failed %s" %filename)
    
    def convert_nexus_ascii(self,scanNo, folder, outputFolder): #this either run the whole folder or a range of scan numbers for conversion
        if isinstance(scanNo, (list,)):
            for filename in scanNo:
                #print filename
                self.check_nexus_data(folder, outputFolder,str(filename) )
    
        if scanNo == folder:
            for filename in sorted(os.listdir(scanNo)):
                tempFilename = "%s%s.dat" %(outputFolder,filename[4:-4])  
                exist = os.path.isfile(tempFilename)
                
                if exist and (os.path.getmtime(tempFilename)-os.path.getmtime(folder+"%s" %filename))>300:
                    pass #' do nothing'
                else:
                    if filename[-4:] == ".nxs": #filter out everything that is not data
                        self.check_nexus_data(folder, outputFolder,str(filename))
#=============================== end of neuus conversion ==========================================================
    
    #This section get image data in either tiff or hdf5 format 
    #Not tested for new nexus format    
    def get_nexus_image_filename(self, subBranch = "/pimtetiff/image_data", nData = None, mainBranch ="/entry" ):
        if nData == None:
            nData = self.nexusData
        temp = nData[mainBranch + subBranch]
        #im = Image.open(temp)
        return temp
    
    def get_nexus_tiff(self, subBranch = "/pixistiff/image_data", nData = None, mainBranch ="/entry1" ):
        if nData == None:
            nData = self.nexusData
        temp = "//data" +nData[mainBranch + subBranch][0].split('/dls')[1]
        #im = Image.open(temp)
        return temp
    def get_single_hdf5_image(self, subBranch = "/pixistiff/image_data", nData = None, mainBranch ="/entry1" ):
        image = np.array( nData[mainBranch + subBranch])
        return image
    
    #save image when went a 2d array is given
    def write_image(self, outPutFilename, data, imageTpye = "TIFF"):
        im = Image.fromarray(data) # float32
        im.save("%s.%s" %(outPutFilename,imageTpye), imageTpye)