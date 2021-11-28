import tkinter as tk
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure 
from matplotlib.pyplot import figure 

import numpy as np

# So:
#     are two doubles that are sent over serial communication both the y values one for arial and one for ventricular 

#     Only need to implement this to show both graphs at once 

#     Need a STOP button for user to put to stop updating the graphs! (But stay on the output page I guess)

class output_page:
    def __init__(self, root):
        self.root = root

        self.window = tk.Toplevel(self.root)
        self.window.title("Output")

        self.canvas = tk.Canvas(self.window, width=400, height=300)
        self.canvas.grid(columnspan=3, rowspan=5)

        self.data1 = [0, 0, 0, 0, 0]

        self.figure1, self.ax1 = plt.subplots(1, 2)
        self.figure1.set_figwidth(12)
        self.figure1.set_figheight(6)

        self.graph_button = tk.Button(self.window, text = "Show Atrium + Ventricle Graphs", bg="#20bebe", font = "Raleway",
                                       command = lambda: self.show_graphs(), fg = "white", height = 1, width = 26)
        self.graph_button.grid(column = 2, row = 1)

        self.stop_button = tk.Button(self.window, text = "Stop Updating Graphs", bg = "#20bebe", font = "Raleway", 
                                      fg = "white", height = 1, width = 26)
        self.stop_button.grid(column = 2, row = 2)

        


    def show_graphs(self):        
        ani1 = animation.FuncAnimation(self.figure1, self.animate_graphs, frames = 100, interval = 1000)
        plt.show()        


    def animate_graphs(self, i):
        with open('data.txt', 'r') as f:
            for line in f:
                self.data1.append(float(line.strip()))

        self.ax1[0].clear()
        self.ax1[0].plot(self.data1[-40:]) # This makes graph show last 20 points

        self.ax1[0].set_title("Atrium: Voltage vs Time")
        self.ax1[0].set_ylabel("Voltage (mV)")
        self.ax1[0].set_xlabel("Time (ms)")

        self.ax1[1].clear()
        self.ax1[1].plot(self.data1[-40:])

        self.ax1[1].set_title("Ventricle: Voltage vs Time")
        self.ax1[1].set_ylabel("Voltage (mV)")
        self.ax1[1].set_xlabel("Time (ms)")




# class output_page:
#     def __init__(self, root):
#         self.root = root
        
        
#         #self.window = tk.Toplevel(self.root)
#         #self.window.title("Output")

#         #self.canvas1 = tk.Canvas(self.window, width=600, height=600)
#         #self.canvas1.grid(columnspan=5, rowspan=10)

        

#         self.data = [0, 0, 0, 0, 0]

#         self.figure, self.ax = plt.subplots()
#         self.ani = animation.FuncAnimation(self.figure, self.animate, frames = 100, interval = 1000)
#         plt.show()

#         self.canvas = FigureCanvasTkAgg(self.figure, master = self.root)
#         self.canvas.draw()
#         #self.canvas.get_tk_widget().grid(column = 1, row = 1)
        
#         self.button1 = tk.Button(master=self.root, text="Quit", command=quit)
#         self.button1.pack(side=tk.BOTTOM)

#         # self.button1 = tk.Button(self.window, text = "Show Atrium Graph", bg="#20bebe", font = "Raleway",
#         #                                command = lambda: self.show_ani(), fg = "white", height = 1, width = 12)
#         # self.button1.grid(column = 2, row = 2)

#     # def show_ani(self):        
#     #     ani = animation.FuncAnimation(self.figure, self.animate, frames = 100, interval = 1000)
#     #     plt.show()
        

#     def animate(self, i):
#         with open('data.txt', 'r') as f:
#             for line in f:
#                 self.data.append(float(line.strip()))

#         self.ax.clear()
#         self.ax.plot(self.data[-20:]) # This makes graph show last 20 points 
#         plt.xlabel('Time (ms)')
#         plt.ylabel('Voltage (mV)')
#         plt.title('Atrium: Voltage With Respect to Time')

