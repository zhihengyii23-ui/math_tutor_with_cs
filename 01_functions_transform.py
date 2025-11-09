"""
Precalculus, 01_functions_transform
Visualize y = a * f(b*(x-h)) + k
Quick test on translations, stretches/shrink, reflections
First Version: Nov.8, 2025
copyright: Cecilia Zhiheng Hu
"""

import numpy as np
import matplotlib.pyplot as plt


# ----- graphing tools -----

def plot_functions(f, x, title):
    y = f(x)
    plt.figure()
    plt.plot(x, y, linewidth = 2)
    plt.axhline(0, linewidth = 1)
    plt.axvline(0, linewidth = 1)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# ----- major function entrance -----

def transform(f, a = 1.0, b = 1.0, h = 0.0, k = 0.0):
    """
    f(x) = a * f(b*(x-h)) + k
    """
    def g(x):
        return a * f(b*(x-h)) + k
    return g

# ----- mother functions -----
# can add more mother functions

def f_linear(x):
    return x

def f_quadratic(x):
    return x ** 2

def f_abs(x):
    return np.abs(x)

def f_cubic(x):
    return x ** 3

def f_reciprocal(x):
    y = np.empty_like(x, dtype = float)
    y[:] = np.nan
    m = x != 0
    y[m] = 1.0 / x[m]
    return y

def f_sin(x):
    return np.sin(x)

#def f_cos(x):
    return np.cos(x)

#def f_tan(x):
    return np.tan(x)

#def f_exp(x):
    return np.exp(x)

#def f_log(x):
    return np.log(x)

# ----- base parents f entrance -----
xs = np.linspace(-5, 5, 1001)
PARENTS = [
    ("linear", f_linear),
    ("quadratic", f_quadratic),
    ("absolute", f_abs),
    ("cubic", f_cubic),
    ("reciprocal", f_reciprocal),
    ("sin", f_sin)
    #("cos", f_cos),
    #("tan", f_tan),
    #("exp", f_exp),
    #("log", f_log),
]

for name, f in PARENTS:
    plot_functions(f, xs, f"paren: {name}")

# ----- example 1: quadratic -----
f = f_quadratic
xs = np.linspace(-6, 6, 1201)

# 1. translate
g1 = transform(f, h = 2, k = -3)
plot_functions(g1, xs, "x^2 translated: h = 2, k = -3")

# 2. vertical stretch + reflect across x-axis
g2 = transform(f, a = -2)
plot_functions(g2, xs, "x^2 with a= -2 (stretch by 2+ reflect across x-axis)")

# 3. horizontal compress (b=2) + vertical compress (a=0.5)
g3 = transform(f, a = 0.5, b = 2.0)
plot_functions(g3, xs, "x^2 with a = 0.5, b = 2 (vertical compress + horizontal compress")

# 4. combo: shift then horizontal stretch (b=0.5)
g4 = transform(f, b = 0.5, h = 1, k = 1)
plot_functions(g3, xs, "x^2 with h = 1, k = 1, b = 0.5 (horizontal stretch)")

# ----- example 2: sine (period/amplitude/phase/midline) -----
f = f_sin
xs = np.linspace(-2*np.pi, 2*np.pi, 2001)

# original
plot_functions(f, xs, "y = sin(x)")

# change a, b, h, k
g = transform(f, a = 1.5, b = 2.0, h = np.pi/6, k = 0.5)
plot_functions(g, xs, "y = 1.5 sin(2(x - pi/6)) + 0.5 (Amp = 1.5, T = pi, midline = 0.5)")

# ----- practice -----
# Problem: f(x) = |x|
# 1) right shift 3, up shift 2
# 2) reflect across x-axis then up 1
# 3) horizontal compress to half width
f= f_abs
xs = np.linspace(-8, 8, 1601)

g1 = transform(f, h = 3, k = 2)
plot_functions(g1, xs, "P_1: |x| -> right 3, up 2")

g2 = transform(f, a = -1, k = 1)
plot_functions(g2, xs, "P_2: |x| reflect across x-axis, then up 1")

g3 = transform(f, b = 2)
plot_functions(g3, xs, "P_3: |x| horizontal compress by factor 2 (half width)")

# ----- challenge -----
# Build g(x) so that:
# - vertex/extremum at (2, -1)
# - vertical scale *3
# - horizontal length half (i.e., b =2)
# example with quadratic parent
f = f_quadratic
xs = np.linspace(-8, 8, 1601)
g = transform(f, a = 3, b = 2, h = 2, k = -1)
plot_functions(g, xs, "Challenge sample (quadratic): a = 3, b = 2, h = 2, k = -1")
