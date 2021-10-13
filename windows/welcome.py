import tkinter as tk
from windows.register import register_window
from windows.parameters import parameter_page

def welcome_page(root, login_database, parameter_database):
    root.title("Welcome Page")

    # Defines the size of the window
    canvas = tk.Canvas(root, width=600, height=300)

    # Initializes the canvas. Columnspan creates 3 invisible columns which allows us
    # to place objects in our window with extra precision
    canvas.grid(columnspan=5, rowspan=10)

    # Instructions/Text
    instructions = tk.Label(root, text="Login", font=("Raleway", 18))
    instructions.grid(column=0, row=0)

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
                    parameter_page(root, username, parameter_database)
                    username_entry.delete(0, 'end')
                    password_entry.delete(0, 'end')
                    return

        login_response["text"] = "Login Failed"
        login_response.grid(column=1, row=4)
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        return


    # Username and Password Input Box
    username_entry = tk.Entry(root)
    username_label = tk.Label(root, text="Username:")
    username_entry.grid(column=1, row=1)
    username_label.grid(column=0, row=1)

    password_entry = tk.Entry(root)
    password_label = tk.Label(root, text="Password:")
    password_entry.grid(column=1, row=2)
    password_label.grid(column=0, row=2)

    # Login Button
    login_btn_text = tk.StringVar()
    login_btn = tk.Button(root, textvariable=login_btn_text, command=lambda: login(), font="Raleway", bg="#20bebe",
                          fg="white", height=2, width=15)
    login_btn_text.set("Login")
    login_btn.grid(column=1, row=3)

    #-------------------Registration feature-------------------------


    # Sign-up Button
    register_btn_text = tk.StringVar()
    register_btn = tk.Button(root, textvariable=register_btn_text, command=lambda:register_window(root, login_database), font="Raleway",
                             bg="#20bebe", fg="white", height=2, width=15)
    register_btn_text.set("Sign-up")
    register_btn.grid(column=2, row=3)

    if len(login_database["credentials"]) >= 10:
        register_btn.destroy()