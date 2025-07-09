
# =========== 2. variance function ============
print(" ----------- example 2: variance function -----------")
def calculate_var(a,b,c):
    mean_of_abc = (a + b + c ) / 3
    sqa = (a - mean_of_abc) * (a - mean_of_abc)
    sqb = (b - mean_of_abc) * (b - mean_of_abc)
    sqc = (c - mean_of_abc) * (c - mean_of_abc)
    var_abc = (sqa + sqb + sqc) / 3
    return var_abc

var1 = calculate_var(4, 5, 6)
print(f"Variance of 4, 5, 6 is: {var1}")
var2 = calculate_var(10, 20, 30)
print(f"Variance of 10, 20, 30 is: {var2}")
