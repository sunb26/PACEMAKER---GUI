import tkinter as tk
import json


# class parameter_page:
#     def __init__(self, root, user, parameter_database):
#         # Intialize Current User
#         self.user = user
#
#         # Intialize database
#         self.DB = parameter_database
#
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
#
#         # Build canvas
#         self.root = root
#         # self.window = tk.Toplevel(self.root)
#         self.root.destroy()
#
#         self.window = tk.Tk()
#         self.window.title("Parameters")
#         self.canvas = tk.Canvas(self.window, width=1000, height=500)
#         self.canvas.grid(columnspan=8, rowspan=6)
#
#         self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18))
#         self.title_label.grid(column=0, row=0)
#
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
#         self.msr = tk.Entry(self.window)
#         self.msr.grid(column=, row=)
#         self.favd = tk.Entry(self.window)
#         self.favd.grid(column=, row=)
#         self.asen = tk.Entry(self.window)
#         self.asen.grid(column=, row=)
#         self.vsen = tk.Entry(self.window)
#         self.vsen.grid(column=, row=)
#         self.PVARP = tk.Entry(self.window)
#         self.PVARP.grid(column=, row=)
#         self.hys = tk.Entry(self.window)
#         self.hys.grid(column=, row=)
#         self.rs = tk.Entry(self.window)
#         self.rs.grid(column=, row=)
#         self.at = tk.Entry(self.window)
#         self.at.grid(column=, row=)
#         self.rct = tk.Entry(self.window)
#         self.rct.grid(column=, row=)
#         self.rf = tk.Entry(self.window)
#         self.rf.grid(column=, row=)
#         self.rvt = tk.Entry(self.window)
#         self.rvt.grid(column=,row=)
#
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
#         self.msr_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.msr_label.grid(column=, row=)
#         self.favd_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.favd_label.grid(column=, row=)
#         self.asen_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.asen_label.grid(column=, row=)
#         self.vsen_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.vsen_label.grid(column=, row=)
#         self.PVARP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.PVARP_label.grid(column=, row=)
#         self.hys_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.hys_label.grid(column=, row=)
#         self.rs_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.rs_label.grid(column=, row=)
#         self.at_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.at_label.grid(column=, row=)
#         self.rct_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.rct_label.grid(column=, row=)
#         self.rf_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.rf_label.grid(column=, row=)
#         self.rvt_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
#         self.rvt_label.grid(column=, row=)
#
#
#
#         # Intialize "invalid" label
#         self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_va = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_vpw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_VRP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_ARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_msr = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_favd = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_asen = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_vsen = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_PVARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_hys = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_rs = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_at = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_rct = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_rf = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#         self.invalid_label_rvt = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
#
#         # Initialize Save Button
#         save_btn_text = tk.StringVar()
#         self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
#                                   font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
#         save_btn_text.set("Save")
#         self.save_btn.grid(columnspan=4, column=1, row=6)
#
#
#
#     def check_lrl(self, lrl_input):
#         # Check if correct datatype was entered
#         try:
#             lrl_input = int(lrl_input)
#         except:
#             self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
#                                         row=self.limits["lrl"]["row"])
#             return False
#
#         # Check which range the lrl input falls in
#         if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
#             return True
#         elif 50 <= lrl_input <= 90:
#             return True
#         elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
#             return True
#         elif lrl_input < 30 or lrl_input > 175:
#             self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
#                                         row=self.limits["lrl"]["row"])
#             return False
#         else:
#             self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
#                                         row=self.limits["lrl"]["row"])
#             return False
#
#     def check_url(self, url_input):
#         # Check if correct datatype was entered
#         try:
#             url_input = int(url_input)
#         except:
#             self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
#                                         row=self.limits["url"]["row"])
#             return False
#
#         # Check which range the lrl input falls in
#         if 50 <= url_input <= 175 and url_input % 5 == 0:
#             return True
#         else:
#             self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
#                                         row=self.limits["url"]["row"])
#             return False
#
#     def check_atrial_amplitude(self, amplitude_input):
#         # Check if correct datatype was entered
#         try:
#             amplitude_input = float(amplitude_input)
#         except:
#             self.invalid_label_aa.grid(columnspan=2, column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
#             return False
#
#         if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
#             return True
#         else:
#             self.invalid_label_aa.grid(columnspan=2, column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
#             return False
#
#     def check_apw(self, pw_input):
#         # Check if correct datatype was entered
#         try:
#             pw_input = int(pw_input)
#         except:
#             self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
#                                         row=self.limits["apw"]["row"])
#             return False
#
#         if 1 <= pw_input <= 30:
#             return True
#         else:
#             self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
#                                         row=self.limits["apw"]["row"])
#             return False
#
#     def check_atrial_refractory_period(self, RP_input):
#         # Check if correct datatype was entered
#         try:
#             RP_input = int(RP_input)
#         except:
#             self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"],
#                                         row=self.limits["ARP"]["row"])
#             return False
#
#         if 150 <= RP_input <= 500 and RP_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"],
#                                         row=self.limits["ARP"]["row"])
#             return False
#
#     def check_ventricle_amplitude(self, amplitude_input):
#         # Check if correct datatype was entered
#         try:
#             amplitude_input = float(amplitude_input)
#         except:
#             self.invalid_label_va.grid(columnspan=2, column=self.limits["va"]["column"], row=self.limits["va"]["row"])
#             return False
#
#         if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input, 1) == amplitude_input:
#             return True
#         else:
#             self.invalid_label_va.grid(columnspan=2, column=self.limits["va"]["column"], row=self.limits["va"]["row"])
#             return False
#
#     def check_vpw(self, pw_input):
#         # Check if correct datatype was entered
#         try:
#             pw_input = int(pw_input)
#         except:
#             self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
#                                         row=self.limits["vpw"]["row"])
#             return False
#
#         if 1 <= pw_input <= 30:
#             return True
#         else:
#             self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
#                                         row=self.limits["vpw"]["row"])
#             return False
#
#     def check_ventricle_refractory_period(self, RP_input):
#         # Check if correct datatype was entered
#         try:
#             RP_input = int(RP_input)
#
#         except:
#             self.invalid_label_VRP.grid(columnspan=2, column=self.limits["VRP"]["column"],
#                                         row=self.limits["VRP"]["row"])
#             return False
#
#         if 150 <= RP_input <= 500 and RP_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_VRP.grid(columnspan=2, column=self.limits["VRP"]["column"],
#                                         row=self.limits["VRP"]["row"])
#             return False
#
#     def check_max_sensor_rate(self):
#         # Check if correct datatype was entered
#         try:
#             msr_input = int(self.msr.get())
#         except:
#             self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
#                                         row=self.limits["msr"]["row"])
#             return False
#
#         # Check which range the lrl input falls in
#         if 50 <= msr_input <= 175 and msr_input % 5 == 0:
#             return True
#         else:
#             self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
#                                         row=self.limits["msr"]["row"])
#             return False
#
#     def check_favd(self):
#         # Check if correct datatype was entered
#         try:
#             favd_input = int(self.favd.get())
#         except:
#             self.invalid_label_favd.grid(columnspan=2, column=self.limits["favd"]["column"],
#                                         row=self.limits["favd"]["row"])
#             return False
#
#         # Check which range the lrl input falls in
#         if 70 <= favd_input <= 300 and favd_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_favd.grid(columnspan=2, column=self.limits["favd"]["column"],
#                                         row=self.limits["favd"]["row"])
#             return False
#
#     def check_asen(self):
#         # Check if correct datatype was entered
#         try:
#             sens_input = float(self.asen.get())
#         except:
#             self.invalid_label_asen.grid(columnspan=2, column=self.limits["asen"]["column"], row=self.limits["asen"]["row"])
#             return False
#
#         if 0.0 <= sens_input <= 5.0 and round(sens_input, 1) == sens_input:
#             return True
#         else:
#             self.invalid_label_asen.grid(columnspan=2, column=self.limits["asen"]["column"], row=self.limits["asen"]["row"])
#             return False
#
#     def check_vsen(self):
#         # Check if correct datatype was entered
#         try:
#             sens_input = float(self.vsen.get())
#         except:
#             self.invalid_label_vsen.grid(columnspan=2, column=self.limits["vsen"]["column"], row=self.limits["vsen"]["row"])
#             return False
#
#         if 0.0 <= sens_input <= 5.0 and round(sens_input, 1) == sens_input:
#             return True
#         else:
#             self.invalid_label_vsen.grid(columnspan=2, column=self.limits["vsen"]["column"], row=self.limits["vsen"]["row"])
#             return False
#
#     def check_PVARP(self):
#         # Check if correct datatype was entered
#         try:
#             RP_input = int(self.PVARP.get())
#         except:
#             self.invalid_label_PVARP.grid(columnspan=2, column=self.limits["PVARP"]["column"],
#                                         row=self.limits["PVARP"]["row"])
#             return False
#
#         if 150 <= RP_input <= 500 and RP_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_PVARP.grid(columnspan=2, column=self.limits["PVARP"]["column"],
#                                         row=self.limits["PVARP"]["row"])
#             return False
#
#     def check_hys(self):
#         # Check if correct datatype was entered
#         try:
#             hys_input = int(self.hys.get())
#         except:
#             self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
#                                         row=self.limits["hys"]["row"])
#             return False
#
#         # Check if hys is turned off
#         if hys_input == 0:
#             return True
#
#         # Check which range the lrl input falls in
#         if 30 <= hys_input <= 50 and hys_input % 5 == 0:
#             return True
#         elif 50 <= hys_input <= 90:
#             return True
#         elif 90 <= hys_input <= 175 and hys_input % 5 == 0:
#             return True
#         elif hys_input < 30 or hys_input > 175:
#             self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
#                                         row=self.limits["hys"]["row"])
#             return False
#         else:
#             self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
#                                         row=self.limits["hys"]["row"])
#             return False
#
#     def check_rs(self):
#
#         try:
#             rs_input = int(self.rs.get())
#         except:
#             self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
#                                         row=self.limits["rs"]["row"])
#             return False
#
#         valid_inputs = [0, 3, 6, 9, 12, 15, 18, 21, 25]
#
#         if rs_input in valid_inputs:
#             return True
#         else:
#             self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
#                                         row=self.limits["rs"]["row"])
#             return False
#
#     def check_at(self):
#         try:
#             at_input = int(self.at.get())
#         except:
#             self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
#                                         row=self.limits["at"]["row"])
#             return False
#
#         if 0 <= at_input <= 6:
#             return True
#         else:
#             self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
#                                         row=self.limits["at"]["row"])
#             return False
#
#     def check_rct(self):
#         try:
#             rct_input = int(self.rct.get())
#         except:
#             self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
#                                         row=self.limits["rct"]["row"])
#             return False
#
#         if 10 <= rct_input <= 50 and rct_input % 10 == 0:
#             return True
#         else:
#             self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
#                                         row=self.limits["rct"]["row"])
#             return False
#
#     def check_rf(self):
#
#         try:
#             rf_input = int(self.rf.get())
#         except:
#             self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
#                                         row=self.limits["rf"]["row"])
#             return False
#
#         if 1 <= rf_input <= 16:
#             return True
#         else:
#             self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
#                                         row=self.limits["rf"]["row"])
#             return False
#
#     def check_rvt(self):
#
#         try:
#             rvt_input = int(self.rvt.get())
#         except:
#             self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
#                                         row=self.limits["rvt"]["row"])
#             return False
#
#         if 2 <= rvt_input <= 16:
#             return True
#         else:
#             self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
#                                         row=self.limits["rvt"]["row"])
#             return False
#
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
#         self.invalid_label_msr.grid_remove()
#         self.invalid_label_favd.grid_remove()
#         self.invalid_label_asen.grid_remove()
#         self.invalid_label_vsen.grid_remove()
#         self.invalid_label_PVARP.grid_remove()
#         self.invalid_label_hys.grid_remove()
#         self.invalid_label_rs.grid_remove()
#         self.invalid_label_at.grid_remove()
#         self.invalid_label_rct.grid_remove()
#         self.invalid_label_rf.grid_remove()
#         self.invalid_label_rvt.grid_remove()
#
#         input_params = {
#             "lrl": self.lrl.get(),
#             "url": self.url.get(),
#             "aa": self.aa.get(),
#             "apw": self.apw.get(),
#             "va": self.va.get(),
#             "vpw": self.vpw.get(),
#             "VRP": self.VRP.get(),
#             "ARP": self.ARP.get(),
#             "msr": self.msr.get(),
#             "favd": self.favd.get(),
#             "asen": self.asen.get(),
#             "vsen": self.vsen.get(),
#             "PVARP": self.PVARP.get(),
#             "hys": self.hys.get(),
#             "rs": self.rs.get(),
#             "at": self.at.get(),
#             "rct": self.rct.get(),
#             "rf": self.rf.get(),
#             "rvt": self.rvt.get(),
#         }
#
#         # Checking if any entries are empty
#         for param in input_params.keys():
#             if input_params[param] == "":
#                 self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
#                 return
#
#         valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
#                         self.check_atrial_amplitude(self.aa.get()),
#                         self.check_ventricle_amplitude(self.va.get()),
#                         self.check_apw(self.apw.get()), self.check_vpw(self.vpw.get()),
#                         self.check_atrial_refractory_period(self.ARP.get()),
#                         self.check_ventricle_refractory_period(self.VRP.get())]
#
#         # Checking lrl separately due to increment differences
#
#         if False not in valid_params:
#             self.save_parameters(input_params)
#
#      def save_parameters(self, inputs):
#         if self.user not in self.DB.keys():
#             self.DB[self.user] = {}
#         self.DB[self.user]["AOO"] = inputs
#         print(self.DB)
#         with open("database/parameters.json", "w") as destination:
#             json.dump(self.DB, destination)
#         self.window.destroy()
#---------------------------------------------AOO-----------------------------------------------
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

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= self.lrl.get():
            self.invalid_label_url.grid(columnspan=2, column=self.limits["url"]["column"],
                                        row=self.limits["url"]["row"])
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

        if 1 <= pw_input <= 30:
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
        self.blank_label.place_forget()

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

