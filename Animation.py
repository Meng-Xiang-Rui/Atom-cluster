import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], '-r', animated=False)

x = np.loadtxt(r"C:\Users\OptLa\Documents\Meng\\opt1.txt")
y = np.loadtxt(r"C:\Users\OptLa\Documents\Meng\\opt2.txt")


# x = np.linspace(9,15)
# y = np.linspace(9,15)

def init():
    ax.set_xlim(8, 16)
    ax.set_ylim(8, 16)
    return line,

def update(i):
    xdata.append(x[i])
    ydata.append(y[i])
    line.set_data(xdata, ydata)
    return line,

ani = FuncAnimation(fig, update, frames=range(len(x)),
    init_func=init, interval=150, blit=True)
ani.save("second.gif")
# plt.show()