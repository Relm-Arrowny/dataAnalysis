'''
Created on 9 Dec 2021

@author: wvx67826
'''
from Tools.ReadWriteData import ReadWriteData
dr = ReadWriteData()
import numpy as np
import re
import time
from os import listdir

def scanTypeToData(folder, scanNo, output):
    dr.read_nexus_data(folder, scanNo)
    scanType = dr.get_scan_type(subBranch = "/scan_command", nData = 0, mainBranch ="/entry/diamond_scan" )
    print (scanType)
    if scanType[-6:] == "energy":
        temperature = dr.get_nexus_data("/lakeshore340/Channel0Temp", mainBranch ="/entry/instrument")
        energy = dr.get_nexus_data("/energy/value", mainBranch ="/entry/instrument")
        det16 = dr.get_nexus_data("/mcs16/data", mainBranch ="/entry/instrument")
        det17 = dr.get_nexus_data("/mcs17/data", mainBranch ="/entry/instrument")
        det18 = dr.get_nexus_data("/mcs18/data", mainBranch ="/entry/instrument")
        det19 = dr.get_nexus_data("/mcs19/data", mainBranch ="/entry/instrument")
        th = dr.get_nexus_data("/rasor/diff/theta", mainBranch ="/entry/instrument")
        tth = dr.get_nexus_data("/rasor/diff/2_theta", mainBranch ="/entry/instrument")
        ldata = np.vstack((energy, det16, det17, det18, det19))
        sx = dr.get_nexus_data("/rasor/cryo/x", mainBranch ="/entry/instrument")
        sz = dr.get_nexus_data("/rasor/cryo/z", mainBranch ="/entry/instrument")
        dataName = ["energy", "IO", "det", "flou(offset tth+60)", "Drain"]
        metaName = ["Temperature", "sx" ,"sy", "tth", "th" ]
        meta = [temperature,sx,sz,tth, th]
        
        dr.write_ascii(output+"EScan_%s.dat" %(scanNo), dataName, ldata, metaName, meta )
    elif scanType == "th":
        energy = dr.get_nexus_data("/pgm/energy", mainBranch ="/entry/instrument") 
        try:
            th = dr.get_nexus_data("/th/value", mainBranch ="/entry/instrument")
        except:
            th = dr.get_nexus_data("/rasor/diff/theta", mainBranch ="/entry/instrument")
        try:
            tth = dr.get_nexus_data("/tth/value", mainBranch ="/entry/instrument")
        except:         
            tth = dr.get_nexus_data("/rasor/diff/2_theta", mainBranch ="/entry/instrument")
        temperature = dr.get_nexus_data("/lakeshore340/Channel0Temp", mainBranch ="/entry/instrument")
        sx = dr.get_nexus_data("/rasor/cryo/x", mainBranch ="/entry/instrument")
        det =  dr.get_nexus_data("/rdeta/rnormdet", mainBranch ="/entry/instrument")
        if tth.size>2:
            ldata = np.vstack((th,tth,det))
            dataName = ["th", "tth", "det"]
            metaName = ["Temperature", "sx"]
            meta = [temperature,sx]
            dr.write_ascii(output + "Th2th_%s.dat" %(scanNo), dataName, ldata, metaName, meta )
            
        else:
            ldata = np.vstack((th,det))
            dataName = ["th", "det"]
            metaName = ["Temperature", "sx"]
            meta = [temperature,sx]
            dr.write_ascii(output+"Th_%s.dat" %(scanNo), dataName, ldata, metaName, meta )
        
        
        
        
#scanNo = 676854
output = "Z:\\2021\\mm28741-1\\processing\\"   
folder = "Z:\\2021\\mm28741-1\\"

newScanNo = 678234
lastScanNo = 678233
timeOut = 0
while timeOut < 24*3600:
    if newScanNo == lastScanNo:
        try:
            #lastScanNo = int(re.split("-|.nxs" ,sorted([f for f in listdir(folder) if f.endswith('.nxs')]) [-1])[1])
            #print (lastScanNo)
            if timeOut>180:
                scanTypeToData(folder+ "i10-", newScanNo, output)
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
        for scanNo in range(lastScanNo,newScanNo):
            scanTypeToData(folder + "i10-", scanNo, output)
        lastScanNo = newScanNo


