# # ----------------------------------------------AAI-----------------------------------------------
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
            },
            "PVARP": {
                "column": 6,
                "row": 3
            },
            "asen": {
                "column": 2,
                "row": 5
            },
            "hys": {
                "column": 6,
                "row": 4
            },
            "rs": {
                "column": 2,
                "row": 4
            },

        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        # self.root.destroy()

        # self.window = tk.Tk()
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=8, rowspan=10)

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
        self.PVARP = tk.Entry(self.window)
        self.PVARP.grid(column=5, row=3)
        self.rs = tk.Entry(self.window)
        self.rs.grid(column=1, row=4)
        self.hys = tk.Entry(self.window)
        self.hys.grid(column=5, row=4)
        self.asen = tk.Entry(self.window)
        self.asen.grid(column=1, row=5)

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
        self.PVARP_label = tk.Label(self.window, text="PVARP", font=("Raleway", 12))
        self.PVARP_label.grid(column=4, row=3)
        self.asen_label = tk.Label(self.window, text="Atrial Sensitivity", font=("Raleway", 12))
        self.asen_label.grid(column=0, row=5)
        self.rs_label = tk.Label(self.window, text="Rate Smoothing", font=("Raleway", 12))
        self.rs_label.grid(column=0, row=4)
        self.hys_label = tk.Label(self.window, text="Hysteresis", font=("Raleway", 12))
        self.hys_label.grid(column=4, row=4)

        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_ARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_PVARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_rs = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_asen = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
        self.invalid_label_hys = tk.Label(self.window, text="Invalid", font=("Raleway", 12), width=6, height=1)
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
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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

        if 1 <= pw_input <= 30:
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

    def check_PVARP(self):
        # Check if correct datatype was entered
        try:
            RP_input = int(self.PVARP.get())
        except:
            self.invalid_label_PVARP.grid(columnspan=2, column=self.limits["PVARP"]["column"],
                                        row=self.limits["PVARP"]["row"])
            return False

        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label_PVARP.grid(columnspan=2, column=self.limits["PVARP"]["column"],
                                        row=self.limits["PVARP"]["row"])
            return False

    def check_hys(self):
        # Check if correct datatype was entered
        try:
            hys_input = int(self.hys.get())
        except:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

        # Check if hys is turned off
        if hys_input == 0:
            return True

        # Check which range the hys input falls in
        if 30 <= hys_input <= 50 and hys_input % 5 == 0:
            return True
        elif 50 <= hys_input <= 90:
            return True
        elif 90 <= hys_input <= 175 and hys_input % 5 == 0:
            return True
        elif hys_input < 30 or hys_input > 175:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False
        else:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

    def check_rs(self):

        try:
            rs_input = int(self.rs.get())
        except:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

        valid_inputs = [0, 3, 6, 9, 12, 15, 18, 21, 25]

        if rs_input in valid_inputs:
            return True
        else:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

    def check_asen(self):
        # Check if correct datatype was entered
        try:
            sens_input = float(self.asen.get())
        except:
            self.invalid_label_asen.grid(columnspan=2, column=self.limits["asen"]["column"], row=self.limits["asen"]["row"])
            return False

        if 0.0 <= sens_input <= 5.0 and round(sens_input, 1) == sens_input:
            return True
        else:
            self.invalid_label_asen.grid(columnspan=2, column=self.limits["asen"]["column"], row=self.limits["asen"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.invalid_label_ARP.grid_remove()
        self.invalid_label_PVARP.grid_remove()
        self.invalid_label_asen.grid_remove()
        self.invalid_label_rs.grid_remove()
        self.invalid_label_hys.grid_remove()
        self.blank_label.place_forget()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "ARP": self.ARP.get(),
            "PVARP": self.PVARP.get(),
            "asen": self.asen.get(),
            "rs": self.rs.get(),
            "hys": self.hys.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()), self.check_atrial_amplitude(self.aa.get()),
                        self.check_apw(self.apw.get()), self.check_atrial_refractory_period(self.ARP.get()), self.check_PVARP(),
                        self.check_hys(), self.check_rs(), self.check_asen()]

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

