import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time 

import random


# Animate function 
    # ser is serial object 
def animate(i, data_lst, ser):
    #b = ser.readline()
    #string_n = b.decode()
    #string = string_n.rstrip()
    string = ser
    try:
        flt = float(string) # Casts the string from the serial communication to a float "flt" (shouldn't be needed because we're receiving doubles)
        data_lst.append(flt) # This currently jut plots constant value because flt not changing 
    except:
        pass    

    data_lst = data_lst[-100:] # Shows the previous 100 values 

    ax.clear()
    ax.plot(data_lst)
    ax.set_ylim([0, 1050])
    ax.set_title('Live Plot Reading')
    ax.set_ylabel('Reading')

data_lst = [] # This is empty list to store data coming in from hardware 
fig, ax = plt.subplots()

# ser = serial.Serial() # COM as first input and number (Baud rate I think) as second input
#x = random.randint(1, 100)
ser = '500' # So this is the y-value for the plot 
#time.sleep(1)



print(ser)

# The interval is how often (ms) the graph updates, so directily effects the x-values 
ani = animation.FuncAnimation(fig, animate, frames = 100, fargs = (data_lst, ser), interval = 2000)
plt.show()

# ser.close()
# print("Serial Line Closed")


## So this (above) is how can do it so that set specific x axis limits 
# This will work if 