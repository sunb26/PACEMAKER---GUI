import tkinter as tk
import json



# Import login database
try:
    with open("login_data.json") as database:
        login_database = json.load(database)

except:
    print("Database is empty or does not exist. Please register.")
    login_database = {"credentials": []}
    pass


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

login_response = tk.Label(root)


# Function for button click. Checks database for login credentials and outputs
# success or failure if login is correct or not
def login():
    global login_response
    username = username_entry.get()
    password = password_entry.get()
    login_success = False
    login_response.destroy()

    for cred in login_database['credentials']:
        if cred['username'] == username:
            if cred['password'] == password:
                login_response = tk.Label(root, text="Login Successful")
                login_response.grid(column=1, row=4)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                return

    login_response = tk.Label(root, text="Login Failed")
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


# Opens new window for registration
def register_window():

    register_window = tk.Toplevel(root)
    register_window.title("Register")
    reg_canvas = tk.Canvas(register_window, width=600, height=300)
    reg_canvas.grid(columnspan=5, rowspan=10)

    register_label = tk.Label(root, text="Register", font=("Raleway", 18))
    register_label.grid(column=0, row=0)

    def create_user():
        username = new_username_entry.get()
        password = new_password_entry.get()

        # Checks if fields are empty
        if len(username) == 0 or len(password) == 0:
            create_user_response = tk.Label(register_window, text="Please fill in all the required fields")
            create_user_response.grid(column=1, row=4)
            return

        # Checks if the username already exists
        for cred in login_database['credentials']:
            if cred['username'] == username:
                create_user_response = tk.Label(register_window, text=f"{username} is already taken")
                create_user_response.grid(column=1, row=4)
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                return

        # Updates credentials database
        login_database['credentials'].append({"username": f"{username}", "password": f"{password}"})
        with open("login_data.json", "w") as database:
            json.dump(login_database, database)

        if len(login_database["credentials"]) >= 10:
            register_btn.destroy()
        # Closes registration window
        register_window.destroy()

    create_creds_btn_text = tk.StringVar()
    create_creds_btn = tk.Button(register_window, textvariable=create_creds_btn_text, command=create_user,
                                 font="Raleway", bg="#20bebe",
                                 fg="white", height=2, width=15)
    create_creds_btn_text.set("Create User")
    create_creds_btn.grid(column=1, row=3)

    new_username_entry = tk.Entry(register_window)
    new_username_label = tk.Label(register_window, text="New Username:")
    new_username_entry.grid(column=1, row=1)
    new_username_label.grid(column=0, row=1)

    new_password_entry = tk.Entry(register_window)
    new_password_label = tk.Label(register_window, text="Password:")
    new_password_entry.grid(column=1, row=2)
    new_password_label.grid(column=0, row=2)

# Sign-up Button
register_btn_text = tk.StringVar()
register_btn = tk.Button(root, textvariable=register_btn_text, command=register_window, font="Raleway",
                         bg="#20bebe", fg="white", height=2, width=15)
register_btn_text.set("Sign-up")
register_btn.grid(column=2, row=3)

if len(login_database["credentials"]) >= 10:
    register_btn.destroy()

root.mainloop()  # All code after this line will not display in the window object