# # ----------------------------------------------VOO-----------------------------------------------
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

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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

        if 1 <= pw_input <= 30:
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
        self.blank_label.place_forget()

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

# # ----------------------------------------------VVI-----------------------------------------------
class VVI:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize invalid parameter labels' placements on grid
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
            "rs": {
                "column": 2,
                "row": 4
            },
            "vpw": {
                "column": 6,
                "row": 1
            },
            "VRP": {
                "column": 6,
                "row": 2
            },

            "vsen": {
                "column": 6,
                "row": 3
            },

            "hys": {
                "column": 6,
                "row": 4
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)

        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=9, rowspan=10)

        self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18), width=20, height=1)
        self.title_label.grid(column=0, row=0)

        # Initialize all Entry fields
        self.lrl = tk.Entry(self.window)
        self.lrl.grid(column=1, row=1)
        self.url = tk.Entry(self.window)
        self.url.grid(column=1, row=2)
        self.va = tk.Entry(self.window)
        self.va.grid(column=1, row=3)
        self.rs = tk.Entry(self.window)
        self.rs.grid(column=1, row=4)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=1)
        self.VRP = tk.Entry(self.window)
        self.VRP.grid(column=5, row=2)
        self.vsen = tk.Entry(self.window)
        self.vsen.grid(column=5, row=3)
        self.hys = tk.Entry(self.window)
        self.hys.grid(column=5, row=4)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12), width=20, height=1)
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12), width=20, height=1)
        self.url_label.grid(column=0, row=2)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12), width=20, height=1)
        self.va_label.grid(column=0, row=3)
        self.rs_label = tk.Label(self.window, text="Rate Smoothing", font=("Raleway", 12), width=20, height=1)
        self.rs_label.grid(column=0, row=4)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12), width=20, height=1)
        self.vpw_label.grid(column=4, row=1)
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12), width=20, height=1)
        self.VRP_label.grid(column=4, row=2)
        self.vsen_label = tk.Label(self.window, text="Ventricular Sensitivity", font=("Raleway", 12), width=20, height=1)
        self.vsen_label.grid(column=4, row=3)
        self.hys_label = tk.Label(self.window, text="Hysteresis", font=("Raleway", 12), width=20, height=1)
        self.hys_label.grid(column=4, row=4)

        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_url = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_va = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_vpw = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_VRP = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_vsen = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_hys = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
        self.invalid_label_rs = tk.Label(self.window, text="  Invalid", font=("Raleway", 10), width=6, height=1)
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

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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

        if 1 <= pw_input <= 30:
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

    def check_vsen(self):
    # Check if correct datatype was entered
            try:
                sens_input = float(self.vsen.get())
            except:
                self.invalid_label_vsen.grid(columnspan=2, column=self.limits["vsen"]["column"], row=self.limits["vsen"]["row"])
                return False

            if 0.0 <= sens_input <= 5.0 and round(sens_input, 1) == sens_input:
                return True
            else:
                self.invalid_label_vsen.grid(columnspan=2, column=self.limits["vsen"]["column"], row=self.limits["vsen"]["row"])
                return False

    def check_hys(self):
        # Check if correct datatype was entered
        try:
            hys_input = int(self.hys.get())
        except:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

        # Check if hys is turned off
        if hys_input == 0:
            return True

        # Check which range the hys input falls in
        if 30 <= hys_input <= 50 and hys_input % 5 == 0:
            return True
        elif 50 <= hys_input <= 90:
            return True
        elif 90 <= hys_input <= 175 and hys_input % 5 == 0:
            return True
        elif hys_input < 30 or hys_input > 175:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False
        else:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

    def check_rs(self):

        try:
            rs_input = int(self.rs.get())
        except:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

        valid_inputs = [0, 3, 6, 9, 12, 15, 18, 21, 25]

        if rs_input in valid_inputs:
            return True
        else:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.invalid_label_VRP.grid_remove()
        self.invalid_label_vsen.grid_remove()
        self.invalid_label_rs.grid_remove()
        self.invalid_label_hys.grid_remove()
        self.blank_label.place_forget()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "VRP": self.VRP.get(),
            "vsen": self.vsen.get(),
            "hys": self.hys.get(),
            "rs": self.rs.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_ventricle_amplitude(self.va.get()), self.check_vpw(self.vpw.get()),
                        self.check_ventricle_refractory_period(self.VRP.get()), self.check_rs(), self.check_hys(), self.check_vsen()]

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

