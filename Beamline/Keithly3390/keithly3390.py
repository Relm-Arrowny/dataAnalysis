'''
Created on 29 Sep 2022

@author: wvx67826

@deprecated: 
    Python class to connect and control Keithly3390 
     user manual: https://mfile.tek.com.cn/drupal/51107028-1190-43e5-86c9-c623ff63e174.pdf 
@version: 1.0 
    class take two optional parameters, buffer size for the readout and a connection time out in seconds
    
   
    Connect via TCP, port for the keithly is 5025:
        connection(self, ip : String, port: int) : bool
        closeConnection(self) : bool
    
    Send command:
        __sendCom(self, com : String) : bool
        readBuffer(self) : String
        
    get/set command:
       setVoltageAmp(self, v : float) : bool
       getVoltage(self) : String
'''
import socket

class Keithly3390():
    def __init__(self, bufferSize = 2048, timeout = 5):
        self.timeout = 5; # connection time out in second
        self.k3390Socket = None; #this will store the connection socket
        self.input_buffer = bufferSize #who much to read off
    
    #========= this will set up connection
    def connection(self, ip, port):
        try:
            self.k3390Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            self.k3390Socket.connect((ip, port));
            self.k3390Socket.settimeout(5);
        except:
            print("Failed to connect")
            return False
        return True
    #======= Close connection =============================================================
    def closeConnection(self):
        try:
            self.k3390Socket.close();
            self.k3390Socket = None
        except:
            print("Failed to close connect")
            return False
        return True
    
    #============= This will send command ===================================================
    """ This function take one String parameter/keithly command
    
        Covert string to byte and send it to the Keithly
    """
    def __sendCom(self, com):
        com = com  + "\n"
        try:
            self.k3390Socket.send(com.encode("utf_8")) #convert the string into byte and send it
        except:
            print("Sending failed.")
            return False
        return True
    
    #============= This will read keithly buffer ===================================================
    """ This function take no parameter
        Return buffer as string
        
        Read buffer and convert byte to string and return  
         
    """
    def readBuffer(self):
        try:
            buffer = self.k3390Socket.recv(self.input_buffer); #convert the string into byte and send it
            return buffer.decode("utf_8")
        except:
            print("Buffer read failed")
            return "Read Failed"
        
    #================== Set Voltage ==============================================================
    """ Take a number and set peak to peak voltage
        return true /false
    """
    def setVoltageAmp(self, v):
        if ( float(v) > 10 or float(v)<1e-2): 
            print ("Voltage beyond limit (10mV to 10V")
            return False
        com = "VOLTage %f" %v
        return self.__sendCom(com)
        
        
    #============= get voltage ==================================================================
    """ Take no parameter
        return a string contain voltage
    """
    def getVoltage(self):
        com = "VOLTage?"
        if (self.__sendCom(com)):
            return self.readBuffer()
        else:
            return "Voltage readback failed"
        


 #============== Functions written by Matt, check these work =================================

    #================== Trigger ==============================================================

    def trigger(self):

        com = "*TRG"

        if (self.sendCom(com)):

            return True
        
        else:

            return False


    #=============== Voltage

    #================== Set Voltage Low ==============================================================

    """ Take a number and set voltage low limit
        return true /false
    """

    def setVoltageLow(self, v):

        com = "VOLTage:LOW %f" %v

        if (self.sendCom(com)):

            return True

        else:

            return False

    #============= get voltage low ==================================================================

    """ Take no parameter
        return a string contain voltage
    """

    def getVoltageLow(self):

        com = "VOLTage:LOW?"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "Voltage readback failed"




    #================== Set Voltage High ==============================================================

    """ Take a number and set voltage high limit
        return true /false
    """

    def setVoltageHigh(self, v):

        if ( float(v) > 10 or float(v)<1e-2):

            print ("Voltage beyond limit (10mV to 10V")

            return False

        com = "VOLTage:HIGH %f" %v

        if (self.sendCom(com)):

            return True

        else:

            return False

    
    #============= get voltage high ==================================================================

    """ Take no parameter
        return a string contain voltage
    """

    def getVoltageHigh(self):

        com = "VOLTage:HIGH?"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "Voltage readback failed"




    #=============== Pulse width

    #============= get pulse width ==================================================================

    """ Take no parameter
        return a string contain pulsewidth
    """

    def getPulsewidth(self):

        com = "FUNCtion:PULSe:WIDTh?"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "Pulsewidth readback failed"

    #============= set pulse width ==================================================================

    """ Take a number and set pulsewidth
        return true /false
    """

    def setPulsewidth(self, w):

        if ( float(w) > 2000 or float(w)<20e-9):

            print ("Pulsewidth beyond limit (20ns to 2000s")

            return False

        com = "FUNCtion:PULSe:WIDTh %f" %w

        if (self.sendCom(com)):

            return True

        else:

            return False

    
    #=============== Period

    #============= get period ==================================================================

    """ Take no parameter
        return a string contain period
    """

    def getPeriod(self):

        com = "PULSe:PERiod?"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "Period readback failed"

    #============= set period ==================================================================

    """ Take a number and set period
        return true /false
    """

    def setPeriod(self, w):

        if ( float(w) > 2000 or float(w)<100e-9):

            print ("Period beyond limit (100ns to 2000s")

            return False

        com = "PULSe:PERiod %f" %w

        if (self.sendCom(com)):

            return True

        else:

            return False

        
    #=============== Pulse shape

    #============= get PWM Function ==================================================================

    def getPWMFunction(self):

        com = "PWM:INTernal:FUNCtion?"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "PWM:Function readback failed"


    #============= set PWM Function ==================================================================

    """ Takes a string function from {SINusoid, SQUare, RAMP, NRAMp, TRIangle}
        return True/False
    
    """
    def setPWMFunction(self, func):

        com = "PWM:INTernal:FUNCtion %s" %func

        if (self.sendCom(com)):

            return True

        else:
            
            return False


    #============= get PWM frequency ==================================================================

    """ Take no parameter
        return a string contain PWM frequency
    """
    def getPWMFrequency(self):

        com = "PWM:INTernal:FREQuency"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "Pulsewidth readback failed"

    #============= set PWM Frequency ==================================================================

    """ Take a number and set PWM Frequency
        return true /false
    """

    def setPWMFrequency(self, f):

        if ( float(f) > 20e3 or float(f)<2e-3):

            print ("PWM Frequency beyond limit (20mHz to 20KHz")

            return False

        com = "PWM:INTernal:FREQuency %f" %f

        if (self.sendCom(com)):

            return True

        else:

            return False


        
    #============= get duty cycle ==================================================================

    """ Take no parameter
        return a string contain duty cycle
    """

    def getDutyCycle(self):

        com = "FUNCtion:PULSe:DCYCle"

        if (self.sendCom(com)):

            return self.readBuffer()

        else:

            return "Pulsewidth readback failed"

    #============= set duty cycle ==================================================================

    """ Take a number and set duty cycle
        return true /false
    """

    def setDutyCycle(self, percent):

        if ( float(percent) > 1000 or float(percent)<0):

            print ("PWM Frequency beyond limit (20mHz to 20KHz")

            return False

        com = "FUNCtion:PULSe:DCYCle %f" %percent

        if (self.sendCom(com)):

            return True

        else:

            return False

