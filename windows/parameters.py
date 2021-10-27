import tkinter as tk
import json


# class parameter_page:
#     def __init__(self, root, user, parameter_database):
#         # Intialize Current User
#         self.user = user

#         # Intialize database
#         self.DB = parameter_database

#         # Intialize parameter limits
#         self.limits = {
#             "lrl": {
#                 "column": 2,
#                 "row": 1
#             },
#             "url": {
#                 "column": 2,
#                 "row": 2
#             },
#             "aa": {
#                 "column": 2,
#                 "row": 3
#             },
#             "apw": {
#                 "column": 2,
#                 "row": 4
#             },
#             "va": {
#                 "column": 6,
#                 "row": 1
#             },
#             "vpw": {
#                 "column": 6,
#                 "row": 2
#             },
#             "VRP": {
#                 "column": 6,
#                 "row": 3
#             },
#             "ARP": {
#                 "column": 6,
#                 "row": 4
#             }
#         }

#         # Build canvas
#         self.root = root
#         # self.window = tk.Toplevel(self.root)
#         self.root.destroy()

#         self.window = tk.Tk()
#         self.window.title("Parameters")
#         self.canvas = tk.Canvas(self.window, width=1000, height=500)
#         self.canvas.grid(columnspan=8, rowspan=6)

#         self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18))
#         self.title_label.grid(column=0, row=0)

#         # Initialize all Entry fields
#         self.lrl = tk.Entry(self.window)
#         self.lrl.grid(column=1, row=1)
#         self.url = tk.Entry(self.window)
#         self.url.grid(column=1, row=2)
#         self.aa = tk.Entry(self.window)
#         self.aa.grid(column=1, row=3)
#         self.apw = tk.Entry(self.window)
#         self.apw.grid(column=1, row=4)
#         self.va = tk.Entry(self.window)
#         self.va.grid(column=5, row=1)
#         self.vpw = tk.Entry(self.window)
#         self.vpw.grid(column=5, row=2)
#         self.VRP = tk.Entry(self.window)
#         self.VRP.grid(column=5, row=3)
#         self.ARP = tk.Entry(self.window)
#         self.ARP.grid(column=5, row=4)

#         # Initialize Labels
#         self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
#         self.lrl_label.grid(column=0, row=1)
#         self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
#         self.url_label.grid(column=0, row=2)
#         self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
#         self.aa_label.grid(column=0, row=3)
#         self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
#         self.apw_label.grid(column=0, row=4)
#         self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
#         self.va_label.grid(column=4, row=1)
#         self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
#         self.vpw_label.grid(column=4, row=2)
#         self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.VRP_label.grid(column=4, row=3)
#         self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
#         self.ARP_label.grid(column=4, row=4)

#         # Intialize "invalid" label
#         self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_va = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_vpw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_VRP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_ARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))

#         # Initialize Save Button
#         save_btn_text = tk.StringVar()
#         self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
#                                   font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
#         save_btn_text.set("Save")
#         self.save_btn.grid(columnspan=4, column=1, row=6)

#     def check_lrl(self, lrl_input):
#         # Check which range the lrl input falls in
#         if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
#             return True
#         elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
#             return True
#         elif lrl_input < 30 or lrl_input > 175:
#             self.invalid_label_lrl.grid(column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
#             return False
#         else:
#             return True

#     def check_url(self, url_input):
#         # Check which range the lrl input falls in
#         if 50 <= url_input <= 175 and url_input % 5 == 0:
#             return True
#         else:
#             self.invalid_label_url.grid(column=self.limits["url"]["column"], row=self.limits["url"]["row"])
#             return False

#     def check_atrial_amplitude(self, amplitude_input):
#         if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
#             return True
#         else:
#             self.invalid_label_aa.grid(column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
#             return False

#     def check_ventricle_amplitude(self, amplitude_input):
#         if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
#             return True
#         else:
#             self.invalid_label_va.grid(column=self.limits["va"]["column"], row=self.limits["va"]["row"])
#             return False

#     def check_apw(self, pw_input):
#         if pw_input == 1 or pw_input == 2:
#             return True
#         else:
#             self.invalid_label_apw.grid(column=self.limits["apw"]["column"], row=self.limits["apw"]["row"])
#             return False

#     def check_vpw(self, pw_input):
#         if pw_input == 1 or pw_input == 2:
#             return True
#         else:
#             self.invalid_label_vpw.grid(column=self.limits["vpw"]["column"], row=self.limits["vpw"]["row"])
#             return False

