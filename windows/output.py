import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import windows.utils.serial_com as serial


#     Need a STOP button for user to put to stop updating the graphs! (But stay on the output page I guess)

stop_var = False


class output_page:
    def __init__(self, root, user, mode, param_DB):
        self.root = root
        self.user = user
        self.mode = mode
        self.param_DB = param_DB

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

        # 
        if stop_var:
            print("start! _-______---__-")
            ani1 = animation.FuncAnimation(self.figure1, self.animate_graphs, fargs = [self.param_DB], interval = 100) ## Maybe want frames = 100 or something in here, not sure what it does
            plt.show()

        self.window.after(1, self.show_graphs)


    def animate_graphs(self, i, parameter_database):

        # Conditional accounting for if user doesn't have inputted values so use default to send to MATLAB
        if self.user in parameter_database.keys() and self.mode in parameter_database[self.user].keys():
            dict_user = self.user
        else:
            dict_user = "default"

        # If stop_var == True then skeep plotting in the graph, if False then don't plot (and keep iterating)
        if stop_var == True:
            self.ax1[0].clear() # Clearing the previous version of the graph, followed by plotting the entire graph again
            self.ax1[0].plot(self.atrium[-150:])  # This makes graph show last 150 points

            self.ax1[0].set_title("Atrium: Voltage vs Time")
            self.ax1[0].set_ylabel("Voltage (mV)")
            self.ax1[0].set_xlabel("Time (ms)")

            self.ax1[1].clear()
            self.ax1[1].plot(self.ventricle[-150:])

            self.ax1[1].set_title("Ventricle: Voltage vs Time")
            self.ax1[1].set_ylabel("Voltage (mV)")
            self.ax1[1].set_xlabel("Time (ms)")

        # Do serial communication to get packet in the form [Atrial, Ventricle], then append to pre-made lists
        for l in range(50):
            param_dict = parameter_database[dict_user][self.mode]
            param_dict["mode"] = self.param_index[self.mode]
            packet = serial.serial_packet(param_dict).transmit_params(4)
            self.atrium.append(packet[0])
            self.ventricle.append(packet[1])

    def start(self):
        global stop_var
        stop_var = True

    def stop(self):
        global stop_var
        stop_var = False
        