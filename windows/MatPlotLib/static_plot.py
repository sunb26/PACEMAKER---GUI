import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

from random import randint 

# Creating a static line plot
# data_list = [60, 59, 49, 51, 49, 52, 53]

# fig, ax = plt.subplots()

# ax.plot(data_list)
# ax.set_xlabel('Day Number')
# ax.set_ylabel('Temperature (*F)')
# ax.set_title('Temperature in Portland over 7 Days')

# # fig.savefig('static_plot.png')
# plt.show()


# # Creating an animated line plot

# # Empty lists for x and y data 
# x = []
# y = []

# fig, ax = plt.subplots()

# # Need to build the plot into a function that takes the input of the frame number in animation

# def animate(i):
#     pt = randint(1,9) # this will be the next y-value in the animate plot
#     x.append(i)
#     y.append(pt)

#     ax.clear()
#     ax.plot(x, y)
#     ax.set_xlim([0, 20])
#     ax.set_ylim([0, 10])

# # Now need to run the animation using this fuction
# # fig: the figure object defined above
# # animate: the function created above
# # frames: sets how many times the plot is redrawn (ie. how many times call the function)
# # interval: time between frames (times between function calls) in ms
# # repeat = False: after all frames are drawn, animation does not repeat 
# ani = FuncAnimation(fig, animate, frames = 20, interval = 500, repeat = False)

# plt.show()



# Creating a live-auto updating plot based on user input

# Initial data (will add more later)
data = [0, 0, 0, 0, 0]

fig, ax = plt.subplots()

# Build animate function that reads values from text file and plots them here
# The axes must be cleared each time redraw plot
# The line "ax.plot(data[-5:])" plots the last 5 data points 

def animate(i):
    with open('data.txt', 'r') as f:
        for line in f:
            data.append(float(line.strip()))
    ax.clear()
    ax.plot(data[-20:]) # So this sets the xlim to go from 0-20 basically 

ani = FuncAnimation(fig, animate, interval = 9000)

plt.show()