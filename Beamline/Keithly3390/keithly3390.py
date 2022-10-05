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
    
        Cover string to byte and send it to the Keithly
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
        return ture /false
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
