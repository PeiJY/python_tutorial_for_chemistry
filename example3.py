# ============ 3. Basic Statistics Example ============
print(" ----------- example 3: basic statistics -----------")
import statistics
data = [1.5, 3.2, 5.0, 7.8, 2.1]

mean_val = statistics.mean(data)
variance_val = statistics.variance(data)
max_val = max(data)
min_val = min(data)
median_val = statistics.median(data)
print(f"Mean: {mean_val}")
print(f"Variance: {variance_val}")  
print(f"Max: {max_val}")
print(f"Min: {min_val}")
print(f"Median: {median_val}")
