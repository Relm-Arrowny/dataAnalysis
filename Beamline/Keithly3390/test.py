'''
Created on 29 Sep 2022

@author: wvx67826
'''
from keithly3390 import Keithly3390 
import time
input_buffer = 2 * 1024;
 

s = Keithly3390();
s.connection("172.23.110.130", 5025 );
#s.connect();

input_buffer = 2 * 1024;


#cmd = "VOLTage 2e-2"
#s.sendCom(cmd)
s.setVoltageAmp(10e-3)
id = s.getVoltage()
#time.sleep(2)
#cmd = "VOLTage?";
#s.sendCom(cmd)
#s.setVoltage(1e-2)

#id = s.readBuffer();
print (id);


s.closeConnection();
