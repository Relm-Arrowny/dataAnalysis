from Tools.ReadWriteData import ReadWriteData
import matplotlib.pyplot as plt 
from Tools.Output.Output import Output
import numpy as np

dr = ReadWriteData()

op = Output()
op.add_clipboard_to_figures()

folder = "Z:\\2021\\mm28741-1\\i10-"
lEscan = []
lRef = []
lBadScan = []
sRange = range(677753, 677865)


#============================      This part read out the scan numbers for different scans ===============================
for i, scanNo in enumerate (sRange):
    #print scanNo
    if (int(scanNo) in lBadScan):
        print ("Passing escan")
        
    else:
        dr.read_nexus_data(folder, scanNo)
        scanType = dr.get_scan_type(subBranch = "/scan_command", nData = 0, mainBranch ="/entry/diamond_scan" )
        #print (scanType)
        if scanType[-6:] == "energy":
            temperature = dr.get_nexus_data("/lakeshore340/Channel0Temp", mainBranch ="/entry/instrument")
            sx = dr.get_nexus_data("/rasor/cryo/x", mainBranch ="/entry/instrument")
            th = dr.get_nexus_data("/rasor/diff/theta", mainBranch ="/entry/instrument")
            pol = dr.get_nexus_data("/id/polarisation", mainBranch ="/entry/instrument") 
            energy = dr.get_nexus_data("/pgm/energy", mainBranch ="/entry/instrument") 
            temp = "%s,%s,%.2f,%.2f,%.2f,%.2f" %(scanNo, pol, energy, sx, temperature, th) 
            lEscan.append(temp.split(","))
            print ("%s scan: %s" %(scanType, temp))
        if scanType == "sx":
                #print ("alignment scan")
                temp = "alignment"
        if scanType == "th":
            temperature = dr.get_nexus_data("/lakeshore340/Channel0Temp", mainBranch ="/entry/instrument")
            sx = dr.get_nexus_data("/rasor/cryo/x", mainBranch ="/entry/instrument")
                
            pol = dr.get_nexus_data("/id/polarisation", mainBranch ="/entry/instrument") 
            energy = dr.get_nexus_data("/pgm/energy", mainBranch ="/entry/instrument") 
            temp = "%s,%s,%.2f, %.2f,%.2f" %(scanNo, pol, energy, sx, temperature)
            lRef.append(temp.split(","))
            print ("%s scan: %s" %(scanType, temp))
#==========================================================================================================================

output = "Z:\\2021\\mm28741-1\\processing\\"
plt.figure(1)
plt.figure(2)
plt.figure(3)
lTemp = []
ldet = []
ldetTh = []
for i, refScan in enumerate (lRef[:]):
    print (refScan[0])
    
    if int(refScan[0]) in lBadScan:
        print ("Passing escan")
        
    else:
        dr.read_nexus_data(folder,refScan[0])
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
        det =  dr.get_nexus_data("/rdeta/rnormdet", mainBranch ="/entry/instrument")
        if tth.size>2:
            plt.figure(1)
            plt.plot(tth,det-det[0], label='T = %.2fK' %temperature)
            plt.legend()
            lTemp.append(temperature)
            ldet.append(np.sum(det-np.min(det)))
            ldata = np.vstack((th,tth,det))
            dataName = ["th", "tth", "det"]
            metaName = ["Temperature"]
            meta = [temperature]
            #dr.write_ascii(output + "%s.dat" %(refScan[0]), dataName, ldata, metaName, meta )
            
        else:
            plt.figure(2)
            plt.plot(th,det-det[0], label='T = %.2fK' %temperature)
            plt.legend()
            ldetTh.append(np.sum(det-np.min(det)))
            ldata = np.vstack((th,det))
            dataName = ["th", "det"]
            metaName = ["Temperature"]
            meta = [temperature]
            #dr.write_ascii(output+"%s.dat" %(refScan[0]), dataName, ldata, metaName, meta )
            
plt.figure(3)
plt.plot(lTemp,ldet)
plt.figure(4)
plt.plot(lTemp,ldetTh)


for i, escan in enumerate (lEscan[:]):
    print (escan[0])
    if (float(escan[0]) in lBadScan):
        print ("Passing escan")

    else:
        dr.read_nexus_data(folder,escan[0])
        temperature = dr.get_nexus_data("/lakeshore340/Channel0Temp", mainBranch ="/entry/instrument")
        energy = dr.get_nexus_data("/energy/value", mainBranch ="/entry/instrument")
        det16 = dr.get_nexus_data("/mcs16/data", mainBranch ="/entry/instrument")
        det17 = dr.get_nexus_data("/mcs17/data", mainBranch ="/entry/instrument")
        det18 = dr.get_nexus_data("/mcs18/data", mainBranch ="/entry/instrument")
        ldata = np.vstack((energy, det16, det17, det18))
        dataName = ["energy", "IO", "det", "flou(offset tth+60)"]
        metaName = ["Temperature"]
        meta = [temperature]
        #dr.write_ascii(output+"%s.dat" %(escan[0]), dataName, ldata, metaName, meta )

plt.show()
