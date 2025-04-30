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