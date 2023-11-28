import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.1, 1.2, 1.3, 1.4])
y = np.array([9.025013, 11.02318, 13.46374, 16.44465])

dy_dx = np.gradient(y, x)

plt.plot(x, y, marker='o', linestyle='-', label='Function')
plt.plot(x, dy_dx, marker='x', linestyle='--', label='Three-Point Differentiation')
plt.title('Differentiation: Three-Point')
plt.xlabel('x')
plt.ylabel('y / dy_dx')
plt.legend()
plt.grid(True)
plt.show()
