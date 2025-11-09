"""
Extension
use trapezoid and simpson
copyright: Cecilia Zhiheng Hu
"""
import numpy as np

# ----- trapezoid -----
def trapz_integrate(f, a, b, n = 1000):
    xs = np.linspace(a, b, n + 1)
    ys = f(xs)
    return np.trapezoid(ys, xs)

val = trapz_integrate(lambda x: np.sin(x) + 1.5, 0, np.pi, n = 1000)
print("Trapz = ", val)

def simpson_integrate(f, a, b, n = 1000 ):
    if n % 2 == 1:
        n += 1
    xs = np.linspace(a, b, n + 1)
    dx = (b - a) / n
    ys = f(xs)
    S = ys[0] + ys[-1] + 4 * np.sum(ys[1:-1:2]) + 2 * np.sum(ys[2:-1:2])
    return S * dx / 3

val = simpson_integrate(lambda x: np.sin(x) + 1.5, 0, np.pi, n = 1000)
print("Simpson = ", val)