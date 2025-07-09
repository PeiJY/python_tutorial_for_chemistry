# ============ 9. 3D Scatter Plot Example ============
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]
z = [1, 3, 5, 7, 9]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Scatter Plot')
plt.show()
plt.savefig('example9.png', dpi=300, bbox_inches='tight')

# clear the current figure and close it
plt.clf()
plt.close()

