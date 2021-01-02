import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

window = tk.Tk()
window.geometry("1080x640")
window.wm_title("Trading")

pw = ttk.Panedwindow(window, orient= tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand = True)

w2 = ttk.Panedwindow(pw, orient= tk.VERTICAL)

frame1 = ttk.Frame(pw, width = 360, height = 640, relief = tk.SUNKEN)
frame2 = ttk.Frame(pw, width = 720, height = 400, relief = tk.SUNKEN)
frame3 = ttk.Frame(pw, width = 720, height = 240, relief = tk.SUNKEN)

w2.add(frame2)
w2.add(frame3)


pw.add(w2)
pw.add(frame1)

#frame1 : treeview, open trade button

item = ""

def callback(event):
    global item
    item = treeview.identify("item",event.x, event.y)
    print("Clicked", item)


treeview = ttk.Treeview(frame1)
treeview.grid(row = 0, column = 1, padx=25, pady=25)
treeview.insert("","0","Major", text = "Major")
treeview.insert("Major", "1", "EUR/USD", text = "EUR/USD")
treeview.insert("","2","Minor", text = "Minor")
treeview.insert("Minor", "3", "EUR/GBP", text = "EUR/GBP")

treeview.bind("<Double-1>", callback)

#button

def openTrade():
    print("opentrade")
    if item != "":
        print("chosen item : ", item)
        
        if item =="EUR/USD":
        #button settings
            open_button.config(state = "disabled")
            start_button.config(state = "normal")
            
            #data
            data = pd.read_csv("eurusd.csv")
            
            future = data[-1000:]
            data = data[:len(data)-1000]
            data_close_array = data.close1.values
            future_array = list(future.close1.values)
            
            #line
            
            fig1 = plt.Figure(figsize = (5,4), dpi = 100)
            ax1 = fig1.add_subplot(111) # 1. satir, 1. sutun a 1 tane resim,plot koycam
            line, = ax1.plot(range(len(data)), data.close1, color = "blue") # line a 2 deger doner ama 1 tanesini istiyorum dgeri cok onemli degil
            
            canvas = FigureCanvasTkAgg(fig1, master = tab1)
            canvas.draw()
            canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            # scatte
            
            fig2 = plt.Figure(figsize = (5,4), dpi = 100)
            ax2 = fig2.add_subplot(111)
            line2 = ax2.scatter(range(len(data)), data.close1, s = 1, alpha = 0.5, color = "red")
            canvas2 = FigureCanvasTkAgg(fig2, master = tab2)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        
        elif item =="EUR/GBP":
            #button settings
            open_button.config(state = "disabled")
            start_button.config(state = "normal")
            
            #data
            data = pd.read_csv("eurgbr.csv")
            
            future = data[-1000:]
            data = data[:len(data)-1000]
            data_close_array = data.close1.values
            future_array = list(future.close1.values)
            
            #line
            
            fig3 = plt.Figure(figsize = (5,4), dpi = 100)
            ax3 = fig3.add_subplot(111) # 1. satir, 1. sutun a 1 tane resim,plot koycam
            line3, = ax3.plot(range(len(data)), data.close1, color = "blue") # line a 2 deger doner ama 1 tanesini istiyorum dgeri cok onemli degil
            
            canvas3 = FigureCanvasTkAgg(fig3, master = tab1)
            canvas3.draw()
            canvas3.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            # scatter
            
            fig4 = plt.Figure(figsize = (5,4), dpi = 100)
            ax4 = fig4.add_subplot(111)
            line4 = ax4.scatter(range(len(data)), data.close1, s = 1, alpha = 0.5, color = "red")
            canvas4 = FigureCanvasTkAgg(fig4, master = tab2)
            canvas4.draw()
            canvas4.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
            
        else:
            messagebox.showinfo(title = "Warning", message = "Double Click to Choose Currency Pair")    
    else : 
        messagebox.showinfo(title = "Warning", message = "Double Click to Choose Currency Pair")            
            
    
open_button = tk.Button(frame1, text = "Open Trading", command = openTrade)
open_button.grid(row = 2, column = 1, padx=5, pady=5)
    
 # frame3: text editor,scrollbar
 
textBox = tk.Text(frame3, width = 70, height=10, wrap = "word")
textBox.grid(row = 0, column = 0, padx=25,pady=10)
scroll = tk.Scrollbar(frame3, orient=tk.VERTICAL, command = textBox.yview)
scroll.grid(row = 0, column = 1, sticky = tk.N + tk.S, pady = 2)
textBox.config(yscrollcommand=scroll.set)
    

#frame2 : tabview, radiobuttons, button, labelframe ve plot

tabs = ttk.Notebook(frame2, width = 500, height=300)
tabs.place(x = 25, y = 25)
tab1 = ttk.Frame(tabs, width = 50, height= 50)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text = "Line")
tabs.add(tab2, text = "Scatter", compound = tk.LEFT) # compound sola yaslar

# radiobutton

method = tk.StringVar() # stringVar, radiobuttonda bulunan verileri okumak icin
tk.Radiobutton(frame2, text = "m1 : ", value = "m1", variable = method).place(x = 580, y = 100)
tk.Radiobutton(frame2, text = "m2 : ", value = "m2", variable = method).place(x = 580, y = 125)

# LAbelFrame

label_frame = tk.LabelFrame(frame2, text = "Result", width = 100, height = 150)
label_frame.place(x = 580, y = 25)
tk.Label(label_frame, text = "Buy: ", bd = 3).grid(row = 0, column = 0)
tk.Label(label_frame, text = "Sell: ", bd = 3).grid(row = 1, column = 0)


# button

def startTrading():
    print("startTrading")


start_button = tk.Button(frame2, text = "Start Trading", command = startTrading)
start_button.place(x = 580, y = 150)
start_button.config(state = "disabled") # daha sonra duzenlenecek













window.mainloop()