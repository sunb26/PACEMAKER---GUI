import tkinter as tk
import json


# Import login database
with open("login_data.json") as database:
    login_database = json.load(database)

# Define the start of the Window Object
root = tk.Tk()

# Defines the size of the window
canvas = tk.Canvas(root, width=600, height=300)

# Initializes the canvas. Columnspan creates 3 invisible columns which allows us
# to place objects in our window with extra precision
canvas.grid(columnspan=5, rowspan=10)

# Instructions/Text
instructions = tk.Label(root, text="Login", font=("Raleway", 18))
instructions.grid(column=0, row=0)

def login():
    username = username_entry.get()
    password = password_entry.get()
    login_success = False
    for cred in login_database['credentials']:
        if cred['username'] == username:
            if cred['password'] == password:
                response = tk.Label(root, text="Login Successful")
                response.grid(column=1, row=4)
                return 0

    response = tk.Label(root, text="Login Failed")
    response.grid(column=1, row=4)
    return 0

# Input Box
username_entry = tk.Entry(root)
username_label = tk.Label(root, text="Username:")
username_entry.grid(column=1, row=1)
username_label.grid(column=0, row=1)
password_entry = tk.Entry(root)
password_label = tk.Label(root, text="Password:")
password_entry.grid(column=1, row=2)
password_label.grid(column=0, row=2)


# Button
btn_text = tk.StringVar()
login_btn = tk.Button(root, textvariable=btn_text, command=lambda:login(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
btn_text.set("Login")
login_btn.grid(column=1, row=3)




root.mainloop() # All code after this line will not display in the window object


