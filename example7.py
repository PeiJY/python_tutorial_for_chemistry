# ============ 7. Violin Plot Example ============
import matplotlib.pyplot as plt

data1 = [2, 3, 5, 6, 7, 8, 9]
data2 = [5, 6, 7, 8, 8, 10, 12]
data3 = [1, 2, 2, 3, 3, 4, 5]

data = [data1, data2, data3]

plt.violinplot(data, showmeans=True)

plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.ylabel("Value")
plt.title("Violin Plot Example")
plt.show()
plt.savefig('example7.png', dpi=300, bbox_inches='tight')

# clear the current figure and close it
plt.clf()
plt.close()
