# Bruno Dutra

import matplotlib.pyplot as plt
import serial
import time
import numpy as np
var=0.0;
def start(port,baud):
    port=str(port)
    global ser
    ser= serial.Serial(port,baud, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
    
    #2000000

    time.sleep(2.5)
    ser.write(bytearray(str(0),'ascii'))

def write(val,Ts):
    val=round(val, 2)
    ser.write(bytearray(str(val),'ascii'))
    time.sleep(Ts);
    
def read():
        # Str=ser.readline();
        var=float(ser.readline().rstrip().decode())
        ser.flushInput()
        # #print(Str)
        # global var
        # if len(Str)>4:
        #     try:
        #          v=Str
        #          var=float(v)
        #     except ValueError:
        #          print ("Oops! erro")
     
           
        return(var)
def readStr():

      try:
         Str=str((ser.readline().rstrip()),'ascii');

      except ValueError:
        print ("Oops! erro")
        Str=" "
        
      return(Str)
def fastRead():

      try:
          bytesToRead = ser.inWaiting()
         # print (bytesToRead)
          Str=str((ser.read(191).rstrip()),'ascii');
        # Str=str((ser.readline().rstrip()),'ascii');
        
      except ValueError:
        print ("Oops! erro")
        Str=" "

      return(Str)    
    
def end():
    ser.write(bytearray(str(0),'ascii'))
    ser.close();
     
