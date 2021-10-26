import tkinter as tk
import json
from windows.welcome import welcome_page

# Import login database
try:
    with open("database/login_data.json") as database:
        login_database = json.load(database)

except:
    print("Database is empty or does not exist. Please register.")
    login_database = {"credentials": []}
    pass

try:
    with open("database/parameters.json") as database2:
        parameter_database = json.load(database2)
except:
    print("No Parameter Inputs Found")


# Define the start of the Window Object
root = tk.Tk()

welcome = welcome_page(root, login_database, parameter_database)


root.mainloop()  # All code after this line will not display in the window object
