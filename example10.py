# ============ 10. 3D Scatter GIF Example ============
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 3D data
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
z = [1, 3, 5, 7, 9]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# draw initial scatter plot
scatter = ax.scatter(x, y, z, c='r', s=50)

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 10)
ax.set_zlim(0, 10)

# function to update the view angle
def update(angle):
    ax.view_init(elev=30, azim=angle)
    return scatter,

# create animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 360, 120),  # from 0° to 360°, total 120 frames
    interval=100,
    blit=True
)

# save GIF file
ani.save("example10.gif", writer='pillow', fps=20)
