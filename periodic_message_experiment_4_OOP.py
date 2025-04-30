# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 10:57:05 2025

@author: mnunezcastr
"""

import serial # library used to communicate with serial port
import re # library used to extract data from string
import tkinter as tk
import sys

class WeatherStation(tk.Tk):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, **kwargs):
        super().__init__()
        self.SERIAL_PORT_DEFAULT = 'COM3'
        self.SERIAL_BAUDRATE_DEFAULT = 9600
        self.FILE_NAME_DEFAULT = './data.txt'
        self.geometry("500x200")
        self.title('Weather Station')
        self.resizable(False, False)
        self.btn_quit = tk.Button(master=self, text="Quit", font=50, command=self.close_application)
        self.btn_quit.place(x=230, y=100)
        self.lbl_temp = tk.Label(master=self, text="Initial temp", font=50)
        self.lbl_temp.place(x=230, y=20)
        self.lbl_hum = tk.Label(master=self, text="Initial hum", font=50)
        self.lbl_hum.place(x=100, y=20)
        self.lbl_pres = tk.Label(master=self, text="Initial pres", font=50)
        self.lbl_pres.place(x=330, y=20)
        if 'serial_port' in kwargs:
            self.serial_port = kwargs['serial_port']
        else:
            self.serial_port = self.SERIAL_PORT_DEFAULT
        if 'serial_baudrate' in kwargs:
            self.serial_baudrate = kwargs['serial_baudrate']
        else:
            self.serial_baudrate = self.SERIAL_BAUDRATE_DEFAULT
        if 'file_name' in kwargs:
            self.file_name = kwargs['file_name']
        else:
            self.file_name = self.FILE_NAME_DEFAULT
        self.ser = serial.Serial() # create a serial instance
        self.ser.port = self.serial_port
        self.ser.baudrate=self.serial_baudrate
        try:
            data_file=open("archivo.csv","w")
            
        except IOError as e:
            print(f"Error al abrir el archivo: {e}")
            sys.exit()
        
    def close_application(self):
        self.destroy()
        
    def extract_temp(self,message):
        
        data_string = message.decode("utf-8")
        temp = re.findall('<temp=([\d]+[.,\d]+),', data_string) # extract values from string
        if temp:
            return temp[0]
        else:
            return temp
        

    def extract_hum (self,message):
        
        data_string = message.decode("utf-8")
        hum = re.findall('hum=([\d]+[.,\d]+),', data_string) # extract values from string
        if hum:
            return hum[0]
        else:
            return hum
       

    def extract_pres (self,message):
        
        data_string = message.decode("utf-8")
        pres = re.findall('pres=([\d]+[.,\d]+)>', data_string) # extract values from string
        if pres:
            return pres[0]
        else:
            return pres
        
    def extract_data(self, message):
        self.temp=self.extract_temp(message)
        self.hum=self.extract_hum(message)
        self.pres=self.extract_pres(message)
        data=[self.temp, self.hum, self.pres]
        data_values= [float(num) for num in data if num]
        data_values=[values +10 if values.is_integer() else values for values in data_values ]
        return data_values
        
    def get_weather(self) :
        global data_file
        print("get_weather() working...")
        message = self.ser.readline() # read one line (until EOL) from the serial port
        message = b'<temp=4.2,hum=42,pres=1042> ' #b stands for binary data
        print(message)
        temp=self.extract_temp(message)
        hum=self.extract_hum(message)
        pres=self.extract_pres(message)
        data= self.extract_data(message)
        print(data)
        if len(data)==3:
            temp, hum, pres= [f"{values}" for values in data]
        print(temp)
        print(hum)
        print(pres)
        if temp:
            data_file.write(f'{temp}; {pres}; {hum}\n')
        if temp:
           self.lbl_temp["text"]= temp + " ºC"
           self.lbl_hum["text"]=hum + " %"
           self.lbl_pres["text"]=pres + " hPa"
           
    def run(self):
        self.after(1000, self.get_weather)
        self.mainloop()
        
    
App = WeatherStation(serial_port='COM6');
App.run()

