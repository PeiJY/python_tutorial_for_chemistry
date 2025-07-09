# ============ 6. X Y Plot Example ============
import matplotlib.pyplot as plt
data_x = [1.5, 4.2, 5.0, 6.8, 9.1]
data_y = [2.3, 4.1, 6.0, 6.1, 6.3]
plt.plot(data_x, data_y, marker='.', markersize=20, linestyle='-', color='black')
plt.title('Sample Data Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
# plt.show()
plt.savefig('example6.png', dpi=300, bbox_inches='tight')

# clear the current figure and close it
plt.clf()
plt.close()
