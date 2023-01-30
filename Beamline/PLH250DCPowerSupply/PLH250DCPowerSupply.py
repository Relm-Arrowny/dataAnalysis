'''
Created on 30 Jan 2023

@author: wvx67826


@deprecated: 
    Python class to connect and control PLH250P DC power supply
     user manual: https://resources.aimtti.com/manuals/PLH+PLH-P_Instruction_Manual-Iss6.pdf
@version: 1.0 
    class take two optional parameters, buffer size for the readout and a connection time out in seconds 

        
    get/set command:
       setVoltageAmp(self, v : float) : bool
       getVoltage(self) : String
'''
from Beamline.TCPSocket.TCPSocket import TCPSocket
class PLH250DCPowerSupply(TCPSocket):
    def __init__(self, bufferSize = 4096, timeout = 5):
        super().__init__(bufferSize, timeout)
        


#================== Set Voltage ==============================================================
    """ Set Voltage 
        return true /false
    """
    def setV(self, channel, value):
        com = "V%s %s" %(channel, value) 
        return self.sendCom(com)

#================== Set Voltage ==============================================================
    """ get Voltage
        return voltage
    """
    def getV(self, channel):
        com = "V%s?" %channel
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "Heater readback failed"
        
#================== Set Current ==============================================================
    """ set Current
        return true /false
    """
    def setI(self, channel, value):
        com = "I%s %s" %(channel, value) 
        return self.sendCom(com)

#================== Set Voltage ==============================================================
    """ get Current
        return voltage
    """
    def getI(self, channel):
        com = "I%s?" %channel
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "Heater readback failed"
        
        
#============= Output On/Off =================================
    """ output on/off
        1 is on 0 is off
        return true /false
    """
    def setOutPut(self, channel, value):
        com = "OP%s %s" %(channel, value) 
        return self.sendCom(com)


ps250 = PLH250DCPowerSupply()
ps250.connection("172.23.110.128", 9221)
ps250.setV(1, 50)
ps250.sendCom("V1?")
ps250.setOutPut(1, 0)
ps250.setI(1,5e-3)
print(ps250.readBuffer())
print(ps250.getI(1))



ps250.closeConnection()