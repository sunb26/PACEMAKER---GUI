import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import windows.utils.serial_com as serial

# Defining global variable stop_var to start as False
stop_var = False

class output_page:
    def __init__(self, root, user, mode, param_DB, echo_param):
        # Initialize parameters to be used in class 
        self.root = root
        self.user = user
        self.mode = mode
        self.param_DB = param_DB
        self.echo_param = echo_param

        # Creating new output window 
        self.window = tk.Toplevel(self.root)
        self.window.title("Output")

        # Setting canvas size for output window
        self.canvas = tk.Canvas(self.window, width=400, height=300)
        self.canvas.grid(columnspan=1, rowspan=6)

        # Initializing empty lists to hold data to be plotted on graphs 
        self.atrium = []
        self.ventricle = []

        # Initializing figure as a subplot to show both atrial and ventricle graphs at once 
        # self.figure1, self.ax1 = plt.subplots(1, 2)
        # self.figure1.set_figwidth(12)
        # self.figure1.set_figheight(6)

        # Button used to show the graphs and call start() function
        self.graph_button = tk.Button(self.window, text="Show Atrium + Ventricle Graphs", bg="#20bebe", font="Raleway",
                                      command=lambda: self.__start(), fg="white", height=1, width=26)
        self.graph_button.grid(column=0, row=1)

        # Button used to stop the graphs from plotting by calling stop() function 
        self.stop_button = tk.Button(self.window, text="Stop Updating Graphs", bg="#20bebe", font="Raleway",
                                     command=lambda: self.__stop(), fg="white", height=1, width=26)
        self.stop_button.grid(column=0, row=2)

        # Dictionary correlating modes to integer values 
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

        # Order of parameters used to print the values on output page when echoed back from hardware 
        self.params_order = ["lrl", "url", "aa", "va", "apw", "vpw", "ARP", "VRP", "msr", "favd", "asen", "vsen", "PVARP", 
                            "hys", "rs", "at", "rct", "rf", "rvt", "mode"]
        self.param_string1 = ""
        self.param_string2 = ""
        self.counter = 0

        # Creating strings to show as labels on output page with all echoed parameter information 
        for name, param in zip(self.params_order, self.echo_param):
            if self.counter < 10:
                self.param_string1 += f"{name}: "
                self.param_string1 += f"{param}, "
                self.counter += 1
            else:
                self.param_string2 += f"{name}: "
                self.param_string2 += f"{param}, "

        # Placing the labels with echoed parameter information on the output page 
        self.echo_label1 = tk.Label(self.window, text = self.param_string1, font = ("Raleway", 12))
        self.echo_label1.grid(column = 0, row = 3)
        self.echo_label2 = tk.Label(self.window, text = self.param_string2, font = ("Raleway", 12))
        self.echo_label2.grid(column = 0, row = 4)
        self.neg_label = tk.Label(self.window, text = "Note: Disregard all parameters that do not correlate to the current mode", font = ("Raleway", 12))
        self.neg_label.grid(column = 0, row = 5)


    # Once show_graphs() is called, start receiving info from matlab to plot (by calling the animate_graphs function)
    def __show_graphs(self):
        self.figure1, self.ax1 = plt.subplots(1, 2)
        self.figure1.set_figwidth(12)
        self.figure1.set_figheight(6)
        if stop_var:
            ani1 = animation.FuncAnimation(self.figure1, self.__animate_graphs, fargs = [self.param_DB], interval = 100)
            plt.show()   
        

    # animate_graphs() function called repeatedly in the FuncAnimation call in show_graphs function 
    def __animate_graphs(self, i, parameter_database):

        # Conditional accounting for if user doesn't have inputted values so use default to send to MATLAB
        if self.user in parameter_database.keys() and self.mode in parameter_database[self.user].keys():
            dict_user = self.user
        else:
            dict_user = "default"

        # If stop_var == True then keep plotting in the graph, if False then don't plot (and keep iterating)
        if stop_var == True:
            self.ax1[0].clear() # Clearing the previous version of the graph, followed by plotting the entire graph again
            self.ax1[0].plot(self.atrium[-150:])  # This makes graph show last 150 points

            self.ax1[0].set_title("Atrium: Voltage vs Time")
            self.ax1[0].set_ylabel("Voltage (mV)")
            self.ax1[0].set_xlabel("Time")

            self.ax1[1].clear()
            self.ax1[1].plot(self.ventricle[-150:])

            self.ax1[1].set_title("Ventricle: Voltage vs Time")
            self.ax1[1].set_ylabel("Voltage (mV)")
            self.ax1[1].set_xlabel("Time")

        # Do serial communication to get packet in the form [Atrial, Ventricle], then append to pre-made lists
        for l in range(50):
            param_dict = parameter_database[dict_user][self.mode]
            param_dict["mode"] = self.param_index[self.mode]

            # Ensuring the hardware device is still connected 
            if not serial.findPorts():
                print("Device not found")
                break

            packet = serial.serial_packet(param_dict).transmit_params(4)
            self.atrium.append(packet[0])
            self.ventricle.append(packet[1])

    # Called when "Show Graphs" button is hit
    def __start(self):
        global stop_var
        stop_var = True
        self.window.after(1, self.__show_graphs)

    # Called when "Stop Updating Graphs" button is hit
    def __stop(self):
        global stop_var
        stop_var = False
        