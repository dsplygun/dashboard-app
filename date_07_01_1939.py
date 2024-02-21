import tkinter as tk
import tkinter .ttk as ttk
import asyncio
import datetime
import python_weather
import os

async def getweather():
  
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    weather = await client.get('Chuhuiv')
    
    return weather



class Weather(ttk.Frame):
    
    def __init__(self,master,*args,**kwargs):
        super().__init__(master)
        self.weather_field = ttk.Label(self,text = "14:88",style='reich.TLabel') 
        self.weather_field.pack()
    async def run(self):
        try:
            while True:
                weather_task = asyncio.create_task(getweather())
                weather = await weather_task
                self.weather_field["text"] = str(weather.current.temperature) + "°С " + str(weather.current.description)
                await asyncio.sleep(10)
        except:
            pass