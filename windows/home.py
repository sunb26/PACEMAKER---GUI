import tkinter as tk
from PIL import Image, ImageTk
import windows.parameters as win
import windows.welcome as wel
import windows.output as out

class home_page:
    def __init__(self, root, user, login_database, parameter_database): 
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
        self.canvas.grid(columnspan = 9, rowspan = 12)

        # Device name label 
        self.device_label = tk.Label(self.window, text = "Device Name: __________", font = ("Raleway", 14), width = 22, height = 1)
        self.device_label.grid(columnspan = 2, column = 0, row = 0, sticky = "W")

        # Device name 
            # In final version, use some function to get the device name and display it beside the semicolon of "Device Name"

        # Connection label
        self.connection_label = tk.Label(self.window, text = "Connection Status:", font = ("Raleway", 14), width = 15, height = 1)
        self.connection_label.grid(columnspan = 2, column = 0, row = 1, sticky = "W")

        # Connection identifier
            # In final version, use if statement to determine if the device is connected or not, then if so 
            # display the green rectangle, and if not display the red rectangle 
        self.canvas.create_rectangle(180, 75, 210, 105, outline="#000000", fill="#00ee01")

        # Logo image 
        self.logo = Image.open('utils/logo.png')
        self.logo = self.logo.resize((300, 120), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.grid(rowspan = 2, column = 4, row = 0)

        # Username label
        self.username_label = tk.Label(self.window, text = "User: " + user, font = ("Raleway", 14))
        
        # Placing username label far enough away from edge so doesn't distort page
        if len(self.username_label["text"]) < 15:
            self.username_label.grid(column = 8, row = 0)
        else:
            self.username_label.grid(columnspan = 2, column = 7, row = 0)

        # Logout button
        self.logout_button = tk.Button(self.window, text = "Logout", bg="#20bebe", font = "Raleway",
                                       command = lambda: self.logout(), fg = "white", height = 1, width = 8)
        self.logout_button.grid(column = 8, row = 1)

        # Mode dropdown options
        self.mode_options = [
            "AOO",
            "VOO", 
            "AAI", 
            "VVI"
        ]

        # Setting default drop down menu item as "AOO"
        self.default_mode = tk.StringVar(self.window)
        self.default_mode.set(self.mode_options[0])

        # Creating drop down menu 
        self.opt = tk.OptionMenu(self.window, self.default_mode, *self.mode_options)
        tk.Label(self.window, text = "Choose Mode:", font = ("Raleway", 14), width = 12, height = 1).grid(column = 0, row = 5)
        self.opt.config(width = 10, height = 1, font = ("Raleway", 14))
        self.opt.grid(column = 0, row = 6)

        # Button to update parameter values
        self.mode_button = tk.Button(self.window, text = "View Parameters", width = 15, height = 1, 
                                     font = "Raleway", fg = "white", bg = "#20bebe", 
                                     command = lambda: self.change_param())
        self.mode_button.grid(row = 7, column = 0)

        # Parameters label
        self.parameter_label = tk.Label(self.window, text = "Parameters:", font = ("Raleway", 18))
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

        # Initialize placeholder labels (to set discrete spaces where labels will always be)
        self.placeholder_label1 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label2 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label3 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label4 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label5 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label1.grid(column = 4, row = 4)
        self.placeholder_label2.grid(column = 4, row = 5)
        self.placeholder_label3.grid(column = 4, row = 6)
        self.placeholder_label4.grid(column = 4, row = 7)
        self.placeholder_label5.grid(column = 4, row = 8)
        
        # Edit Button
        self.edit_button = tk.Button(self.window, text = "Edit Parameters", width = 15, height = 1, 
                                    font = "Raleway", fg = "white", bg = "#20bebe", 
                                    command = lambda: self.edit_param())
        self.edit_button.grid(column = 8, row = 7)

        # Run Button
        self.run_button = tk.Button(self.window, text = "Run", width = 15, height = 1, 
                                    font = "Raleway", fg = "white", bg = "#20bebe", 
                                    command = lambda: self.run_model())
        self.run_button.grid(column = 8, row = 6)

    # logout function called when logout button pushed, destroying home page and creating new welcome page
    def logout(self):
        self.window.destroy()
        # Have to re-instantiate a new Tk() window to pass to welcome_page because the function doesn't make one itself
        wel.welcome_page(tk.Tk(), self.login_DB, self.param_DB) 
    
    # change_param function called when want to see parameters // change which parameter are viewing // editing 
    def change_param(self):
        if self.user in self.param_DB.keys() and self.default_mode.get() in self.param_DB[self.user].keys():
            dict_user = self.user
        else:
            dict_user = "default"
        
        if self.default_mode.get() == "AOO":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["AOO"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["AOO"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=4, row=5)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["AOO"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=6)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["AOO"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=4, row=7)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 4, row = 8)
            
        elif self.default_mode.get() == "VOO":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["VOO"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["VOO"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=4, row=5)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["VOO"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=4, row=6)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["VOO"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=4, row=7)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 4, row = 8)
            
        elif self.default_mode.get() == "AAI":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["AAI"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["AAI"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=4, row=5)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["AAI"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=6)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["AAI"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=4, row=7)
            self.ARP_label = tk.Label(self.window, text=f'ARP: {self.param_DB[dict_user]["AAI"]["ARP"]}', font=("Raleway", 12), width = 20, height = 1)
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
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["VVI"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["VVI"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=4, row=5)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["VVI"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=4, row=6)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["VVI"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=4, row=7)
            self.VRP_label = tk.Label(self.window, text=f'VRP: {self.param_DB[dict_user]["VVI"]["VRP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.VRP_label.grid(column=4, row=8)

    # edit_param function calls the corresponding class in parameters.py file to edit its parameters 
    def edit_param(self):
        if self.default_mode.get() == "AOO":
            win.AOO(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "VOO":
            win.VOO(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "AAI":
            win.AAI(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "VVI":
            win.VVI(self.window, self.user, self.param_DB)

    # run_model function launches the output window while keeping homepage window open in background 
    def run_model(self):
        out.output_page(self.window)
