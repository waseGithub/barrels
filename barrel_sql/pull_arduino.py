import serial
from serial import SerialException
import time
import csv
import os
import pandas as pd
import numpy


import serial.tools.list_ports
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

import re
import subprocess
import pandas as pd 
#import dictpy

device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")
devices = []

line1 = None
line2 = None
line3 = None 
line4 = None 





     
       


ports = serial.tools.list_ports.comports(include_links =False)
ls = []
for port in ports:
    print(port.device)
    ls.append(port.device)
   
print(ls)


import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

Megas = []

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        if '2341:0042' in hwid:
          print('Requested device found mega 1')
          print(port)
          Megas.append(port)
        elif '2341:0042' in hwid:
         print('Requested device found mega 2')
         print(port)
         Megas.append(port)
        elif '2341:0042' in hwid:
          print('Requested device found mega 3')
          print(port)
          Megas.append(port)
        elif '2341:0042' in hwid:
          print('Requested device found mega 4')
          print(port)
          Megas.append(port)

        elif '2341:0042' in hwid:
          print('Requested device found mega 3')
          print(port)
          Megas.append(port)
        elif '2341:0042' in hwid:
          print('Requested device found mega 4')
          print(port)
          Megas.append(port)

      
          
print('Megas as port:')          
print(Megas)

         
           

ser1 = serial.Serial(str(Megas[0]),  9600, timeout = 25)
ser2 = serial.Serial(str(Megas[1]),  9600, timeout = 25)
ser3 = serial.Serial(str(Megas[2]),  9600, timeout = 25)
ser4 = serial.Serial(str(Megas[3]),  9600, timeout = 25)
print("channels correct")
    
time.sleep(5)

if __name__ == '__main__':
    
   

    ser1.flush()
    ser2.flush()
    ser3.flush()
    ser4.flush()


    i = 0

   
    while True:
         ser1.flush()
         ser2.flush()
         ser3.flush()
         ser4.flush()
         print('sql script')
         i +=1
         print('Current count =')
         print(i)
         try:
            if ser1.in_waiting > 0:
                
                line1 = ser1.readline().decode("utf-8")
                
                
                with open ("Sensor_A.csv","a") as f:
                    
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow([time.asctime(),line1])

                    

            if ser2.in_waiting > 0:
            
                line2 = ser2.readline().decode("utf-8")
                
                
                with open ("Sensor_B.csv","a") as f:
                    
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow([time.asctime(),line2])
                    
                    
                    
            if ser3.in_waiting > 0:
            
                line3 = ser3.readline().decode("utf-8")
            
                
                with open ("Sensor_C.csv","a") as f:
                    
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow([time.asctime(),line3])
            
                    
            if ser4.in_waiting > 0:
            
                line4 = ser4.readline().decode("utf-8")
            
                
                with open ("Sensor_D.csv","a") as f:
                    
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow([time.asctime(),line4])
            
           
            print('writing data')
            print(Megas[0])
            print(line1) 
            print(Megas[1])
            print(line2)
            print(Megas[2])
            print(line3)
            print(Megas[3])
            print(line4)

         except UnicodeDecodeError:
             pass

                
  