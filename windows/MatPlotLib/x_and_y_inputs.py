import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def animate(i):
    f = open('data.txt','r').read()
    lines = f.split('\n') # This assuming data text file has each xy pair separated by a new line
    xs = []
    ys = []

    for line in lines:
        if line == "":
            break
        else:
            x,y = line.split(',') # This assuming data text file has x and y separated by ,
            xs.append(float(x))
            ys.append(float(y))
            print("X-Values: ") 
            print(xs)
            print("Y-Values: ")
            print(ys)

    ax1.clear()
    ax1.plot(xs, ys)
    plt.xlabel('Time')
    plt.ylabel('mV')
    plt.title('Voltage With Respect to Time')

fig1, ax1 = plt.subplots()
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
ani1 = animation.FuncAnimation(fig1, animate, interval = 1000)
plt.show()

fig2, ax2 = plt.subplots()
ani2 = animation.FuncAnimation(fig2, animate, interval = 1000)
plt.show()