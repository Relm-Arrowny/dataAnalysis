'''
Created on 9 Oct 2020

@author: wvx67826
'''

from Tools.ReadWriteData import ReadWriteData

rd = ReadWriteData()

folder = "Z:\\2020\\cm26456-4\\i10-"#-pixis-files
output = "C:\\Users\\wvx67826\\Desktop\\i11_powder_2\\"
lfilename =  range(610359, 610361,1)   # 563001
for i,k in enumerate(lfilename):
    rd.read_nexus_data(folder, k)
    en=rd.get_nexus_meta("/pgm_energy/pgm_energy")
    tth=rd.get_nexus_meta("/tth/tth")
    print ("%i,%.2f,%i" %(k,en,tth))