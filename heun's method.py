# Function to perform Heun's Method for numerical differentiation
def heuns_method(x, y):
    h = x[1] - x[0]  
    dy_dx = []

   
    for i in range(len(x) - 1):
        y_predictor = y[i] + h * numerical_derivative(y[i], x[i])
        y_corrector = y[i] + (h / 2) * (numerical_derivative(y[i], x[i]) + numerical_derivative(y_predictor, x[i+1]))
        
        dy_dx.append((y_corrector - y[i]) / h)

    return dy_dx

def numerical_derivative(y, x):
    return (y**2) / x

x_data = [1.1, 1.2, 1.3, 1.4]
y_data = [9.025013, 11.02318, 13.46374, 16.44465]

print("Input values:")
for xi, yi in zip(x_data, y_data):
    print(f"x: {xi}, y: {yi}")
dy_dx_result = heuns_method(x_data, y_data)

print("Heun's Method results:")
for dy_dx_val in dy_dx_result:
    print(f"dy_dx: {dy_dx_val}")
