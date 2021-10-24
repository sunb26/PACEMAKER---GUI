## Will need to add this to imported in the welcome page so that can send to this page after login 
    # And get rid of the parameters page from that 

import tkinter as tk
from PIL import Image, ImageTk
import json 
#from windows.parameters import parameter_page # Will send to this page when want to edit the parameters 
import windows.welcome as wel

class home_page:
    def __init__(self, root, user, login_database, parameter_database): # May need to alter these - need username to display it on homepage 
        # Intialize current user
        self.user = user

        # Intialize databases
        self.DB = parameter_database
        self.login_DB = login_database

        # Closing login page "root"
        self.root = root 
        self.root.destroy()

        # Creating new window for home page 
        self.window = tk.Tk()
        self.window.title("Home Page")

        # Setting canvas size for home page 
        self.canvas = tk.Canvas(self.window, width = 1200, height = 600)
        self.canvas.grid(columnspan = 8, rowspan = 12)

        # Device name label 
        self.device_label = tk.Label(self.window, text = "Device Name: ___________", font = ("Raleway", 14))
        self.device_label.grid(columnspan = 3, column = 0, row = 0, sticky="W")

        # Device name 
            # In final version, use some function to get the device name and display it beside the semicolon of "Device Name"

        # Connection label
        self.connection_label = tk.Label(self.window, text = "Connection Status:", font = ("Raleway", 14))
        self.connection_label.grid(columnspan = 3, column = 0, row = 1, sticky="W")

        # Connection identifier
            # In final version, use if statement to determine if the device is connected or not, then if so 
            # display the green rectangle, and if not display the red rectangle 
        self.canvas.create_rectangle(175, 65, 205, 95, outline="#000000", fill="#00ee01")

        # Logo image 
        self.logo = Image.open('utils/logo.png')
        self.logo = self.logo.resize((300, 120), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.grid(rowspan = 3, columnspan = 2, column=3, row=0)

        # Username label

        # Username identifier

        
        # Logout button
        self.logout_button = tk.Button(self.window, text = "Logout", bg="#20bebe", font = "Raleway",
                                       command = lambda: self.function1(), fg = "white", height = 1, width = 8)
        self.logout_button.grid(column = 7, row = 1)

        # Mode dropdown
        self.mode_options = [
            "AOO",
            "VOO", 
            "AAI", 
            "VVI"
        ]

        # Setting default drop down menu item as "AOO"
        self.default_mode = tk.StringVar(self.window)
        self.default_mode.set(self.mode_options[0])

        self.opt = tk.OptionMenu(self.window, self.default_mode, *self.mode_options)
        tk.Label(self.window, text = "Choose a mode:", font = ("Raleway", 14)).grid(column = 0, row = 5)
        self.opt.config(width = 10, font = ("Raleway", 14))
        self.opt.grid(column = 0, row = 6)

        # Parameters label
        self.parameter_label = tk.Label(self.window, text = "Parameters", font = ("Raleway", 18))
        self.parameter_label.grid(column = 4, row = 3)

        # Initializing parameters
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=4, row=4)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=4, row=5)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=4, row=6)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=4, row=7)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=8)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=9)
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
        self.VRP_label.grid(column=4, row=10)
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
        self.ARP_label.grid(column=4, row=11)
    
    def function1(self):
        self.window.destroy()
        wel.welcome_page(tk.Tk(), self.login_DB, self.DB) # Have to re-instatiate a new TK() window to pass to welcome_page because the function doesn't make one itself
        



