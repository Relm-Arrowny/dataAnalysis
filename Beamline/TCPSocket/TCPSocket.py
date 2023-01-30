'''
Created on 18 Nov 2022

@author: Relm Arrowny

@deprecated: 
    Python class to connect, send and receive command 

@version: 1.0 
    class take two optional parameters, buffer size for the readout and a connection time out in seconds

'''
import socket
class TCPSocket():
    
    def __init__(self, bufferSize = 4096, timeout = 5):
        self.timeout = 5; # connection time out in second
        self.LakeshoreSocket = None; #this will store the connection socket
        self.input_buffer = bufferSize #who much to read off
    
    #========= this will set up connection ================================================
    def connection(self, ip, port):
        try:
            self.LakeshoreSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            self.LakeshoreSocket.connect((ip, port));
            self.LakeshoreSocket.settimeout(self.timeout);
        except:
            print("Failed to connect")
            return False
        return True
    #======= Close connection =============================================================
    def closeConnection(self):
        try:
            self.LakeshoreSocket.close();
            self.LakeshoreSocket = None
        except:
            print("Failed to close connect")
            return False
        return True
    
    #============= This will send command ===================================================
    """ This function take one String parameter
    
        Covert string to byte and send it to the sever 
    """
    def sendCom(self, com):
        try:
            self.LakeshoreSocket.send(com.encode("utf_8") + b'\n') #convert the string into byte and send it
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
            buffer = self.LakeshoreSocket.recv(self.input_buffer); #convert the string into byte and send it
            return buffer.decode("utf_8")
        except:
            print("Buffer read failed")
            return "Read Failed"
        



