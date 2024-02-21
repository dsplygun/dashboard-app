import tkinter as tk
import tkinter.ttk as ttk
import asyncio

import psutil


class CpWidget(ttk.Frame):
    
    def __init__(self,master ,*args, **kwargs):
        super().__init__(master, padding=4)
        self.text_field=ttk.Label(self, text='50% CPU',style='cp_MGc.TLabel')
        self.text_field.pack()
        
        
        self.text_pon=ttk.Label(self, text='pon',style='cp_MGc.TLabel')
        self.text_pon.pack()
        
        
        
        
        
        
    async def run(self):
        try:
            #psutil.cpu_times()
            
            #for x in range(3):
                #psutil.cpu_percent(interval=1)
                    
            #for x in range(3):
                #psutil.cpu_percent(interval=1, percpu=True)
                
            #for x in range(3):
                #psutil.cpu_times_percent(interval=1, percpu=False)
                
            #psutil.cpu_count()
            #psutil.cpu_count(logical=False)
            #psutil.cpu_stats()
            #psutil.cpu_freq()
            #psutil.getloadavg()  # also on Windows (emulated)
            while True:
                self.text_field['text']=str(psutil.cpu_percent(interval=1))+"% CPU"
                self.text_pon['text']=str(psutil.cpu_freq().current)+" МГц"
                await asyncio.sleep(1)  
        except:
            pass
