# ============ 5. Plot Example ============
import matplotlib.pyplot as plt
data = [1.5, 3.2, 5.0, 7.8, 2.1]
plt.plot(data, marker='.', markersize=20, linestyle='-', color='black')
plt.title('Sample Data Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
# plt.show()
plt.savefig('example5.png', dpi=300, bbox_inches='tight')

# clear the current figure and close it
plt.clf()
plt.close()
