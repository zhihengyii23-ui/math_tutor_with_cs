"""
Calculus, 04_parametric_polar
Parametric & polar curves
visualize curves defined by parametric or polar equations
"""
import numpy as np
import matplotlib.pyplot as plt

# ----- parametric curve -----
t = np.linspace(0, 2*np.pi, 500)
x = np.sin(3 * t)
y = np.cos(2 * t)

plt.figure()
plt.plot(x, y)
plt.axis("equal")
plt.title("Parametric: x= sin(3t), y = cos(2t) ")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()

# ----- polar curve -----
theta = np.linspace(0, 2*np.pi, 600)
r = 2 + np.sin(5 * theta)

plt.figure()
plt.polar(theta, r)
plt.title("Polar: r = 2 + sin(5 * theta)")
plt.show()