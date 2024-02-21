import tkinter as tk
import tkinter.ttk as ttk
import asyncio

import datetime

class DateTimeWidget(ttk.Frame):
    
    def __init__(self, master, *args,**kwargs):
        super().__init__(master, padding=3)

        self.text_field = ttk.Label(self,text='14:28',style='datetime.TLabel')
        self.text_field.pack()

    async def run(self):
        try:
            while True:
                time = datetime.datetime.now()
                self.text_field['text'] = str(time.hour)+":"+str(time.minute)
                await asyncio.sleep(10)
        except:
            pass