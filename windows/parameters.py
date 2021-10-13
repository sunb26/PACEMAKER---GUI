import tkinter as tk
import json


class parameter_page:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize parameter limits
        self.limits = {
            "lrl": {
                "UL": 0,
                "LL": 0,
                "column": 2,
                "row": 1
            },
            "url": {
                "UL": 0,
                "LL": 0,
                "column": 2,
                "row": 2
            },
            "aa": {
                "UL": 0,
                "LL": 0,
                "column": 2,
                "row": 3
            },
            "apw": {
                "UL": 0,
                "LL": 0,
                "column": 2,
                "row": 4
            },
            "va": {
                "UL": 0,
                "LL": 0,
                "column": 6,
                "row": 1
            },
            "vpw": {
                "UL": 0,
                "LL": 0,
                "column": 6,
                "row": 2
            },
            "VRP": {
                "UL": 0,
                "LL": 0,
                "column": 6,
                "row": 3
            },
            "ARP": {
                "UL": 0,
                "LL": 0,
                "column": 6,
                "row": 4
            }
        }

        # Build canvas
        self.root = root
        #self.window = tk.Toplevel(self.root)
        self.root.destroy()

        self.window = tk.Tk()
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
        self.apw.grid(column=1, row=4)
        self.va = tk.Entry(self.window)
        self.va.grid(column=5, row=1)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=2)
        self.VRP = tk.Entry(self.window)
        self.VRP.grid(column=5, row=3)
        self.ARP = tk.Entry(self.window)
        self.ARP.grid(column=5, row=4)

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
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
        self.VRP_label.grid(column=4, row=3)
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
        self.ARP_label.grid(column=4, row=4)

        # Intialize "invalid" label
        self.invalid_label = tk.Label(self.window, text="Invalid", font=("Raleway", 6))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                    font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.grid(columnspan=4, column=1, row=6)


    def check_validity(self):
        valid = True
        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "VRP": self.VRP.get(),
            "ARP": self.ARP.get()
        }

        for param in input_params.keys():
            if input_params[param] < self.limits[param]["LL"] or input_params[param] > self.limits[param]["UL"]:
                self.invalid_label.grid(column=self.limits["column"], row=self.limites["row"])
                valid = False

        if valid:
            self.save_parameters(input_params)
        else:
            return

    def save_parameters(self, inputs):
        self.DB[self.user] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()
