# ============ 12. Draw Molecular Structure Example ============
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.spatial.distance import cdist # for calculating distances

# 1. Load data from CSV
data = []
header = []
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        data.append(row)

# 2. Split different elements and filter out unwanted elements
data = [line for line in data if line[0] != 'O' and line[0] != 'H']  # filter out O and H
na_data = [line for line in data if line[0] == 'Na']
cl_data = [line for line in data if line[0] == 'Cl']

# 3. Split elements and coordinates
na_coords = []
for line in na_data:
    na_coords.append([float(x) for x in line[1:]])
na_coords = np.array(na_coords)

cl_coords = []
for line in cl_data:
    cl_coords.append([float(x) for x in line[1:]])
cl_coords = np.array(cl_coords)

# 4. Use KDTree to find Na-Cl pairs within 3 Å
distance_matrix = cdist(na_coords, cl_coords)
bonds = np.argwhere(distance_matrix < 3)

# 5. Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot Na atoms
na_scatter = ax.scatter(*na_coords.T, color='blue', label='Na', s=300, marker='o')
# Plot Cl atoms
cl_scatter = ax.scatter(*cl_coords.T, color='green', label='Cl', s=600, marker='o')

# Draw bonds
lines = []
print(len(bonds), "bonds found")
for start, end in bonds:
    start_coord = na_coords[start]
    end_coord = cl_coords[end]
    line = ax.plot([start_coord[0], end_coord[0]], [start_coord[1], end_coord[1]],
                    [start_coord[2], end_coord[2]], color='gray', lw=2)
    lines.append(line)

# set range to avoid shaking when rotating
ax.set_xlim(np.min([na_coords[:,0], cl_coords[:,0]]) - 1, np.max([na_coords[:,0], cl_coords[:,0]]) + 1)
ax.set_ylim(np.min([na_coords[:,1], cl_coords[:,1]]) - 1, np.max([na_coords[:,1], cl_coords[:,1]]) + 1)
ax.set_zlim(np.min([na_coords[:,2], cl_coords[:,2]]) - 1, np.max([na_coords[:,2], cl_coords[:,2]]) + 1)


# 6. Set labels and title
ax.set_xlabel("X (Å)")
ax.set_ylabel("Y (Å)")
ax.set_zlabel("Z (Å)")
ax.set_title("NaCl 4x4x4 Supercell with Na-Cl Bonds (< 3 Å)")
ax.legend()
plt.tight_layout()

# 7. Make GIF animation
# function to update the view angle
def update(angle):
    ax.view_init(elev=30, azim=angle)
    return [na_scatter, cl_scatter] + lines

ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 360, 120),  # from 0° to 360°, total 120 frames
    interval=100,
    blit=False # blit=False to ensure all elements are redrawn in each frame
)

ani.save('example12.gif', writer='pillow', fps=20)