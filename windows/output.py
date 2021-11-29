import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure
from matplotlib.pyplot import figure

# import numpy as np

import windows.utils.serial_com as serial
import json

# So:
#     are two doubles that are sent over serial communication both the y values one for arial and one for ventricular 

#     Only need to implement this to show both graphs at once 

#     Need a STOP button for user to put to stop updating the graphs! (But stay on the output page I guess)


## create while true loop that has if conditional inside it that says if button is pressed then call ben's serial 
## comm. function to send packet (and thus stop receiving input packet) then in while loop, take the list of 2 double 
## values and append 1st one to atrial list (which is being plotted) then append other to ventricle list 

stop_var = False


class output_page:
    def __init__(self, root, user, mode):
        self.root = root
        self.user = user
        self.mode = mode

        self.window = tk.Toplevel(self.root)
        self.window.title("Output")

        self.canvas = tk.Canvas(self.window, width=400, height=300)
        self.canvas.grid(columnspan=1, rowspan=5)

        self.atrium = []
        self.ventricle = []

        self.figure1, self.ax1 = plt.subplots(1, 2)
        self.figure1.set_figwidth(12)
        self.figure1.set_figheight(6)

        self.graph_button = tk.Button(self.window, text="Show Atrium + Ventricle Graphs", bg="#20bebe", font="Raleway",
                                      command=lambda: self.start(), fg="white", height=1, width=26)
        self.graph_button.grid(column=0, row=1)

        self.stop_button = tk.Button(self.window, text="Stop Updating Graphs", bg="#20bebe", font="Raleway",
                                     command=lambda: self.stop(), fg="white", height=1, width=26)
        self.stop_button.grid(column=0, row=2)

        # self.stop_var = True

        self.param_index = {
            "AOO": 1,
            "VOO": 2,
            "AAI": 3,
            "VVI": 4,
            "DOO": 5,
            "AOOR": 6,
            "VOOR": 7,
            "AAIR": 8,
            "VVIR": 9,
            "DOOR": 10
        }
        self.window.after(1, self.show_graphs)

    # once this is called, start receiving info from matlab to plot (by calling the animate_graphs function)
    def show_graphs(self):

        if stop_var:
            # If stop button hit, break
            ani1 = animation.FuncAnimation(self.figure1, self.animate_graphs, interval = 1) ## Maybe want frames = 100 or something in here, not sure what it does
            plt.show()
            #self.window.title("Working...")
        else:
            #self.window.title("Stopped!")

        self.window.after(1, self.show_graphs)

    def animate_graphs(self, i):
        with open("database/parameters.json") as database2:
            parameter_database = json.load(database2)

        # Accounting for if user doesn't have inputted values so use default to send to MATLAB
        if self.user in parameter_database.keys() and self.mode in parameter_database[self.user].keys():
            dict_user = self.user
        else:
            dict_user = "default"

        # Do serial comm stuff to get packet in the form [Atrial y-component, Ventricle y-component]
        param_dict = parameter_database[dict_user][self.mode]
        param_dict["mode"] = self.param_index[self.mode]
        packet = serial.serial_packet(param_dict).transmit_params(4)
        self.atrium.append(packet[0])
        self.ventricle.append(packet[1])

        self.ax1[0].clear()
        self.ax1[0].plot(self.atrium[-40:])  # This makes graph show last 40 points
        # If not working maybe neext to pre-fill atrium and ventricle graphs with 40 zeros in __init__

        self.ax1[0].set_title("Atrium: Voltage vs Time")
        self.ax1[0].set_ylabel("Voltage (mV)")
        self.ax1[0].set_xlabel("Time (ms)")

        self.ax1[1].clear()
        self.ax1[1].plot(self.ventricle[-40:])

        self.ax1[1].set_title("Ventricle: Voltage vs Time")
        self.ax1[1].set_ylabel("Voltage (mV)")
        self.ax1[1].set_xlabel("Time (ms)")

    def start(self):
        global stop_var
        stop_var = True

    def stop(self):
        global stop_var
        stop_var = False






## Copy of pre-serial comm. output_page class

# class output_page:
#     def __init__(self, root):
#         self.root = root

#         self.window = tk.Toplevel(self.root)
#         self.window.title("Output")

#         self.canvas = tk.Canvas(self.window, width=400, height=300)
#         self.canvas.grid(columnspan=3, rowspan=5)

#         self.data1 = [0, 0, 0, 0, 0]

#         self.figure1, self.ax1 = plt.subplots(1, 2)
#         self.figure1.set_figwidth(12)
#         self.figure1.set_figheight(6)

#         self.graph_button = tk.Button(self.window, text = "Show Atrium + Ventricle Graphs", bg="#20bebe", font = "Raleway",
#                                        command = lambda: self.show_graphs(), fg = "white", height = 1, width = 26)
#         self.graph_button.grid(column = 2, row = 1)

#         self.stop_button = tk.Button(self.window, text = "Stop Updating Graphs", bg = "#20bebe", font = "Raleway", 
#                                       fg = "white", height = 1, width = 26)
#         self.stop_button.grid(column = 2, row = 2)


#     def show_graphs(self):        
#         ani1 = animation.FuncAnimation(self.figure1, self.animate_graphs, frames = 100, interval = 1000)
#         plt.show()        


#     def animate_graphs(self, i):
#         with open('data.txt', 'r') as f:
#             for line in f:
#                 self.data1.append(float(line.strip()))

#         self.ax1[0].clear()
#         self.ax1[0].plot(self.data1[-40:]) # This makes graph show last 20 points

#         self.ax1[0].set_title("Atrium: Voltage vs Time")
#         self.ax1[0].set_ylabel("Voltage (mV)")
#         self.ax1[0].set_xlabel("Time (ms)")

#         self.ax1[1].clear()
#         self.ax1[1].plot(self.data1[-40:])

#         self.ax1[1].set_title("Ventricle: Voltage vs Time")
#         self.ax1[1].set_ylabel("Voltage (mV)")
#         self.ax1[1].set_xlabel("Time (ms)")
