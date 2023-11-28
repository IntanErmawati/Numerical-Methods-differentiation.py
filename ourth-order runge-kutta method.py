# Function to perform Fourth-Order Runge-Kutta Method for numerical differentiation
def runge_kutta_method(x, y, h):
    dy_dx = []

    for i in range(len(x) - 1):
        k1 = h * numerical_derivative(y[i], x[i])
        k2 = h * numerical_derivative(y[i] + k1 / 2, x[i] + h / 2)
        k3 = h * numerical_derivative(y[i] + k2 / 2, x[i] + h / 2)
        k4 = h * numerical_derivative(y[i] + k3, x[i] + h)
        y[i+1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        dy_dx.append(y[i+1] / h)
    return dy_dx

def numerical_derivative(y, x):
    return (y**2) / x

x_data = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6]
y_data = [-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966]

print("Input values:")
for xi, yi in zip(x_data, y_data):
    print(f"x: {xi}, y: {yi}")
h = x_data[1] - x_data[0]
dy_dx_result = runge_kutta_method(x_data, y_data, h)

print("Fourth-Order Runge-Kutta Method results:")
for dy_dx_val in dy_dx_result:
    print(f"dy_dx: {dy_dx_val}")
