import tkinter as tk
import tkinter.ttk as ttk
import asyncio
import psutil as ps

class BatteryWidget(ttk.Frame):
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,)
        
        self.text_field=ttk.Label(self,text='Battery')
        self.text_field.pack()
        
        
    async def run(self):
        try:
             ps.sensors_battery()
        
        except:
            pass