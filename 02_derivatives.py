"""
Calculus, 02_derivatives
# visualize derivative
# verification of calculus
# First version: Nov.8, 2025
# copyright: Cecilia Zhiheng Hu
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ----- base -----

def f(x):
    return x**3 - 3*x + 1 #tune, here is just an example
    #return np.sin(x) or np.exp(x)

# ----- numerical derivative -----

def derivative_numeric(f, x, h = 1e-5):
    """
    f'(x) = [f(x + h) - f(x - h)] / 2h
    """
    return (f(x + h) - f(x - h)) / (2 * h)

# ----- tangent line at a point -----

def tangent_line(f, x0, h = 1e-5):
    """
    x0: the point that tangent line"touched"
    """
    m = derivative_numeric(f, x0, h) # the slope at x0
    y0 = f(x0) # the function at x0
    return m, lambda x: m * (x - x0) + y0 # x -> y - y0 = m * (x - x0)
    # return m, and a lambda function. need to call m in the following code
# ----- plot tangent at a point

xs = np.linspace(-3, 3, 400)
x0 = 0.0 #tune it if needed
m, tangent = tangent_line(f, x0)

plt.figure()
plt.plot(xs, f(xs), label = 'f(x)')
plt.plot(xs, tangent(xs), '--', label = f"Tangent at x0 = {x0}, slope = {m:.3f}")
plt.scatter([x0], [f(x0)], color = 'red', zorder = 5)
plt.legend()
plt.title("Derivative as Tangent Slope")
plt.grid(True)
plt.show()

# ----- full derivative curve -----

fprime_num = derivative_numeric(f, xs)

plt.figure()
plt.plot(xs, f(xs), label = "f(x)")
plt.plot(xs, fprime_num, label = "f(x) numeric")
plt.legend()
plt.title("Function and Its Derivative")
plt.grid(True)
plt.show()

# ----- symbolic derivative for verification -----

x = sp.symbols('x')
f_expr = x**3 - 3*x + 1
fprime_expr = sp.diff(f_expr, x)
print("f'(x) = ", fprime_expr)
print("f'(1) =", fprime_expr.subs(x, 0).evalf()) # tune if needed

