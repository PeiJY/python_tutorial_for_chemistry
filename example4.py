# ============ 4. Data Manipulation Example ============

data = [1.5, 3.2, 5.0, 7.8, 2.1]
print(" ----------- example 4: data manipulation -----------")
ascending_sorted_data = sorted(data)
print(f"Ascending sorted data: {ascending_sorted_data}")
# [1.5, 2.1, 3.2, 5.0, 7.8]

descending_sorted_data = sorted(data, reverse=True)
print(f"Descending sorted data: {descending_sorted_data}")
# [7.8, 5.0, 3.2, 2.1, 1.5]

filtered_data = [x for x in data if x > 3 and x < 6]
print(f"Filtered data (3 < x < 6): {filtered_data}")
# [3.2, 5.0]