# ----------------------------------------------DOO-----------------------------------------------
class DOO:
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
                "column": 2,
                "row": 4
            },
            "va": {
                "column": 6,
                "row": 1
            },
            "vpw": {
                "column": 6,
                "row": 2
            },
            "favd": {
                "column": 6,
                "row": 3
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)

        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
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
        self.apw.grid(column=1, row=4)
        self.va = tk.Entry(self.window)
        self.va.grid(column=5, row=1)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=2)
        self.favd = tk.Entry(self.window)
        self.favd.grid(column=5, row=3)


        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=0, row=3)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=0, row=4)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=1)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=2)
        self.favd_label = tk.Label(self.window, text="Fixed AV Delay", font=("Raleway", 12))
        self.favd_label.grid(column=4, row=3)



        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_va = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_vpw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_favd = tk.Label(self.window, text="Invalid", font=("Raleway", 12))


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

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

        if 1 <= pw_input <= 30:
            return True
        else:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

    def check_atrial_refractory_period(self, RP_input):
        # Check if correct datatype was entered
        try:
            RP_input = int(RP_input)
        except:
            self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"],
                                        row=self.limits["ARP"]["row"])
            return False

        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"],
                                        row=self.limits["ARP"]["row"])
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

        if 1 <= pw_input <= 30:
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

    def check_favd(self):
        # Check if correct datatype was entered
        try:
            favd_input = int(self.favd.get())
        except:
            self.invalid_label_favd.grid(columnspan=2, column=self.limits["favd"]["column"],
                                        row=self.limits["favd"]["row"])
            return False

        # Check which range the lrl input falls in
        if 70 <= favd_input <= 300 and favd_input % 10 == 0:
            return True
        else:
            self.invalid_label_favd.grid(columnspan=2, column=self.limits["favd"]["column"],
                                        row=self.limits["favd"]["row"])
            return False


    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.invalid_label_favd.grid_remove()


        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "favd": self.favd.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()),
                        self.check_ventricle_amplitude(self.va.get()),
                        self.check_apw(self.apw.get()), self.check_vpw(self.vpw.get()), self.check_favd()]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["DOO"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
# # ----------------------------------------------AOOR----------------------------------------------
class AOOR:
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
                "column": 2,
                "row": 4
            },
            "msr": {
                "column": 2,
                "row": 5
            },
            "at": {
                "column": 6,
                "row": 1
            },
            "rct": {
                "column": 6,
                "row": 2
            },
            "rf": {
                "column": 6,
                "row": 3
            },
            "rvt": {
                "column": 6,
                "row": 4
            }
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=8, rowspan=10)

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
        self.apw.grid(column=1, row=4)
        self.msr = tk.Entry(self.window)
        self.msr.grid(column=1, row=5)
        self.at = tk.Entry(self.window)
        self.at.grid(column=5, row=1)
        self.rct = tk.Entry(self.window)
        self.rct.grid(column=5, row=2)
        self.rf = tk.Entry(self.window)
        self.rf.grid(column=5, row=3)
        self.rvt = tk.Entry(self.window)
        self.rvt.grid(column=5,row=4)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=0, row=3)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=0, row=4)
        self.msr_label = tk.Label(self.window, text="Maximum Sensor Rate", font=("Raleway", 12))
        self.msr_label.grid(column=0, row=5)
        self.at_label = tk.Label(self.window, text="Activity Threshold", font=("Raleway", 12))
        self.at_label.grid(column=4, row=1)
        self.rct_label = tk.Label(self.window, text="Reaction Time", font=("Raleway", 12))
        self.rct_label.grid(column=4, row=2)
        self.rf_label = tk.Label(self.window, text="Response Factor", font=("Raleway", 12))
        self.rf_label.grid(column=4, row=3)
        self.rvt_label = tk.Label(self.window, text="Recovery Time", font=("Raleway", 12))
        self.rvt_label.grid(column=4, row=4)



        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_msr = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_at = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rct = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rf = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rvt = tk.Label(self.window, text="Invalid", font=("Raleway", 12))

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

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

        if 1 <= pw_input <= 30:
            return True
        else:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

    def check_max_sensor_rate(self):
        # Check if correct datatype was entered
        try:
            msr_input = int(self.msr.get())
        except:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= msr_input <= 175 and msr_input % 5 == 0:
            return True
        else:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

    def check_at(self):
        try:
            at_input = int(self.at.get())
        except:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

        if 0 <= at_input <= 6:
            return True
        else:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

    def check_rct(self):
        try:
            rct_input = int(self.rct.get())
        except:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

        if 10 <= rct_input <= 50 and rct_input % 10 == 0:
            return True
        else:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

    def check_rf(self):

        try:
            rf_input = int(self.rf.get())
        except:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

        if 1 <= rf_input <= 16:
            return True
        else:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

    def check_rvt(self):

        try:
            rvt_input = int(self.rvt.get())
        except:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

        if 2 <= rvt_input <= 16:
            return True
        else:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.invalid_label_msr.grid_remove()
        self.invalid_label_at.grid_remove()
        self.invalid_label_rct.grid_remove()
        self.invalid_label_rf.grid_remove()
        self.invalid_label_rvt.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "msr": self.msr.get(),
            "at": self.at.get(),
            "rct": self.rct.get(),
            "rf": self.rf.get(),
            "rvt": self.rvt.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()),
                        self.check_apw(self.apw.get()), self.check_max_sensor_rate(), self.check_at(), self.check_rct(), self.check_rf(),
                        self.check_rvt()]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["AOOR"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
# # ----------------------------------------------AAIR----------------------------------------------
class AAIR:
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
                "column": 2,
                "row": 4
            },
            "ARP": {
                "column": 2,
                "row": 5
            },
            "msr": {
                "column": 2,
                "row": 6
            },
            "asen": {
                "column": 2,
                "row": 7
            },
            "PVARP": {
                "column": 6,
                "row": 1
            },
            "hys": {
                "column": 6,
                "row": 2
            },
            "rs": {
                "column": 6,
                "row": 3
            },
            "at": {
                "column": 6,
                "row": 4
            },
            "rct": {
                "column": 6,
                "row": 5
            },
            "rf": {
                "column": 6,
                "row": 6
            },
            "rvt": {
                "column": 6,
                "row": 7
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=8, rowspan=10)

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
        self.apw.grid(column=1, row=4)
        self.ARP = tk.Entry(self.window)
        self.ARP.grid(column=1, row=5)
        self.msr = tk.Entry(self.window)
        self.msr.grid(column=1, row=6)
        self.asen = tk.Entry(self.window)
        self.asen.grid(column=1, row=7)
        self.PVARP = tk.Entry(self.window)
        self.PVARP.grid(column=5, row=1)
        self.hys = tk.Entry(self.window)
        self.hys.grid(column=5, row=2)
        self.rs = tk.Entry(self.window)
        self.rs.grid(column=5, row=3)
        self.at = tk.Entry(self.window)
        self.at.grid(column=5, row=4)
        self.rct = tk.Entry(self.window)
        self.rct.grid(column=5, row=5)
        self.rf = tk.Entry(self.window)
        self.rf.grid(column=5, row=6)
        self.rvt = tk.Entry(self.window)
        self.rvt.grid(column=5,row=7)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=0, row=3)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=0, row=4)
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
        self.ARP_label.grid(column=0, row=5)
        self.msr_label = tk.Label(self.window, text="Maximum Sensor Rate", font=("Raleway", 12))
        self.msr_label.grid(column=0, row=6)
        self.asen_label = tk.Label(self.window, text="Atrial Sensitivity", font=("Raleway", 12))
        self.asen_label.grid(column=0, row=7)
        self.PVARP_label = tk.Label(self.window, text="PVARP", font=("Raleway", 12))
        self.PVARP_label.grid(column=4, row=1)
        self.hys_label = tk.Label(self.window, text="Hysteresis", font=("Raleway", 12))
        self.hys_label.grid(column=4, row=2)
        self.rs_label = tk.Label(self.window, text="Rate Smoothing", font=("Raleway", 12))
        self.rs_label.grid(column=4, row=3)
        self.at_label = tk.Label(self.window, text="Activity Threshold", font=("Raleway", 12))
        self.at_label.grid(column=4, row=4)
        self.rct_label = tk.Label(self.window, text="Reaction Time", font=("Raleway", 12))
        self.rct_label.grid(column=4, row=5)
        self.rf_label = tk.Label(self.window, text="Response Factor", font=("Raleway", 12))
        self.rf_label.grid(column=4, row=6)
        self.rvt_label = tk.Label(self.window, text="Recovery Time", font=("Raleway", 12))
        self.rvt_label.grid(column=4, row=7)



        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_ARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_msr = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_asen = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_PVARP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_hys = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rs = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_at = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rct = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rf = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rvt = tk.Label(self.window, text="Invalid", font=("Raleway", 12))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.90, anchor="center")



    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

        if 1 <= pw_input <= 30:
            return True
        else:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

    def check_atrial_refractory_period(self, RP_input):
        # Check if correct datatype was entered
        try:
            RP_input = int(RP_input)
        except:
            self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"],
                                        row=self.limits["ARP"]["row"])
            return False

        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label_ARP.grid(columnspan=2, column=self.limits["ARP"]["column"],
                                        row=self.limits["ARP"]["row"])
            return False

    def check_max_sensor_rate(self):
        # Check if correct datatype was entered
        try:
            msr_input = int(self.msr.get())
        except:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= msr_input <= 175 and msr_input % 5 == 0:
            return True
        else:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

    def check_asen(self):
        # Check if correct datatype was entered
        try:
            sens_input = float(self.asen.get())
        except:
            self.invalid_label_asen.grid(columnspan=2, column=self.limits["asen"]["column"], row=self.limits["asen"]["row"])
            return False

        if 0.0 <= sens_input <= 5.0 and round(sens_input, 1) == sens_input:
            return True
        else:
            self.invalid_label_asen.grid(columnspan=2, column=self.limits["asen"]["column"], row=self.limits["asen"]["row"])
            return False

    def check_PVARP(self):
        # Check if correct datatype was entered
        try:
            RP_input = int(self.PVARP.get())
        except:
            self.invalid_label_PVARP.grid(columnspan=2, column=self.limits["PVARP"]["column"],
                                        row=self.limits["PVARP"]["row"])
            return False

        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label_PVARP.grid(columnspan=2, column=self.limits["PVARP"]["column"],
                                        row=self.limits["PVARP"]["row"])
            return False

    def check_hys(self):
        # Check if correct datatype was entered
        try:
            hys_input = int(self.hys.get())
        except:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

        # Check if hys is turned off
        if hys_input == 0:
            return True

        # Check which range the lrl input falls in
        if 30 <= hys_input <= 50 and hys_input % 5 == 0:
            return True
        elif 50 <= hys_input <= 90:
            return True
        elif 90 <= hys_input <= 175 and hys_input % 5 == 0:
            return True
        elif hys_input < 30 or hys_input > 175:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False
        else:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

    def check_rs(self):

        try:
            rs_input = int(self.rs.get())
        except:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

        valid_inputs = [0, 3, 6, 9, 12, 15, 18, 21, 25]

        if rs_input in valid_inputs:
            return True
        else:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

    def check_at(self):
        try:
            at_input = int(self.at.get())
        except:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

        if 0 <= at_input <= 6:
            return True
        else:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

    def check_rct(self):
        try:
            rct_input = int(self.rct.get())
        except:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

        if 10 <= rct_input <= 50 and rct_input % 10 == 0:
            return True
        else:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

    def check_rf(self):

        try:
            rf_input = int(self.rf.get())
        except:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

        if 1 <= rf_input <= 16:
            return True
        else:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

    def check_rvt(self):

        try:
            rvt_input = int(self.rvt.get())
        except:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

        if 2 <= rvt_input <= 16:
            return True
        else:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.invalid_label_ARP.grid_remove()
        self.invalid_label_msr.grid_remove()
        self.invalid_label_asen.grid_remove()
        self.invalid_label_PVARP.grid_remove()
        self.invalid_label_hys.grid_remove()
        self.invalid_label_rs.grid_remove()
        self.invalid_label_at.grid_remove()
        self.invalid_label_rct.grid_remove()
        self.invalid_label_rf.grid_remove()
        self.invalid_label_rvt.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "ARP": self.ARP.get(),
            "msr": self.msr.get(),
            "asen": self.asen.get(),
            "PVARP": self.PVARP.get(),
            "hys": self.hys.get(),
            "rs": self.rs.get(),
            "at": self.at.get(),
            "rct": self.rct.get(),
            "rf": self.rf.get(),
            "rvt": self.rvt.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()),
                        self.check_apw(self.apw.get()),
                        self.check_atrial_refractory_period(self.ARP.get()), self.check_max_sensor_rate(), self.check_asen(),
                        self.check_PVARP(), self.check_hys(), self.check_rs(), self.check_at(), self.check_rct(), self.check_rf(),
                        self.check_rvt()]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["AAIR"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
# # ----------------------------------------------VOOR----------------------------------------------
class VOOR:
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
            "msr": {
                "column": 2,
                "row": 3
            },
            "at": {
                "column": 2,
                "row": 4
            },
            "va": {
                "column": 6,
                "row": 1
            },
            "vpw": {
                "column": 6,
                "row": 2
            },
            "rct": {
                "column": 6,
                "row": 3
            },
            "rf": {
                "column": 6,
                "row": 4
            },
            "rvt": {
                "column": 2,
                "row": 5
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)

        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=8, rowspan=10)

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
        self.msr = tk.Entry(self.window)
        self.msr.grid(column=1, row=3)
        self.at = tk.Entry(self.window)
        self.at.grid(column=1, row=4)
        self.rct = tk.Entry(self.window)
        self.rct.grid(column=5, row=3)
        self.rf = tk.Entry(self.window)
        self.rf.grid(column=5, row=4)
        self.rvt = tk.Entry(self.window)
        self.rvt.grid(column=1,row=5)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=1)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=2)
        self.msr_label = tk.Label(self.window, text="Maximum Sensor Rate", font=("Raleway", 12))
        self.msr_label.grid(column=0, row=3)
        self.at_label = tk.Label(self.window, text="Activity Threshold", font=("Raleway", 12))
        self.at_label.grid(column=0, row=4)
        self.rct_label = tk.Label(self.window, text="Reaction Time", font=("Raleway", 12))
        self.rct_label.grid(column=4, row=3)
        self.rf_label = tk.Label(self.window, text="Response Factor", font=("Raleway", 12))
        self.rf_label.grid(column=4, row=4)
        self.rvt_label = tk.Label(self.window, text="Recovery Time", font=("Raleway", 12))
        self.rvt_label.grid(column=0, row=5)



        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_va = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_vpw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_msr = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_at = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rct = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rf = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rvt = tk.Label(self.window, text="Invalid", font=("Raleway", 12))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.90, anchor="center")



    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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

        if 1 <= pw_input <= 30:
            return True
        else:
            self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
                                        row=self.limits["vpw"]["row"])
            return False

    def check_max_sensor_rate(self):
        # Check if correct datatype was entered
        try:
            msr_input = int(self.msr.get())
        except:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= msr_input <= 175 and msr_input % 5 == 0:
            return True
        else:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

    def check_at(self):
        try:
            at_input = int(self.at.get())
        except:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

        if 0 <= at_input <= 6:
            return True
        else:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

    def check_rct(self):
        try:
            rct_input = int(self.rct.get())
        except:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

        if 10 <= rct_input <= 50 and rct_input % 10 == 0:
            return True
        else:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

    def check_rf(self):

        try:
            rf_input = int(self.rf.get())
        except:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

        if 1 <= rf_input <= 16:
            return True
        else:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

    def check_rvt(self):

        try:
            rvt_input = int(self.rvt.get())
        except:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

        if 2 <= rvt_input <= 16:
            return True
        else:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.invalid_label_msr.grid_remove()
        self.invalid_label_at.grid_remove()
        self.invalid_label_rct.grid_remove()
        self.invalid_label_rf.grid_remove()
        self.invalid_label_rvt.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "msr": self.msr.get(),
            "at": self.at.get(),
            "rct": self.rct.get(),
            "rf": self.rf.get(),
            "rvt": self.rvt.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_ventricle_amplitude(self.va.get()),
                        self.check_vpw(self.vpw.get()),
                        self.check_max_sensor_rate(),
                        self.check_at(), self.check_rct(), self.check_rf(), self.check_rvt()]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["VOOR"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
# # ----------------------------------------------VVIR----------------------------------------------
class VVIR:
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
            "msr": {
                "column": 2,
                "row": 3
            },
            "vsen": {
                "column": 2,
                "row": 4
            },
            "va": {
                "column": 6,
                "row": 1
            },
            "vpw": {
                "column": 6,
                "row": 2
            },
            "VRP": {
                "column": 6,
                "row": 3
            },
            "hys": {
                "column": 6,
                "row": 4
            },
            "rs": {
                "column": 2,
                "row": 5
            },
            "at": {
                "column": 6,
                "row": 5
            },
            "rct": {
                "column": 2,
                "row": 6
            },
            "rf": {
                "column": 6,
                "row": 6
            },
            "rvt": {
                "column": 2,
                "row": 7
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)

        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=8, rowspan=10)

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
        self.VRP = tk.Entry(self.window)
        self.VRP.grid(column=5, row=3)
        self.msr = tk.Entry(self.window)
        self.msr.grid(column=1, row=3)
        self.vsen = tk.Entry(self.window)
        self.vsen.grid(column=1, row=4)
        self.hys = tk.Entry(self.window)
        self.hys.grid(column=5, row=4)
        self.rs = tk.Entry(self.window)
        self.rs.grid(column=1, row=5)
        self.at = tk.Entry(self.window)
        self.at.grid(column=5, row=5)
        self.rct = tk.Entry(self.window)
        self.rct.grid(column=1, row=6)
        self.rf = tk.Entry(self.window)
        self.rf.grid(column=5, row=6)
        self.rvt = tk.Entry(self.window)
        self.rvt.grid(column=1,row=7)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=1)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=2)
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
        self.VRP_label.grid(column=4, row=3)
        self.msr_label = tk.Label(self.window, text="Maximum Sensor Rate", font=("Raleway", 12))
        self.msr_label.grid(column=0, row=3)
        self.vsen_label = tk.Label(self.window, text="Ventricular Sensitivity", font=("Raleway", 12))
        self.vsen_label.grid(column=0, row=4)
        self.hys_label = tk.Label(self.window, text="Hysteresis", font=("Raleway", 12))
        self.hys_label.grid(column=4, row=4)
        self.rs_label = tk.Label(self.window, text="Rate Smoothing", font=("Raleway", 12))
        self.rs_label.grid(column=0, row=5)
        self.at_label = tk.Label(self.window, text="Activity Threshold", font=("Raleway", 12))
        self.at_label.grid(column=4, row=5)
        self.rct_label = tk.Label(self.window, text="Reaction Time", font=("Raleway", 12))
        self.rct_label.grid(column=0, row=6)
        self.rf_label = tk.Label(self.window, text="Response Factor", font=("Raleway", 12))
        self.rf_label.grid(column=4, row=6)
        self.rvt_label = tk.Label(self.window, text="Recovery Time", font=("Raleway", 12))
        self.rvt_label.grid(column=0, row=7)



        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_va = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_vpw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_VRP = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_msr = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_vsen = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_hys = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rs = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_at = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rct = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rf = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rvt = tk.Label(self.window, text="Invalid", font=("Raleway", 12))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.90, anchor="center")



    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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

        if 1 <= pw_input <= 30:
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

    def check_max_sensor_rate(self):
        # Check if correct datatype was entered
        try:
            msr_input = int(self.msr.get())
        except:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= msr_input <= 175 and msr_input % 5 == 0:
            return True
        else:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

    def check_vsen(self):
        # Check if correct datatype was entered
        try:
            sens_input = float(self.vsen.get())
        except:
            self.invalid_label_vsen.grid(columnspan=2, column=self.limits["vsen"]["column"], row=self.limits["vsen"]["row"])
            return False

        if 0.0 <= sens_input <= 5.0 and round(sens_input, 1) == sens_input:
            return True
        else:
            self.invalid_label_vsen.grid(columnspan=2, column=self.limits["vsen"]["column"], row=self.limits["vsen"]["row"])
            return False

    def check_hys(self):
        # Check if correct datatype was entered
        try:
            hys_input = int(self.hys.get())
        except:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

        # Check if hys is turned off
        if hys_input == 0:
            return True

        # Check which range the lrl input falls in
        if 30 <= hys_input <= 50 and hys_input % 5 == 0:
            return True
        elif 50 <= hys_input <= 90:
            return True
        elif 90 <= hys_input <= 175 and hys_input % 5 == 0:
            return True
        elif hys_input < 30 or hys_input > 175:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False
        else:
            self.invalid_label_hys.grid(columnspan=2, column=self.limits["hys"]["column"],
                                        row=self.limits["hys"]["row"])
            return False

    def check_rs(self):

        try:
            rs_input = int(self.rs.get())
        except:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

        valid_inputs = [0, 3, 6, 9, 12, 15, 18, 21, 25]

        if rs_input in valid_inputs:
            return True
        else:
            self.invalid_label_rs.grid(columnspan=2, column=self.limits["rs"]["column"],
                                        row=self.limits["rs"]["row"])
            return False

    def check_at(self):
        try:
            at_input = int(self.at.get())
        except:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

        if 0 <= at_input <= 6:
            return True
        else:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

    def check_rct(self):
        try:
            rct_input = int(self.rct.get())
        except:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

        if 10 <= rct_input <= 50 and rct_input % 10 == 0:
            return True
        else:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

    def check_rf(self):

        try:
            rf_input = int(self.rf.get())
        except:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

        if 1 <= rf_input <= 16:
            return True
        else:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

    def check_rvt(self):

        try:
            rvt_input = int(self.rvt.get())
        except:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

        if 2 <= rvt_input <= 16:
            return True
        else:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.invalid_label_VRP.grid_remove()
        self.invalid_label_msr.grid_remove()
        self.invalid_label_vsen.grid_remove()
        self.invalid_label_hys.grid_remove()
        self.invalid_label_rs.grid_remove()
        self.invalid_label_at.grid_remove()
        self.invalid_label_rct.grid_remove()
        self.invalid_label_rf.grid_remove()
        self.invalid_label_rvt.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "VRP": self.VRP.get(),
            "msr": self.msr.get(),
            "vsen": self.vsen.get(),
            "hys": self.hys.get(),
            "rs": self.rs.get(),
            "at": self.at.get(),
            "rct": self.rct.get(),
            "rf": self.rf.get(),
            "rvt": self.rvt.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_ventricle_amplitude(self.va.get()),
                        self.check_vpw(self.vpw.get()),
                        self.check_ventricle_refractory_period(self.VRP.get()), self.check_max_sensor_rate(), self.check_vsen(), self.check_hys(),
                        self.check_rs(), self.check_at(), self.check_rct(), self.check_rf(), self.check_rvt()]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["VVIR"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
# ---------------------------------------------DOOR-----------------------------------------------
class DOOR:
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
                "column": 2,
                "row": 4
            },
            "va": {
                "column": 6,
                "row": 1
            },
            "vpw": {
                "column": 6,
                "row": 2
            },
            "msr": {
                "column": 6,
                "row": 3
            },
            "favd": {
                "column": 6,
                "row": 4
            },
            "at": {
                "column": 2,
                "row": 5
            },
            "rct": {
                "column": 6,
                "row": 5
            },
            "rf": {
                "column": 2,
                "row": 6
            },
            "rvt": {
                "column": 6,
                "row": 6
            },
        }

        # Build canvas
        self.root = root
        self.window = tk.Toplevel(self.root)

        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=700)
        self.canvas.grid(columnspan=8, rowspan=10)

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
        self.apw.grid(column=1, row=4)
        self.va = tk.Entry(self.window)
        self.va.grid(column=5, row=1)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=2)
        self.msr = tk.Entry(self.window)
        self.msr.grid(column=5, row=3)
        self.favd = tk.Entry(self.window)
        self.favd.grid(column=5, row=4)
        self.at = tk.Entry(self.window)
        self.at.grid(column=1, row=5)
        self.rct = tk.Entry(self.window)
        self.rct.grid(column=5, row=5)
        self.rf = tk.Entry(self.window)
        self.rf.grid(column=1, row=6)
        self.rvt = tk.Entry(self.window)
        self.rvt.grid(column=5,row=6)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=0, row=3)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=0, row=4)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=1)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=2)
        self.msr_label = tk.Label(self.window, text="Maximum Sensor Rate", font=("Raleway", 12))
        self.msr_label.grid(column=4, row=3)
        self.favd_label = tk.Label(self.window, text="Fixed AV Delay", font=("Raleway", 12))
        self.favd_label.grid(column=4, row=4)
        self.at_label = tk.Label(self.window, text="Activity Threshold", font=("Raleway", 12))
        self.at_label.grid(column=0, row=5)
        self.rct_label = tk.Label(self.window, text="Reaction Time", font=("Raleway", 12))
        self.rct_label.grid(column=4, row=5)
        self.rf_label = tk.Label(self.window, text="Response Factor", font=("Raleway", 12))
        self.rf_label.grid(column=0, row=6)
        self.rvt_label = tk.Label(self.window, text="Recovery Time", font=("Raleway", 12))
        self.rvt_label.grid(column=4, row=6)



        # Intialize "invalid" label
        self.invalid_label_lrl = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_url = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_aa = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_apw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_va = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_vpw = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_msr = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_favd = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_at = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rct = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rf = tk.Label(self.window, text="Invalid", font=("Raleway", 12))
        self.invalid_label_rvt = tk.Label(self.window, text="Invalid", font=("Raleway", 12))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                  font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.place(relx=0.5, rely=0.90, anchor="center")



    def check_lrl(self, lrl_input):
        # Check if correct datatype was entered
        try:
            lrl_input = int(lrl_input)
        except:
            self.invalid_label_lrl.grid(columnspan=2, column=self.limits["lrl"]["column"],
                                        row=self.limits["lrl"]["row"])
            return False

        # Compare lrl to url
        if lrl_input >= int(self.url.get()):
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

        # Compare lrl and url
        if url_input <= int(self.lrl.get()):
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
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
            return False

        if 1 <= pw_input <= 30:
            return True
        else:
            self.invalid_label_apw.grid(columnspan=2, column=self.limits["apw"]["column"],
                                        row=self.limits["apw"]["row"])
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

        if 1 <= pw_input <= 30:
            return True
        else:
            self.invalid_label_vpw.grid(columnspan=2, column=self.limits["vpw"]["column"],
                                        row=self.limits["vpw"]["row"])
            return False

    def check_max_sensor_rate(self):
        # Check if correct datatype was entered
        try:
            msr_input = int(self.msr.get())
        except:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

        # Check which range the lrl input falls in
        if 50 <= msr_input <= 175 and msr_input % 5 == 0:
            return True
        else:
            self.invalid_label_msr.grid(columnspan=2, column=self.limits["msr"]["column"],
                                        row=self.limits["msr"]["row"])
            return False

    def check_favd(self):
        # Check if correct datatype was entered
        try:
            favd_input = int(self.favd.get())
        except:
            self.invalid_label_favd.grid(columnspan=2, column=self.limits["favd"]["column"],
                                        row=self.limits["favd"]["row"])
            return False

        # Check which range the lrl input falls in
        if 70 <= favd_input <= 300 and favd_input % 10 == 0:
            return True
        else:
            self.invalid_label_favd.grid(columnspan=2, column=self.limits["favd"]["column"],
                                        row=self.limits["favd"]["row"])
            return False

    def check_at(self):
        try:
            at_input = int(self.at.get())
        except:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

        if 0 <= at_input <= 6:
            return True
        else:
            self.invalid_label_at.grid(columnspan=2, column=self.limits["at"]["column"],
                                        row=self.limits["at"]["row"])
            return False

    def check_rct(self):
        try:
            rct_input = int(self.rct.get())
        except:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

        if 10 <= rct_input <= 50 and rct_input % 10 == 0:
            return True
        else:
            self.invalid_label_rct.grid(columnspan=2, column=self.limits["rct"]["column"],
                                        row=self.limits["rct"]["row"])
            return False

    def check_rf(self):

        try:
            rf_input = int(self.rf.get())
        except:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

        if 1 <= rf_input <= 16:
            return True
        else:
            self.invalid_label_rf.grid(columnspan=2, column=self.limits["rf"]["column"],
                                        row=self.limits["rf"]["row"])
            return False

    def check_rvt(self):

        try:
            rvt_input = int(self.rvt.get())
        except:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

        if 2 <= rvt_input <= 16:
            return True
        else:
            self.invalid_label_rvt.grid(columnspan=2, column=self.limits["rvt"]["column"],
                                        row=self.limits["rvt"]["row"])
            return False

    def check_validity(self):
        # Remove previous invalid labels
        self.invalid_label_lrl.grid_remove()
        self.invalid_label_url.grid_remove()
        self.invalid_label_aa.grid_remove()
        self.invalid_label_apw.grid_remove()
        self.invalid_label_va.grid_remove()
        self.invalid_label_vpw.grid_remove()
        self.invalid_label_msr.grid_remove()
        self.invalid_label_favd.grid_remove()
        self.invalid_label_at.grid_remove()
        self.invalid_label_rct.grid_remove()
        self.invalid_label_rf.grid_remove()
        self.invalid_label_rvt.grid_remove()

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "favd": self.favd.get(),
            "at": self.at.get(),
            "rct": self.rct.get(),
            "rf": self.rf.get(),
            "rvt": self.rvt.get(),
        }

        # Checking if any entries are empty
        for param in input_params.keys():
            if input_params[param] == "":
                self.blank_label.place(relx=0.5, rely=0.75, anchor="center")
                return

        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()),
                        self.check_ventricle_amplitude(self.va.get()),
                        self.check_apw(self.apw.get()), self.check_vpw(self.vpw.get()),
                        self.check_at(), self.check_rct(), self.check_rf(), self.check_rvt(), self.check_favd(), self.check_max_sensor_rate()
                        ]

        # Checking lrl separately due to increment differences

        if False not in valid_params:
            self.save_parameters(input_params)

    def save_parameters(self, inputs):
        if self.user not in self.DB.keys():
            self.DB[self.user] = {}
        self.DB[self.user]["DOOR"] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()