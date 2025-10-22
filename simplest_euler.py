import numpy as np
import matplotlib.pyplot as plt


omega = 2 * np.pi
h = 0.01           #tune
T = 2              #tune
n_steps = int(T / h)


x = 1.0   #tune
v = 0.0   #tune


t_hist, x_hist, v_hist = [0], [x], [v]


for i in range(n_steps):
    x_new = x + h * v
    v_new = v - h * (omega**2) * x
    t_hist.append(t_hist[-1] + h)
    x_hist.append(x_new)
    v_hist.append(v_new)
    x = x_new
    v = v_new


plt.figure(figsize=(6,4))
plt.plot(t_hist, x_hist, label="Euler x(t)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement x")
plt.title("Simple Harmonic Oscillator (Euler Method)")
plt.grid(True)
plt.legend()
plt.show()
