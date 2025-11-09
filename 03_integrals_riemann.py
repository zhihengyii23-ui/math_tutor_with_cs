"""
Calculus, 03_integrals_riemann
Visualize Riemann sums as approximations to ∫ f(x) dx
First version: Nov.9, 2025
copyright: Cecilia Zhiheng Hu
"""

import numpy as np
import matplotlib.pyplot as plt

# ----- function def -----
def f(x):
    return np.sin(x) + 1.5 #tune if needed

a, b = 0, np.pi #finite integrals, integration bounds
n = 20 # number of rectangles
xs = np.linspace(a, b, n + 1)
dx = (b - a) / n

# ----- choose sample points -----
x_left = xs[:-1] #left endpoint
x_right = xs[1:] #right endpoint
x_mid = (xs[:-1] + xs[1:]) / 2 #midpoint

# ----- compute riemann sums -----
L_sum = np.sum(f(x_left) * dx)
R_sum = np.sum(f(x_right) * dx)
M_sum = np.sum(f(x_mid) * dx)

print(f"Left Riemann sum: {L_sum:.6f}")
print(f"Right Riemann sum: {R_sum:.6f}")
print(f"Mid Riemann sum: {M_sum:.6f}")

# ----- visualize (midpoint) -----
x_plot = np.linspace(a, b, 400)
plt.plot(x_plot, f(x_plot), 'b', linewidth = 2, label = 'f(x)')

for x in x_mid:
    plt.bar(x - dx/2, f(x), width = dx, align = 'edge', alpha = 0.3, edgecolor = 'k')

plt.title(f"Riemann Sum (n={n}, Midpoint rule)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
