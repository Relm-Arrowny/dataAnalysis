"""
Created on 18 Nov2022

@author: wvx67826

@deprecated: 
    Python class to connect and control Laksshore 336 
     user manual: https://www.lakeshore.com/docs/default-source/product-downloads/336_manual0ebc9b06cbbb456491c65cf1337983e4.pdf?sfvrsn=2e8633a3_1
@version: 1.0 
    class take two optional parameters, buffer size for the readout and a connection time out in seconds 

        
    get/set command:
       setVoltageAmp(self, v : float) : bool
       getVoltage(self) : String

"""

from Beamline.TCPSocket.TCPSocket import TCPSocket

class Lakeshore336(TCPSocket):
    def __init__(self, bufferSize = 4096, timeout = 5):
        super().__init__(bufferSize, timeout)
        
    

#================== Get Temperature ==============================================================
    """ Get Temperature take 1 parameter, the sensor channel
        return temperature 
    """
    def GetTemp(self, channel):
        com = "KRDG?%s" %channel
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "Temperature readback failed"

#================== Get Temperature Setpoint==============================================================
    """ Get set point Temperature, take 1 parameter, channel setpoint
        return temperature setpoint
    """
    def GetSetTemp(self,channel):
        com = "SETP?%s" %channel
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "Temperature readback failed"

#================== Set Temperature Setpoint==============================================================
    """ Set Temperature
        return true /false
    """
    def SetTemp(self, channel, value):
        com = "SETP%s,%s" %(channel,value) 
        return self.sendCom(com)

#================== Get Pid ==============================================================
    """ Get PID take 1 parameter, the sensor channel
        return "P, I, D" in one string
    """
    def GetPID(self, channel):
        com = "PID?%s" %channel
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "PID readback failed"

#================== Set PID==============================================================
    """ Set PID take 4 parameters, channel, p, i, d 
        return true /false
    """
    def SetPID(self, channel, p, i,d):
        com = "PID%s,%s,%s,%s" %(channel, p, i, d) 
        return self.sendCom(com)

#================== Get Heater power ==============================================================
    """ Get heater power take 1 parameter, the heater channel
        return heater power
    """
    def GetHeater(self, channel):
        com = "MOUT?%s" %channel
        if (self.sendCom(com)):
            return self.readBuffer().strip()
        else:
            return "Heater readback failed"

#================== Set Heater ==============================================================
    """ Setheater power 
        return true /false
    """
    def SetHeater(self, channel, value):
        com = "MOUT%s,%s" %(channel, value) 
        return self.sendCom(com)




    

ls336 = Lakeshore336()
ls336.connection("172.23.110.186", 7777)
ls336.SetPID(1, 130, 50, 0)
ls336.SetTemp(1, 300)
ls336.SetHeater(1, 0)
print("Temperature = %s, Temperature Set = %s" %(ls336.GetTemp("c"), ls336.GetSetTemp(1)) )
print("PID = %s, power out= %s" %(ls336.GetPID(1), ls336.GetHeater(1) ))

ls336.closeConnection()


