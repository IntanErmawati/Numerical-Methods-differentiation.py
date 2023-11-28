import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.0, 0.2, 0.4])
y = np.array([0.00000, 0.74140, 1.3718])

plt.plot(x, y, marker='o', linestyle='-')
plt.title('Differentiation: Backward-difference')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
