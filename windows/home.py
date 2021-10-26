## Will need to add this to imported in the welcome page so that can send to this page after login 
    # And get rid of the parameters page from that 

import tkinter as tk
from PIL import Image, ImageTk
import json 
from windows.parameters import parameter_page 
import windows.welcome as wel

import os
os.system("color")

c = {
    "Bold": "\u001b[1m"
}

class home_page:
    def __init__(self, root, user, login_database, parameter_database): # May need to alter these - need username to display it on homepage 
        # Intialize current user
        self.user = user

        # Intialize databases
        self.param_DB = parameter_database
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
        self.username_label = tk.Label(self.window, text = "User: " + user, font = ("Raleway", 14))
        
        # Placing username label far enough away from edge so doesn't distort page
        if len(self.username_label["text"]) < 15:
            self.username_label.grid(column = 7, row = 0)
        else:
            self.username_label.grid(columnspan = 2, column = 6, row = 0)

        # Background (Ugly)
        # self.background_img = Image.open("utils/background.png")
        # self.background_img = ImageTk.PhotoImage(self.background_img)
        # self.background = tk.Label(image=self.background_img)
        # self.background.image = self.background_img
        # self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Logout button
        self.logout_button = tk.Button(self.window, text = "Logout", bg="#20bebe", font = "Raleway",
                                       command = lambda: self.logout(), fg = "white", height = 1, width = 8)
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
        tk.Label(self.window, text = "Choose Mode:", font = ("Raleway", 14)).grid(columnspan = 2, column = 0, row = 5)
        self.opt.config(width = 10, font = ("Raleway", 14))
        self.opt.grid(columnspan = 2, column = 0, row = 6)

        # Button to change parameters
        self.mode_button = tk.Button(self.window, text = "View Parameters", width = 15, height = 1, 
                                     font = "Raleway", fg = "white", bg = "#20bebe", 
                                     command = lambda: self.change_param())
        self.mode_button.grid(columnspan = 2, row = 7, column = 0)

        # Parameters label
        self.parameter_label = tk.Label(self.window, text = "Parameters", font = ("Raleway", 18))
        self.parameter_label.grid(column = 4, row = 3)

        # Initializing parameters
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))

        # Edit Button
        #self.edit_button = tk.Button(self.window, text = "Edit Parameters", width = 15, height = 1, 
                                    #font = "Raleway", fg = "white", bg = "#20bebe", 
                                    #command = lambda: self.edit_param())


    def logout(self):
        self.window.destroy()
        wel.welcome_page(tk.Tk(), self.login_DB, self.DB) # Have to re-instantiate a new TK() window to pass to welcome_page because the function doesn't make one itself
        
## use width and height to set standard dize of labels like do buttons 

## self.param_DB["User"]["Mode"]["Param Abbreviation"] = value

    def change_param(self):
        if self.default_mode.get() == "AOO":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text="Lower Rate Limit: " + "\033[1mThis is coloured\033[0m" + str(self.param_DB["default"]["AOO"]["lrl"]) + "\033[0m", font=("Raleway", 12))
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
            self.url_label.grid(column=4, row=5)
            self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
            self.aa_label.grid(column=4, row=6)
            self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
            self.apw_label.grid(column=4, row=7)
            
        elif self.default_mode.get() == "VOO":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
            self.url_label.grid(column=4, row=5)
            self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
            self.va_label.grid(column=4, row=6)
            self.apw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
            self.apw_label.grid(column=4, row=7)
            
        elif self.default_mode.get() == "AAI":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
            self.url_label.grid(column=4, row=5)
            self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
            self.aa_label.grid(column=4, row=6)
            self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
            self.apw_label.grid(column=4, row=7)
            self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
            self.ARP_label.grid(column=4, row=8)
        else: 
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
            self.url_label.grid(column=4, row=5)
            self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
            self.va_label.grid(column=4, row=6)
            self.apw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
            self.apw_label.grid(column=4, row=7)
            self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
            self.VRP_label.grid(column=4, row=8)

    #def edit_param(self):
        # Do we want to hide the home window when changing parameters? Will default back to it anwyays 
        #parameter_page()



            



