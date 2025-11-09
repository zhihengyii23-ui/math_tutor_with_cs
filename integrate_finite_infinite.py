"""
extentions
integrate finite and infinite integrals
copyright: Cecilia Zhiheng Hu
"""


import sympy as sp

x = sp.symbols('x')

# ----- infinite integrals -----
f_expr = sp.sin(x) + 1.5
F_expr = sp.integrate(f_expr, x)
print("Antiderivative F(x) = ", F_expr)

# ----- finite integrals -----
a_val, b_val = 0, sp.pi
I = sp.integrate(f_expr, (x, a_val, b_val))
print("Definite integral = ", sp.N(I))

