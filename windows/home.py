import tkinter as tk
from PIL import Image, ImageTk
import windows.parameters as win
import windows.welcome as wel
import windows.output as out
import windows.utils.serial_com as serial
import json

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

        # Connection label
        self.connection_label = tk.Label(self.window, text = "Connection Status:", font = ("Raleway", 14), width = 15, height = 1)
        self.connection_label.grid(columnspan = 2, column = 0, row = 0, sticky = "W")

        # Connection identifier (Modified later when test for connection)
        self.canvas.create_rectangle(180, 15, 210, 45, outline="#000000", fill="#00ee01")

        # Logo image 
        self.logo = Image.open('utils/logo.png')
        self.logo = self.logo.resize((300, 120), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.grid(rowspan = 2, columnspan = 2, column = 4, row = 0)

        # Username label
        self.username_label = tk.Label(self.window, text = "User: " + user, font = ("Raleway", 14))
        
        # Placing username label far enough away from edge so doesn't distort page
        if len(self.username_label["text"]) < 15:
            self.username_label.grid(column = 8, row = 0)
        else:
            self.username_label.grid(columnspan = 2, column = 7, row = 0)

        # Logout button
        self.logout_button = tk.Button(self.window, text = "Logout", bg="#20bebe", font = "Raleway",
                                       command = lambda: self.__logout(), fg = "white", height = 1, width = 8)
        self.logout_button.grid(column = 8, row = 1)

        # Mode dropdown options
        self.mode_options = [
            "AOO",
            "VOO", 
            "AAI", 
            "VVI", 
            "DOO", 
            "AOOR", 
            "VOOR", 
            "AAIR", 
            "VVIR", 
            "DOOR"
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
                                     command = lambda: self.__change_param())
        self.mode_button.grid(row = 7, column = 0)

        # Parameters label
        self.parameter_label = tk.Label(self.window, text = "Parameters:", font = ("Raleway", 18))
        self.parameter_label.grid(columnspan = 2, column = 4, row = 3)

        # Initializing parameters
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
        self.msr_label = tk.Label(self.window, text="Max Sensor Rate", font=("Raleway", 12))
        self.favd_label = tk.Label(self.window, text="Fixed AV Delay", font=("Raleway", 12))
        self.asen_label = tk.Label(self.window, text="Atrial Sensitivity", font=("Raleway", 12))
        self.vsen_label = tk.Label(self.window, text="Ventricular Sensitivity", font=("Raleway", 12))
        self.PVARP_label = tk.Label(self.window, text="PVARP", font=("Raleway", 12))
        self.hys_label = tk.Label(self.window, text="Hysteresis", font=("Raleway", 12))
        self.rs_label = tk.Label(self.window, text="Rate Smoothing", font=("Raleway", 12))
        self.at_label = tk.Label(self.window, text="Activity Threshold", font=("Raleway", 12))
        self.rct_label = tk.Label(self.window, text="Reaction Time", font=("Raleway", 12))
        self.rf_label = tk.Label(self.window, text="Response Factor", font=("Raleway", 12))
        self.rvt_label = tk.Label(self.window, text="Recovery Time", font=("Raleway", 12))

        # Initialize placeholder labels (to set discrete spaces where labels will always be)
        self.placeholder_label1 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label2 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label3 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label4 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label5 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label6 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label7 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label8 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label9 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label10 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label11 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label12 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label13 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label14 = tk.Label(self.window, text = "", font = ("Raleway", 12), width = 20, height = 1)
        self.placeholder_label1.grid(column = 4, row = 4)
        self.placeholder_label2.grid(column = 5, row = 4)
        self.placeholder_label3.grid(column = 4, row = 5)
        self.placeholder_label4.grid(column = 5, row = 5)
        self.placeholder_label5.grid(column = 4, row = 6)
        self.placeholder_label6.grid(column = 5, row = 6)
        self.placeholder_label7.grid(column = 4, row = 7)
        self.placeholder_label8.grid(column = 5, row = 7)
        self.placeholder_label9.grid(column = 4, row = 8)
        self.placeholder_label10.grid(column = 5, row = 8)
        self.placeholder_label11.grid(column = 4, row = 9)
        self.placeholder_label12.grid(column = 5, row = 9)
        self.placeholder_label13.grid(column = 4, row = 10)
        self.placeholder_label14.grid(column = 5, row = 10)

        # Edit Button
        self.edit_button = tk.Button(self.window, text = "Edit Parameters", width = 15, height = 1, 
                                    font = "Raleway", fg = "white", bg = "#20bebe", 
                                    command = lambda: self.__edit_param())
        self.edit_button.grid(column = 8, row = 7)

        # Run Button
        self.run_button = tk.Button(self.window, text = "Run", width = 15, height = 1, 
                                    font = "Raleway", fg = "white", bg = "#20bebe", 
                                    command = lambda: self.__run_model())
        self.run_button.grid(column = 8, row = 6)

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

    # logout function called when Logout button pushed, destroying home page and creating new welcome page
    def __logout(self):
        self.window.destroy()
        # Have to re-instantiate a new Tk() window to pass to welcome_page because the function doesn't make one itself
        wel.welcome_page(tk.Tk(), self.login_DB, self.param_DB) 
    
    # change_param function called when want to see parameters // change which parameter are viewing // editing 
    def __change_param(self):
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
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["AOO"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["AOO"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["AOO"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=5)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["AOO"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=5, row=5)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 4, row = 6)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 5, row = 6)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 4, row = 7)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 5, row = 7)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 4, row = 8)
            self.placeholder_label6 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label6.grid(column = 5, row = 8)
            self.placeholder_label7 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label7.grid(column = 4, row = 9)
            self.placeholder_label8 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label8.grid(column = 5, row = 9)
            self.placeholder_label9 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label9.grid(column = 4, row = 10)
            self.placeholder_label10 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label10.grid(column = 5, row = 10)
            
        elif self.default_mode.get() == "VOO":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["VOO"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["VOO"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["VOO"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=4, row=5)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["VOO"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=5, row=5)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 4, row = 6)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 5, row = 6)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 4, row = 7)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 5, row = 7)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 4, row = 8)
            self.placeholder_label6 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label6.grid(column = 5, row = 8)
            self.placeholder_label7 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label7.grid(column = 4, row = 9)
            self.placeholder_label8 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label8.grid(column = 5, row = 9)
            self.placeholder_label9 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label9.grid(column = 4, row = 10)
            self.placeholder_label10 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label10.grid(column = 5, row = 10)
            
        elif self.default_mode.get() == "AAI":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["AAI"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["AAI"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["AAI"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=5)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["AAI"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=5, row=5)
            self.ARP_label = tk.Label(self.window, text=f'ARP: {self.param_DB[dict_user]["AAI"]["ARP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.ARP_label.grid(column=4, row=6)
            self.asen_label = tk.Label(self.window, text=f'Atrial Sensitivity: {self.param_DB[dict_user]["AAI"]["asen"]}', font=("Raleway", 12), width = 20, height = 1)
            self.asen_label.grid(column=5, row=6)
            self.PVARP_label = tk.Label(self.window, text=f'PVARP: {self.param_DB[dict_user]["AAI"]["PVARP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.PVARP_label.grid(column=4, row=7)
            self.hys_label = tk.Label(self.window, text=f'Hysteresis: {self.param_DB[dict_user]["AAI"]["hys"]}', font=("Raleway", 12), width = 20, height = 1)
            self.hys_label.grid(column=5, row=7)
            self.rs_label = tk.Label(self.window, text=f'Rate Smoothing: {self.param_DB[dict_user]["AAI"]["rs"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rs_label.grid(column=4, row=8)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 5, row = 8)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 4, row = 9)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 5, row = 9)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 4, row = 10)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 5, row = 10)

        elif self.default_mode.get() == "VVI": 
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["VVI"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["VVI"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["VVI"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=4, row=5)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["VVI"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=5, row=5)
            self.VRP_label = tk.Label(self.window, text=f'VRP: {self.param_DB[dict_user]["VVI"]["VRP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.VRP_label.grid(column=4, row=6)
            self.vsen_label = tk.Label(self.window, text=f'Ventricular Sensitivity: {self.param_DB[dict_user]["VVI"]["vsen"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vsen_label.grid(column=5, row=6)
            self.hys_label = tk.Label(self.window, text=f'Hysteresis: {self.param_DB[dict_user]["VVI"]["hys"]}', font=("Raleway", 12), width = 20, height = 1)
            self.hys_label.grid(column=4, row=7)
            self.rs_label = tk.Label(self.window, text=f'Rate Smoothing: {self.param_DB[dict_user]["VVI"]["rs"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rs_label.grid(column=5, row=7)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 4, row = 8)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 5, row = 8)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 4, row = 9)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 5, row = 9)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 4, row = 10)
            self.placeholder_label6 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label6.grid(column = 5, row = 10)

        elif self.default_mode.get() == "DOO":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["DOO"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["DOO"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["DOO"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=5)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["DOO"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=5, row=5)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["DOO"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=4, row=6)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["DOO"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=5, row=6)
            self.favd_label = tk.Label(self.window, text=f'Fixed AV Delay: {self.param_DB[dict_user]["DOO"]["favd"]}', font=("Raleway", 12), width = 20, height = 1)
            self.favd_label.grid(column=4, row=7)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 5, row = 7)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 4, row = 8)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 5, row = 8)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 4, row = 9)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 5, row = 9)
            self.placeholder_label6 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label6.grid(column = 4, row = 10)
            self.placeholder_label7 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label7.grid(column = 5, row = 10)

        elif self.default_mode.get() == "AOOR":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["AOOR"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["AOOR"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["AOOR"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=5)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["AOOR"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=5, row=5)
            self.msr_label = tk.Label(self.window, text=f'Max Sensor Rate: {self.param_DB[dict_user]["AOOR"]["msr"]}', font=("Raleway", 12), width = 20, height = 1)
            self.msr_label.grid(column=4, row=6)
            self.at_label = tk.Label(self.window, text=f'Activity Threshold: {self.param_DB[dict_user]["AOOR"]["at"]}', font=("Raleway", 12), width = 20, height = 1)
            self.at_label.grid(column=5, row=6)
            self.rct_label = tk.Label(self.window, text=f'Reaction Time: {self.param_DB[dict_user]["AOOR"]["rct"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rct_label.grid(column=4, row=7)
            self.rf_label = tk.Label(self.window, text=f'Response Factor: {self.param_DB[dict_user]["AOOR"]["rf"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rf_label.grid(column=5, row=7)
            self.rvt_label = tk.Label(self.window, text=f'Recovery Time: {self.param_DB[dict_user]["AOOR"]["rvt"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rvt_label.grid(column=4, row=8)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 5, row = 8)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 4, row = 9)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 5, row = 9)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 4, row = 10)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 5, row = 10)

        elif self.default_mode.get() == "VOOR":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["VOOR"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["VOOR"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["VOOR"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=4, row=5)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["VOOR"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=5, row=5)
            self.msr_label = tk.Label(self.window, text=f'Max Sensor Rate: {self.param_DB[dict_user]["VOOR"]["msr"]}', font=("Raleway", 12), width = 20, height = 1)
            self.msr_label.grid(column=4, row=6)
            self.at_label = tk.Label(self.window, text=f'Activity Threshold: {self.param_DB[dict_user]["VOOR"]["at"]}', font=("Raleway", 12), width = 20, height = 1)
            self.at_label.grid(column=5, row=6)
            self.rct_label = tk.Label(self.window, text=f'Reaction Time: {self.param_DB[dict_user]["VOOR"]["rct"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rct_label.grid(column=4, row=7)
            self.rf_label = tk.Label(self.window, text=f'Response Factor: {self.param_DB[dict_user]["VOOR"]["rf"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rf_label.grid(column=5, row=7)
            self.rvt_label = tk.Label(self.window, text=f'Recovery Time: {self.param_DB[dict_user]["VOOR"]["rvt"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rvt_label.grid(column=4, row=8)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 5, row = 8)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 4, row = 9)
            self.placeholder_label3 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label3.grid(column = 5, row = 9)
            self.placeholder_label4 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label4.grid(column = 4, row = 10)
            self.placeholder_label5 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label5.grid(column = 5, row = 10)

        elif self.default_mode.get() == "AAIR":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["AAIR"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["AAIR"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["AAIR"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=5)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["AAIR"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=5, row=5)
            self.ARP_label = tk.Label(self.window, text=f'ARP: {self.param_DB[dict_user]["AAIR"]["ARP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.ARP_label.grid(column=4, row=6)
            self.msr_label = tk.Label(self.window, text=f'Max Sensor Rate: {self.param_DB[dict_user]["AAIR"]["msr"]}', font=("Raleway", 12), width = 20, height = 1)
            self.msr_label.grid(column=5, row=6)
            self.asen_label = tk.Label(self.window, text=f'Atrial Sensitivity: {self.param_DB[dict_user]["AAIR"]["asen"]}', font=("Raleway", 12), width = 20, height = 1)
            self.asen_label.grid(column=4, row=7)
            self.PVARP_label = tk.Label(self.window, text=f'PVARP: {self.param_DB[dict_user]["AAIR"]["PVARP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.PVARP_label.grid(column=5, row=7)
            self.hys_label = tk.Label(self.window, text=f'Hysteresis: {self.param_DB[dict_user]["AAIR"]["hys"]}', font=("Raleway", 12), width = 20, height = 1)
            self.hys_label.grid(column=4, row=8)
            self.rs_label = tk.Label(self.window, text=f'Rate Smoothing: {self.param_DB[dict_user]["AAIR"]["rs"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rs_label.grid(column=5, row=8)
            self.at_label = tk.Label(self.window, text=f'Activity Threshold: {self.param_DB[dict_user]["AAIR"]["at"]}', font=("Raleway", 12), width = 20, height = 1)
            self.at_label.grid(column=4, row=9)
            self.rct_label = tk.Label(self.window, text=f'Reaction Time: {self.param_DB[dict_user]["AAIR"]["rct"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rct_label.grid(column=5, row=9)
            self.rf_label = tk.Label(self.window, text=f'Response Factor: {self.param_DB[dict_user]["AAIR"]["rf"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rf_label.grid(column=4, row=10)
            self.rvt_label = tk.Label(self.window, text=f'Recovery Time: {self.param_DB[dict_user]["AAIR"]["rvt"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rvt_label.grid(column=5, row=10)

        elif self.default_mode.get() == "VVIR": 
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["VVIR"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["VVIR"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["VVIR"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=4, row=5)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["VVIR"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=5, row=5)
            self.VRP_label = tk.Label(self.window, text=f'VRP: {self.param_DB[dict_user]["VVIR"]["VRP"]}', font=("Raleway", 12), width = 20, height = 1)
            self.VRP_label.grid(column=4, row=6)
            self.msr_label = tk.Label(self.window, text=f'Max Sensor Rate: {self.param_DB[dict_user]["VVIR"]["msr"]}', font=("Raleway", 12), width = 20, height = 1)
            self.msr_label.grid(column=5, row=6)
            self.vsen_label = tk.Label(self.window, text=f'Ventricular Sensitivity: {self.param_DB[dict_user]["VVIR"]["vsen"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vsen_label.grid(column=4, row=7)
            self.hys_label = tk.Label(self.window, text=f'Hysteresis: {self.param_DB[dict_user]["VVIR"]["hys"]}', font=("Raleway", 12), width = 20, height = 1)
            self.hys_label.grid(column=5, row=7)
            self.rs_label = tk.Label(self.window, text=f'Rate Smoothing: {self.param_DB[dict_user]["VVIR"]["rs"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rs_label.grid(column=4, row=8)
            self.at_label = tk.Label(self.window, text=f'Activity Threshold: {self.param_DB[dict_user]["VVIR"]["at"]}', font=("Raleway", 12), width = 20, height = 1)
            self.at_label.grid(column=5, row=8)
            self.rct_label = tk.Label(self.window, text=f'Reaction Time: {self.param_DB[dict_user]["VVIR"]["rct"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rct_label.grid(column=4, row=9)
            self.rf_label = tk.Label(self.window, text=f'Response Factor: {self.param_DB[dict_user]["VVIR"]["rf"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rf_label.grid(column=5, row=9)
            self.rvt_label = tk.Label(self.window, text=f'Recovery Time: {self.param_DB[dict_user]["VVIR"]["rvt"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rvt_label.grid(column=4, row=10)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 5, row = 10)

        elif self.default_mode.get() == "DOOR":
            self.lrl_label.destroy()
            self.url_label.destroy()
            self.aa_label.destroy()
            self.apw_label.destroy()
            self.va_label.destroy()
            self.vpw_label.destroy()
            self.VRP_label.destroy()
            self.ARP_label.destroy()
            self.msr_label.destroy()
            self.favd_label.destroy()
            self.asen_label.destroy()
            self.vsen_label.destroy()
            self.PVARP_label.destroy()
            self.hys_label.destroy()
            self.rs_label.destroy()
            self.at_label.destroy()
            self.rct_label.destroy()
            self.rf_label.destroy()
            self.rvt_label.destroy()
            self.lrl_label = tk.Label(self.window, text=f'Lower Rate Limit: {self.param_DB[dict_user]["DOOR"]["lrl"]}', font=("Raleway", 12), width = 20, height = 1)
            self.lrl_label.grid(column=4, row=4)
            self.url_label = tk.Label(self.window, text=f'Upper Rate Limit: {self.param_DB[dict_user]["DOOR"]["url"]}', font=("Raleway", 12), width = 20, height = 1)
            self.url_label.grid(column=5, row=4)
            self.aa_label = tk.Label(self.window, text=f'Atrial Amplitude: {self.param_DB[dict_user]["DOOR"]["aa"]}', font=("Raleway", 12), width = 20, height = 1)
            self.aa_label.grid(column=4, row=5)
            self.va_label = tk.Label(self.window, text=f'Ventricular Amplitude: {self.param_DB[dict_user]["DOOR"]["va"]}', font=("Raleway", 12), width = 20, height = 1)
            self.va_label.grid(column=5, row=5)
            self.apw_label = tk.Label(self.window, text=f'Atrial Pulse Width: {self.param_DB[dict_user]["DOOR"]["apw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.apw_label.grid(column=4, row=6)
            self.vpw_label = tk.Label(self.window, text=f'Ventricular Pulse Width: {self.param_DB[dict_user]["DOOR"]["vpw"]}', font=("Raleway", 12), width = 20, height = 1)
            self.vpw_label.grid(column=5, row=6)
            self.favd_label = tk.Label(self.window, text=f'Fixed AV Delay: {self.param_DB[dict_user]["DOOR"]["favd"]}', font=("Raleway", 12), width = 20, height = 1)
            self.favd_label.grid(column=4, row=7)
            self.msr_label = tk.Label(self.window, text=f'Max Sensor Rate: {self.param_DB[dict_user]["DOOR"]["msr"]}', font=("Raleway", 12), width = 20, height = 1)
            self.msr_label.grid(column=5, row=7)
            self.at_label = tk.Label(self.window, text=f'Activity Threshold: {self.param_DB[dict_user]["DOOR"]["at"]}', font=("Raleway", 12), width = 20, height = 1)
            self.at_label.grid(column=4, row=8)
            self.rct_label = tk.Label(self.window, text=f'Reaction Time: {self.param_DB[dict_user]["DOOR"]["rct"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rct_label.grid(column=5, row=8)
            self.rf_label = tk.Label(self.window, text=f'Response Factor: {self.param_DB[dict_user]["DOOR"]["rf"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rf_label.grid(column=4, row=9)
            self.rvt_label = tk.Label(self.window, text=f'Recovery Time: {self.param_DB[dict_user]["DOOR"]["rvt"]}', font=("Raleway", 12), width = 20, height = 1)
            self.rvt_label.grid(column=5, row=9)
            self.placeholder_label1 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label1.grid(column = 4, row = 10)
            self.placeholder_label2 = tk.Label(self.window, text="", font=("Raleway", 12), width = 20, height = 1)
            self.placeholder_label2.grid(column = 5, row = 10)

    # edit_param function calls the corresponding class in parameters.py file to edit its parameters 
    def __edit_param(self):
        if self.default_mode.get() == "AOO":
            win.AOO(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "VOO":
            win.VOO(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "AAI":
            win.AAI(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "VVI":
            win.VVI(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "DOO":
            win.DOO(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "AOOR":
            win.AOOR(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "VOOR":
            win.VOOR(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "AAIR":
            win.AAIR(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "VVIR":
            win.VVIR(self.window, self.user, self.param_DB)
        elif self.default_mode.get() == "DOOR":
            win.DOOR(self.window, self.user, self.param_DB)

    # run_model function launches the output window while keeping homepage window open in background 
    def __run_model(self):
        with open("database/parameters.json") as database2:
            parameter_database = json.load(database2)

        if self.user in parameter_database.keys() and self.default_mode.get() in parameter_database[self.user].keys():
            dict_user = self.user
        else:
            dict_user = "default"

        param_dict = parameter_database[dict_user][self.default_mode.get()]
        param_dict["mode"] = self.param_index[self.default_mode.get()]

        if not serial.findPorts():
            self.canvas.create_rectangle(180, 15, 210, 45, outline="#000000", fill="#FF0000")
            return 0
        else:
            self.canvas.create_rectangle(180, 15, 210, 45, outline="#000000", fill="#00ee01")

        packet = list(serial.serial_packet(param_dict).transmit_params(3))
        out.output_page(self.window, self.user, self.default_mode.get(), parameter_database, packet)
