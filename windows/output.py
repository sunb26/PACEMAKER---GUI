import tkinter as tk
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# So:
    # are two doubles that are sent over serial communication both the y values one for arial and one for ventricular 

    # Only need to implement this to show both graphs at once 

    # Need a STOP button for user to put to stop updating the grpahs! (But stay on the output page I guess)

class output_page:
    def __init__(self, root):
        self.root = root

        self.window = tk.Toplevel(self.root)
        self.window.title("Output")

        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.grid(columnspan=5, rowspan=10)

        self.output_label = tk.Label(self.window, text = "Insert Output Here", font = ("Raleway, 14"))
        self.output_label.grid(column = 2, row = 4)

        self.button1 = tk.Button(self.window, text = "Show Graph", bg="#20bebe", font = "Raleway",
                                       command = lambda: self.show_ani(), fg = "white", height = 1, width = 12)
        self.button1.grid(column = 2, row = 2)
        #self.button1 = tk.Button(self, text="Back to Home", command = lambda: self.)
        #self.button1.grid(column = )

        # self.figure = plt.Figure(figsize=(6,5), dpi = 100)
        # self.ax = self.figure.add_subplot(111)

    def show_ani(self):
        # figure = plt.Figure(figsize=(6,5), dpi = 100)
        # ax = figure.add_subplot(111)

        figure, ax = plt.subplots()
        
        ani = animation.FuncAnimation(figure, self.animate, fargs = (ax), interval = 1000)
        plt.show()

    def animate(self, i, ax):
        f = open('data.txt','r').read()
        lines = f.split('\n') # This assuming data text file has each xy pair separated by a new line
        xs = []
        ys = []

        for line in lines:
            if line == "":
                break
            else:
                x,y = line.split(',') # This assuming data text file has x and y separated by ,
                xs.append(float(x))
                ys.append(float(y))
                print("X-Values: ") 
                print(xs)
                print("Y-Values: ")
                print(ys)

        ax.clear()
        ax.plot(xs, ys)
        plt.xlabel('Time')
        plt.ylabel('mV')
        plt.title('Voltage With Respect to Time')

