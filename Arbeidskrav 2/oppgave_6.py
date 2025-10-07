import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)

# definere funksjonen
y = -x**2 - 5

# lage linjediagrammet
plt.plot(x, y)

# viser grafen
plt.show()