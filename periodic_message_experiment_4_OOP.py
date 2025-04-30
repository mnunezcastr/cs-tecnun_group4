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
        self.geometry("500x200")
        self.title('Weather Station')
        self.resizable(False, False)
        self.btn_quit = tk.Button(master=self, text="Quit", font=50, command=self.close_application)
        self.btn_quit.place(x=230, y=100)
        self.lbl_temp = tk.Label(master=self, text="Initial temp", font=50)
        self.lbl_temp.place(x=230, y=20)
        self.lbl_hum = tk.Label(master=self, text="Initial temp", font=50)
        self.lbl_hum.place(x=100, y=20)
        self.lbl_pres = tk.Label(master=self, text="Initial temp", font=50)
        self.lbl_pres.place(x=330, y=20)
        
    def close_application(self):
        self.destroy()
        
    def run(self):
        self.mainloop()
        
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
        
App = WeatherStation();
App.run()

