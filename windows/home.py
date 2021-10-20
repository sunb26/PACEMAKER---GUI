## Will need to add this to imported in the welcome page so that can send to this page after login 
    # And get rid of the parameters page from that 

import tkinter as tk
#import json # Not sure if will need this? 
#from windows.parameters import parameter_page # Will send to this page when want to edit the parameters 
#from windows.welcome import welcome_page

class home_page:
    def __init__(self, root, user, parameter_database): # May need to alter these - need username to display it on homepage 
        # Intialize current user
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Closing login page "root"
        self.root = root 
        self.root.destroy()

        self.window = tk.Tk()
        self.window.title("Home Page")

        self.canvas = tk.Canvas(self.window, width = 1200, height = 600)
        self.canvas.grid(columnspan = 8, rowspan = 12) # Need to have space for 8 rows parameters 

        # Connection label
        self.connection_label = tk.Label(self.window, text = "Connection Status", font = ("Raleway", 18))
        self.connection_label.grid(column = 0, row = 0)

        # Need connection identifier now 
            # Not sure what this should be so that it takes inputs and has different output (different colour) depending on this 

        # Mode label 
        self.mode_label = tk.Label(self.window, text = "Mode", font = ("Raleway", 18))
        self.mode_label.grid(column = 0, row = 3)



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



