import tkinter as tk
import json
from windows.welcome import welcome_page




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
welcome = welcome_page(root, login_database)

root.mainloop()  # All code after this line will not display in the window object
