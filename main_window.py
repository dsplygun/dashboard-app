import tkinter as tk
import _tkinter
import tkinter.ttk as ttk
import asyncio
from async_tkinter_loop import async_handler, async_mainloop, main_loop
import json

import date_and_time

logging_text : tk.Text = None
window = tk.Tk()
window.title("Dashboard")

def add_line(self : tk.Text, text : str) -> None:
    try:
        self['state']=tk.NORMAL
        self.insert(tk.END,text+'\n')
        self['state']=tk.DISABLED
    except:
        print('Error inserting line',text)
        self['state']=tk.DISABLED

def log(text:str) -> None:
    try:
        logging_text.add_line(text)
    except:
        print(text)

class MessageServerProtocol:
    def __init__(self,list : list):
        self.message_list = list

    def connection_made(self,transport):
        self.transport = transport
    
    def connection_lost(self,transport):
        pass

    def datagram_received(self,data,addr):
        try:
            package = json.loads( data.decode() )
            self.message_list.append(package['name']+'>> '+package['message'])

        except:
            self.message_list.append('Unresolved message: '+data.decode())

async def compile_messages(message_list):
    try:
        while window.state():
            await asyncio.sleep(1)
            for msg in message_list:
                log(message_list.pop(0))
    except:
        pass

async def run_udp_server(message_list : list):
    log('Starting UDP server')

    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda:MessageServerProtocol(message_list),
        local_addr=('0.0.0.0',80))
    
    try:
        await compile_messages(message_list)
    finally:
        transport.close()
    
async def main():
    tk.Text.add_line = add_line


    s = ttk.Style()
    s.configure('TFrame',background='green')
    s.configure('rightpanel.TFrame',background='red')
    s.configure('leftpanel.TFrame',background='blue')
    
    right_panel = ttk.Frame(window,borderwidth=2,padding=3,style='rightpanel.TFrame')
    right_panel.pack(side=tk.RIGHT)

    main_panel = ttk.Frame(window,style='leftpanel.TFrame',padding=3)
    main_panel.pack(side=tk.LEFT)

    main_panel_text = tk.Text(main_panel)
    main_panel_text['state']=tk.DISABLED
    main_panel_text.pack()
    global logging_text
    logging_text = main_panel_text

#####
    date_widget = date_and_time.DateTimeWidget(right_panel)
    date_widget.pack()

#####
    loop = asyncio.get_running_loop()
    msg_list = []
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(run_udp_server(msg_list))
        
        for i in right_panel.children:
            new_task = tg.create_task( right_panel.children[i].run() )
        #task_time = tg.create_task( date_widget.run() )

        task2 = tg.create_task(main_loop(window))
    #asyncio.ensure_future()

    #asyncio.get_event_loop().run_until_complete(main_loop(window))



if __name__ == "__main__":
    asyncio.run(main())