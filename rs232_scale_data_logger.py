# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:20:35 2022

@author: dallo
"""
import serial, csv, time
from datetime import datetime

directory = 'C:/Users/dallo/Documents' #Directory for output

filename = None			#Output file name

port = 'COM10'			#Serial port COM# 
baudrate = 9600			#Serial port baudrate 
timeout = 1				#Serial port timeout

start = datetime.now()  #Save running code's start time

log_rate = 0.1			#Time in seconds between readings (this should be faster than the print rate on the scale)

#Open serial port
with serial.Serial(port, baudrate, timeout=timeout, parity=serial.PARITY_ODD,
                       stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS) as ser:

    #Naming file by date
    if filename is None:
        filename = datetime.now().strftime('{}/RS232_%Y-%m-%d-%H-%M.csv'.format(directory))

    #Create a CSV file and record the data in it
    with open(filename,'w', newline='') as f:
        writer = csv.writer(f)
    
        #Write header for CSV file
        writer.writerow(['Time (s)', 'Mass (kg)'])

        #Read data in bytes type from serial port
        while True:
            
            #Read serial data in buffer by line
            data = ser.readline()
            #Calculate the amount of time elapsed since running the script
            elapsed_time = datetime.now() - start
            #Convert elapsed time to seconds
            etm = elapsed_time.total_seconds()
            
            time.sleep(log_rate)
            #Decode serial bytes into a string
            instring = data.decode('utf-8')
            #split string from scale by spaces
            lists=instring.split()

            if len(lists) > 1:
                print(lists[1])
                #Write elapsed seconds and weight from scale into CSV file
                writer.writerow([etm,lists[1]])
