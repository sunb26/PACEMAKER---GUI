import tkinter as tk
import json

# Opens new window for registration
def register_window(root, login_database):

    register_window = tk.Toplevel(root)
    register_window.title("Register")
    reg_canvas = tk.Canvas(register_window, width=600, height=300)
    reg_canvas.grid(columnspan=5, rowspan=10)

    register_label = tk.Label(register_window, text="Register", font=("Raleway", 18))
    register_label.grid(column=0, row=0)

    create_user_response = tk.Label(register_window)
    def create_user():
        username = new_username_entry.get()
        password = new_password_entry.get()

        if " " in username or " " in password:
            create_user_response["text"] = "No spaces allowed in entries"
            create_user_response.grid(column=1, row=4)
            return 

        # Checks if fields are empty
        if len(username) == 0 or len(password) == 0:
            create_user_response["text"] = "Please fill in all the required fields"
            create_user_response.grid(column=1, row=4)
            return

        # Checks if the username already exists
        for cred in login_database['credentials']:
            if cred['username'] == username:
                create_user_response["text"] = f"{username} is already taken"
                create_user_response.grid(column=1, row=4)
                new_username_entry.delete(0, 'end')
                new_password_entry.delete(0, 'end')
                return

        # Updates credentials database
        login_database['credentials'].append({"username": f"{username}", "password": f"{password}"})
        with open("database/login_data.json", "w") as database:
            json.dump(login_database, database)

        # if len(login_database["credentials"]) >= 10:
        #     register_btn.destroy()
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

    new_password_entry = tk.Entry(register_window, show="*")
    new_password_label = tk.Label(register_window, text="Password:")
    new_password_entry.grid(column=1, row=2)
    new_password_label.grid(column=0, row=2)