#     def check_atrial_refractory_period(self, RP_input):
#         if 150 <= RP_input <= 500 and RP_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_ARP.grid(column=self.limits["ARP"]["column"], row=self.limits["ARP"]["row"])
#             return False

#     def check_ventricle_refractory_period(self, RP_input):
#         if 150 <= RP_input <= 500 and RP_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_VRP.grid(column=self.limits["VRP"]["column"], row=self.limits["VRP"]["row"])
#             return False

#     def check_validity(self):
#         # Remove previous invalid labels
#         self.invalid_label_lrl.grid_remove()
#         self.invalid_label_url.grid_remove()
#         self.invalid_label_aa.grid_remove()
#         self.invalid_label_apw.grid_remove()
#         self.invalid_label_va.grid_remove()
#         self.invalid_label_vpw.grid_remove()
#         self.invalid_label_VRP.grid_remove()
#         self.invalid_label_ARP.grid_remove()

#         input_params = {
#             "lrl": self.lrl.get(),
#             "url": self.url.get(),
#             "aa": self.aa.get(),
#             "apw": self.apw.get(),
#             "va": self.va.get(),
#             "vpw": self.vpw.get(),
#             "VRP": self.VRP.get(),
#             "ARP": self.ARP.get()
#         }

#         # Checking if any entries are empty
#         for param in input_params.keys():
#             if input_params[param] == "":
#                 return

#         valid_params = [self.check_lrl(int(self.lrl.get())), self.check_url(int(self.url.get())),
#                         self.check_atrial_amplitude(float(self.aa.get())),
#                         self.check_ventricle_amplitude(float(self.va.get())),
#                         self.check_apw(int(self.apw.get())), self.check_vpw(int(self.vpw.get())),
#                         self.check_atrial_refractory_period(int(self.ARP.get())),
#                         self.check_ventricle_refractory_period(int(self.VRP.get()))]

#         # Checking lrl separately due to increment differences

#         if False not in valid_params:
#             self.save_parameters(input_params)

#     def save_parameters(self, inputs):
#         self.DB[self.user] = inputs
#         print(self.DB)
#         with open("database/parameters.json", "w") as destination:
#             json.dump(self.DB, destination)
#         self.window.destroy()

