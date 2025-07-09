
# ============ 1. variance ============
print(" ----------- example 1: variance calculation -----------")
a = 4
b = 5
c = 6
mean_of_abc = (a + b + c ) / 3
sqa = (a - mean_of_abc) * (a - mean_of_abc)
sqb = (b - mean_of_abc) * (b - mean_of_abc)
sqc = (c - mean_of_abc) * (c - mean_of_abc)
var1 = (sqa + sqb + sqc) / 3
print(f"Variance of {a}, {b}, {c} is: {var1}")

d = 10
e = 20
f = 30
mean_of_def = (d + e + f) / 3
sqd = (d - mean_of_def) * (d - mean_of_def)
sqe = (e - mean_of_def) * (e - mean_of_def)
sqf = (f - mean_of_def) * (f - mean_of_def)
var2 = (sqd + sqe + sqf) / 3
print(f"Variance of {d}, {e}, {f} is: {var2}")
