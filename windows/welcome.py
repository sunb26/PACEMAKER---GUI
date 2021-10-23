import tkinter as tk
from windows.register import register_window
from windows.home import home_page
from windows.parameters import *
from PIL import Image, ImageTk



def welcome_page(root, login_database, parameter_database):
    root.title("Welcome Page")

    # Defines the size of the window
    canvas = tk.Canvas(root, width=600, height=500)

    # Initializes the canvas. Columnspan creates 3 invisible columns which allows us
    # to place objects in our window with extra precision
    canvas.grid(columnspan=5, rowspan=10)

    # Instructions/Text
    instructions = tk.Label(root, text="Login", font=("Raleway", 18))
    instructions.grid(column=0, row=1)

    login_response = tk.Label(root)

    # Function for button click. Checks database for login credentials and outputs
    # success or failure if login is correct or not
    def login():

        username = username_entry.get()
        password = password_entry.get()

        for cred in login_database['credentials']:
            if cred['username'] == username:
                if cred['password'] == password:
                    # login_response["text"] = "Login Successful"
                    # login_response.grid(column=1, row=4)
                    home_page(root, username, parameter_database)
                    return

        login_response["text"] = "Login Failed"
        login_response.grid(column=1, row=5)
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        return

    # Username and Password Input Box
    username_entry = tk.Entry(root)
    username_label = tk.Label(root, text="Username:")
    username_entry.grid(column=1, row=2)
    username_label.grid(column=0, row=2)

    password_entry = tk.Entry(root, show="*")
    password_label = tk.Label(root, text="Password:")
    password_entry.grid(column=1, row=3)
    password_label.grid(column=0, row=3)

    # Login Button
    login_btn_text = tk.StringVar()
    login_btn = tk.Button(root, textvariable=login_btn_text, command=lambda: login(), font="Raleway", bg="#20bebe",
                          fg="white", height=2, width=15)
    login_btn_text.set("Login")
    login_btn.grid(column=1, row=4)

    # -------------------Registration feature-------------------------

    # Sign-up Button
    register_btn_text = tk.StringVar()
    register_btn = tk.Button(root, textvariable=register_btn_text,
                             command=lambda: register_window(root, login_database), font="Raleway",
                             bg="#20bebe", fg="white", height=2, width=15)
    register_btn_text.set("Sign-up")
    register_btn.grid(column=2, row=4)

    if len(login_database["credentials"]) >= 10:
        register_btn.destroy()

    # Logo
    logo = Image.open('utils/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(columnspan=2, column=1, row=0)