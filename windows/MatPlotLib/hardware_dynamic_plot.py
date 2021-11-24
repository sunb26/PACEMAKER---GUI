import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import serial 
import time 


# Animate function 
    # ser is serial object 
def animate(i, data_lst, ser):
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    try:
        flt = float(string) # Casts the string from the serial communication to a float "flt"
        data_lst.append(flt) # Think that this is done twice to add the x then y values to the data list 
        data_lst.append(flt)
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

ser = serial.Serial() # COM as first input and number (Baud rate I think) as second input
time.sleep(2)
print(ser.name)

ani = animation.FuncAnimation(fig, animate, frames = 100, fargs = (data_lst, ser), interval = 200)
plt.show()

ser.close()
print("Serial Line Closed")


## So this (above) is how can do it so that set specific x axis limits 
# This will work if 