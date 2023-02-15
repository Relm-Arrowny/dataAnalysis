'''
Created on 30 Jan 2023

@author: wvx67826


@deprecated: 
    Python class to connect and control PLH250P DC power supply
     user manual: https://resources.aimtti.com/manuals/PLH+PLH-P_Instruction_Manual-Iss6.pdf
@version: 1.0 
    class take two optional parameters, buffer size for the readout and a connection time out in seconds 

    Setup:
    
        ps250 = PLH250DCPowerSupply() # create object
        ps250.connection("172.23.110.128", 9221) connet to power supply
        

    get/set command:
       setV(self, v : float) : bool
       getV(self) : String
       setI(self, v : float) : bool
       getI(self) : String
       setOutPut(self, v : float) : bool
       getOutPut(self) : String
           
'''
from Beamline.TCPSocket.TCPSocket import TCPSocket
class PLH250DCPowerSupply(TCPSocket):
    def __init__(self, bufferSize = 256, timeout = 5):
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
#============= Output On/Off ?? =================================
    """ get on/off
        1 is on 0 is off
        return true /false
    """
    def getOutPut(self, channel):
        com = "OP%s?" %(channel) 
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "Heater readback failed"

#test#
if __name__ == "__main__":
    import time
    ps250 = PLH250DCPowerSupply()
    ps250.connection("172.23.110.128", 9221)
    ps250.setV(1, 25)
    print(ps250.getOutPut(1))
    
    ps250.setOutPut(1, 1)
    print(ps250.getOutPut(1))
    ps250.setI(1,10e-3)
    print(ps250.getI(1))
    print(ps250.getV(1))
    time.sleep(10)
    ps250.setOutPut(1, 0)
    print(ps250.getOutPut(1))
    ps250.closeConnection()