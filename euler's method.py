# Function to perform Euler Method
def euler_method(x, y, dx, p0, p2, p6):
    results = [(x[0], y[0])]
    for i in range(1, len(x)):
        h = dx
        x_end = x[i-1] + h
        if x_end > x[i]:
            x_end = x[i]

        y_value = y[i-1]  

        while x[i-1] < x_end:
            y_value = y_value + h * (p0 * y_value + p2 * y_value**2 + p6 * y_value**6)
            x[i-1] = x[i-1] + h
            results.append((x[i-1], y_value))

    return results


x = [0.0, 0.2, 0.4]
y = [0.00000, 0.74140, 1.3718]


print("Input values:")
for xi, yi in zip(x, y):
    print(f"x: {xi}, y: {yi}")


p0_coefficient = 1.0
p2_coefficient = 1.0
p6_coefficient = 1.0
results = euler_method(x, y, dx=0.1, p0=p0_coefficient, p2=p2_coefficient, p6=p6_coefficient)
x_results, y_results = zip(*results)

print("Euler method results:")
for xi, yi in zip(x_results, y_results):
    print(f"x: {xi}, y: {yi}")
