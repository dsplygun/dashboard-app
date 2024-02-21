import tkinter as tk
import tkinter.ttk as ttk
import asyncio
import psutil as ps

class BatteryWidget(ttk.Frame):
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,)
        
        self.text_field=ttk.Label(self,text='Battery',style='Battery.TLabel')
        self.text_field.pack()
        
        
    async def run(self):
        try:
            while True:
                battery=ps.sensors_battery()
                self.text_field['text']='Battery: '+str(battery.percent)+'%'
                await asyncio.sleep(10)
        except:
            print('Error: In function "run"')