import matplotlib.pyplot as plt
import numpy as np

x = np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
y = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966])

dy_dx = np.gradient(y, x)

plt.plot(x, y, marker='o', linestyle='-', label='Function')
plt.plot(x, dy_dx, marker='x', linestyle='--', label='Five-Point Differentiation')
plt.title('Differentiation: Five-Point')
plt.xlabel('x')
plt.ylabel('y / dy_dx')
plt.legend()
plt.grid(True)
plt.show()