# ---------------------------------------------AOO-----------------------------------------------
class AOO:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize parameter limits
        self.limits = {
            "lrl": {
                "column": 2,
                "row": 1
            },
            "url": {
                "column": 2,
                "row": 2
            },
            "aa": {
                "column": 6,
                "row": 1
            },
            "apw": {
                "column": 6,
                "row": 2
            }
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        # self.root.destroy()

        # self.window = tk.Tk()
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=500)
        self.canvas.grid(columnspan=8, rowspan=6)

        self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18))
        self.title_label.grid(column=0, row=0)

        # Initialize all Entry fields
        self.lrl = tk.Entry(self.window)
        self.lrl.grid(column=1, row=1)
        self.url = tk.Entry(self.window)
        self.url.grid(column=1, row=2)
        self.aa = tk.Entry(self.window)
        self.aa.grid(column=5, row=1)
        self.apw = tk.Entry(self.window)
        self.apw.grid(column=5, row=2)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=4, row=1)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=4, row=2)

        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.blank_label = tk.Label(self.window, text="All fields must be filled in", font=("Raleway", 12))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.9, anchor="center")

    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False

        # Check which range the lrl input falls in
        if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
            return True
        elif 50 <= lrl_input <= 90:
            return True
        elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
            return True
        elif lrl_input < 30 or lrl_input > 175:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False
        else:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False

    def check_url(self, url_input):
        # Check if correct datatype was entered
        try:
            url_input = int(url_input)
        except:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"], row=self.limits["url"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= url_input <= 175 and url_input % 5 == 0:
            return True
        else:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"], row=self.limits["url"]["row"])
            return False

    def check_atrial_amplitude(self, amplitude_input):
        # Check if correct datatype was entered
        try:
            amplitude_input = float(amplitude_input)
        except:
            self.invalid_label_aa.grid(columnspan=2, column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
            return False

        if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
            return True
        else:
            self.invalid_label_aa.grid(columnspan=2, column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
            return False

    def check_apw(self, pw_input):
        # Check if correct datatype was entered
        try:
            pw_input = int(pw_input)
        except:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"], row=self.limits["apw"]["row"])
            return False

        if pw_input == 1 or pw_input == 2:
            return True
        else:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"], row=self.limits["apw"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.blank_label.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()),
                        self.check_apw(self.apw.get())]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["AOO"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()


# ----------------------------------------------AAI-----------------------------------------------
class AAI:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize parameter limits
        self.limits = {
            "lrl": {
                "column": 2,
                "row": 1
            },
            "url": {
                "column": 2,
                "row": 2
            },
            "aa": {
                "column": 2,
                "row": 3
            },
            "apw": {
                "column": 6,
                "row": 1
            },
            "ARP": {
                "column": 6,
                "row": 2
            }
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        # self.root.destroy()

        # self.window = tk.Tk()
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=500)
        self.canvas.grid(columnspan=8, rowspan=6)

        self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18))
        self.title_label.grid(column=0, row=0)

        # Initialize all Entry fields
        self.lrl = tk.Entry(self.window)
        self.lrl.grid(column=1, row=1)
        self.url = tk.Entry(self.window)
        self.url.grid(column=1, row=2)
        self.aa = tk.Entry(self.window)
        self.aa.grid(column=1, row=3)
        self.apw = tk.Entry(self.window)
        self.apw.grid(column=5, row=1)
        self.ARP = tk.Entry(self.window)
        self.ARP.grid(column=5, row=2)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=0, row=3)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=4, row=1)
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
        self.ARP_label.grid(column=4, row=2)

        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_ARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.blank_label = tk.Label(self.window, text="All fields must be filled in", font=("Raleway", 12))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.9, anchor="center")

    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False

        # Check which range the lrl input falls in
        if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
            return True
        elif 50 <= lrl_input <= 90:
            return True
        elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
            return True
        elif lrl_input < 30 or lrl_input > 175:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False
        else:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False

    def check_url(self, url_input):
        # Check if correct datatype was entered
        try:
            url_input = int(url_input)
        except:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"], row=self.limits["url"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= url_input <= 175 and url_input % 5 == 0:
            return True
        else:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"], row=self.limits["url"]["row"])
            return False

    def check_atrial_amplitude(self, amplitude_input):
        # Check if correct datatype was entered
        try:
            amplitude_input = float(amplitude_input)
        except:
            self.invalid_label_aa.grid(columnspan=2, column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
            return False

        if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
            return True
        else:
            self.invalid_label_aa.grid(columnspan=2, column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
            return False

    def check_apw(self, pw_input):
        # Check if correct datatype was entered
        try:
            pw_input = int(pw_input)
        except:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"], row=self.limits["apw"]["row"])
            return False

        if pw_input == 1 or pw_input == 2:
            return True
        else:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"], row=self.limits["apw"]["row"])
            return False

    def check_atrial_refractory_period(self, RP_input):
        # Check if correct datatype was entered
        try:
            RP_input = int(RP_input)
        except:
            self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"], row=self.limits["ARP"]["row"])
            return False

        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"], row=self.limits["ARP"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.invalid_label_ARP.grid_remove()
        self.blank_label.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "ARP": self.ARP.get()
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()),
                        self.check_apw(self.apw.get()), self.check_atrial_refractory_period(self.ARP.get())]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["AAI"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()


# ----------------------------------------------VOO-----------------------------------------------
class VOO:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize parameter limits
        self.limits = {
            "lrl": {
                "column": 2,
                "row": 1
            },
            "url": {
                "column": 2,
                "row": 2
            },
            "va": {
                "column": 6,
                "row": 1
            },
            "vpw": {
                "column": 6,
                "row": 2
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        # self.root.destroy()

        # self.window = tk.Tk()
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=500)
        self.canvas.grid(columnspan=8, rowspan=6)

        self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18))
        self.title_label.grid(column=0, row=0)

        # Initialize all Entry fields
        self.lrl = tk.Entry(self.window)
        self.lrl.grid(column=1, row=1)
        self.url = tk.Entry(self.window)
        self.url.grid(column=1, row=2)
        self.va = tk.Entry(self.window)
        self.va.grid(column=5, row=1)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=2)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=1)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=2)

        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_url = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_va = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_vpw = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.blank_label = tk.Label(self.window, text="All fields must be filled in", font=("Raleway", 12), width=19,
                                    height=1)

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.9, anchor="center")

    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Check which range the lrl input falls in
        if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
            return True
        elif 50 <= lrl_input <= 90:
            return True
        elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
            return True
        elif lrl_input < 30 or lrl_input > 175:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False
        else:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

    def check_url(self, url_input):
        # Check if correct datatype was entered
        try:
            url_input = int(url_input)
        except:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
                                        row=self.limits["url"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= url_input <= 175 and url_input % 5 == 0:
            return True
        else:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
                                        row=self.limits["url"]["row"])
            return False

    def check_ventricle_amplitude(self, amplitude_input):
        # Check if correct datatype was entered
        try:
            amplitude_input = float(amplitude_input)
        except:
            self.invalid_label_va.grid(columnspan=2, column=self.limits["va"]["column"], row=self.limits["va"]["row"])
            return False

        if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
            return True
        else:
            self.invalid_label_va.grid(columnspan=2, column=self.limits["va"]["column"], row=self.limits["va"]["row"])
            return False

    def check_vpw(self, pw_input):
        # Check if correct datatype was entered
        try:
            pw_input = int(pw_input)
        except:
            self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
                                        row=self.limits["vpw"]["row"])
            return False

        if pw_input == 1 or pw_input == 2:
            return True
        else:
            self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
                                        row=self.limits["vpw"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.blank_label.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_ventricle_amplitude(self.va.get()), self.check_vpw(self.vpw.get())]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["VOO"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()


# ----------------------------------------------VVI-----------------------------------------------
class VVI:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize parameter limits
        self.limits = {
            "lrl": {
                "column": 2,
                "row": 1
            },
            "url": {
                "column": 2,
                "row": 2
            },
            "va": {
                "column": 2,
                "row": 3
            },
            "vpw": {
                "column": 6,
                "row": 1
            },
            "VRP": {
                "column": 6,
                "row": 2
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        # self.root.destroy()

        # self.window = tk.Tk()
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=500)
        self.canvas.grid(columnspan=9, rowspan=6)

        self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18), width=20, height=1)
        self.title_label.grid(column=0, row=0)

        # Initialize all Entry fields
        self.lrl = tk.Entry(self.window)
        self.lrl.grid(column=1, row=1)
        self.url = tk.Entry(self.window)
        self.url.grid(column=1, row=2)
        self.va = tk.Entry(self.window)
        self.va.grid(column=1, row=3)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=1)
        self.VRP = tk.Entry(self.window)
        self.VRP.grid(column=5, row=2)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12), width=20, height=1)
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12), width=20, height=1)
        self.url_label.grid(column=0, row=2)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12), width=20, height=1)
        self.va_label.grid(column=0, row=3)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12), width=20, height=1)
        self.vpw_label.grid(column=4, row=1)
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12), width=20, height=1)
        self.VRP_label.grid(column=4, row=2)

        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_url = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_va = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_vpw = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_VRP = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.blank_label = tk.Label(self.window, text="All fields must be filled in", font=("Raleway", 12), width=19,
                                    height=1)

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.9, anchor="center")

    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Check which range the lrl input falls in
        if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
            return True
        elif 50 <= lrl_input <= 90:
            return True
        elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
            return True
        elif lrl_input < 30 or lrl_input > 175:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False
        else:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

    def check_url(self, url_input):
        # Check if correct datatype was entered
        try:
            url_input = int(url_input)
        except:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
                                        row=self.limits["url"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= url_input <= 175 and url_input % 5 == 0:
            return True
        else:
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
                                        row=self.limits["url"]["row"])
            return False

    def check_ventricle_amplitude(self, amplitude_input):
        # Check if correct datatype was entered
        try:
            amplitude_input = float(amplitude_input)
        except:
            self.invalid_label_va.grid(columnspan=2, column=self.limits["va"]["column"], row=self.limits["va"]["row"])
            return False

        if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
            return True
        else:
            self.invalid_label_va.grid(columnspan=2, column=self.limits["va"]["column"], row=self.limits["va"]["row"])
            return False

    def check_vpw(self, pw_input):
        # Check if correct datatype was entered
        try:
            pw_input = int(pw_input)
        except:
            self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
                                        row=self.limits["vpw"]["row"])
            return False

        if pw_input == 1 or pw_input == 2:
            return True
        else:
            self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
                                        row=self.limits["vpw"]["row"])
            return False

    def check_ventricle_refractory_period(self, RP_input):
        # Check if correct datatype was entered
        try:
            RP_input = int(RP_input)

        except:
            self.invalid_label_VRP.grid(columnspan=2, column=self.limits["VRP"]["column"],
                                        row=self.limits["VRP"]["row"])
            return False

        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label_VRP.grid(columnspan=2, column=self.limits["VRP"]["column"],
                                        row=self.limits["VRP"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.invalid_label_VRP.grid_remove()
        self.blank_label.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "VRP": self.VRP.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_ventricle_amplitude(self.va.get()), self.check_vpw(self.vpw.get()),
                        self.check_ventricle_refractory_period(self.VRP.get())]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["VVI"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
