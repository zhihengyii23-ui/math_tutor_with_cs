"""
Calculus, 01_limits
Numeric approach to a limit from both sides
Symbolic check with Symp: limit, left/right limits
Visualize removable/jump/infinite behavior
Optional epsilon-delta band demo
First version: Nov.9, 2025
copyright: Cecilia Zhiheng Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ----- define expression & point -----
x = sp.symbols('x')
# sample: removable discontinuity with finite limit
f_expr = sp.sin(x) / x # tune if needed
x0 = 0.0 # tune if needed

"""
Optional samples:
f_expr = (x ** 2 -1) / (x - 1); x0 = 1.0 --> limit 2, removable
f_expr = sp.Abs(x) / x; x0 = 0.0 --> jump, no two-sided limit
f_expr = 1 / x; x0 = 0.0 --> infinite one-sided limits
f_expr = (sp.sin(x)) / x; x0 = 0.0 --> limit 1
"""

f = sp.lambdify(x, f_expr, "numpy")

# ------ symbolic limits for verification
L = sp.limit(f_expr, x, x0)
L_left = sp.limit(f_expr, x, x0, dir='-')
L_right = sp.limit(f_expr, x, x0, dir='+')

print("f(x) = ", f_expr)
print("x0 = ", x0)
print("limit =" , L)
print("left limit =" , L_left)
print("right limit =" , L_right)

# ----- numeric approach from both sides -----
# geometric approach sequences toward x0 to avoid hitting x0 exactly
scales = np.geomspace(1e-1, 1e-8, 40)

x_left_seq = x0 - scales
x_right_seq = x0 + scales

y_left_seq = f(x_left_seq)
y_right_seq = f(x_right_seq)

# ----- neighborhood plot -----
# choose a small symmetric window around x0 for plotting

win = max(1.0, 5 * float(scales[0]))
xx = np.linspace(x0 - win, x0 + win, 1200)
yy = f(xx)

mask = np.isfinite(yy)# mask out the exact x0 to avoid division by zero visuals

plt.figure()
plt.plot(xx[mask], yy[mask], label= "f(x)", linewidth = 2)

plt.scatter(x_left_seq, y_left_seq, s = 18, label = "approach from left")
plt.scatter(x_right_seq, y_right_seq, s = 18, label = "approach from right")

plt.axvline(x0, linewidth = 1)
try:
    L_float = float(L)
    if np.isfinite(L_float):
        plt.axhline(L_float, linestyle = '--', linewidth = 1, label = f"limit = {L_float:.6g}")
except Exception:
    pass

# if f(x0) is defined, show it; else show an open circle (hole) at (x0, ?)
# attempt to evaluate f at x0 numerically via small epsilon (robust)

x0_eval = x + 0.0
try:
    y0 = f(np.array([x0_eval]))[0]
    if np.isfinite(y0):
        plt.scatter([x0], [y0], s = 50, zorder = 5, label = "f(x0) (if defined)")
except Exception:
    pass

plt.title("Limit visualization near x0")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# ----- optional: epsilon-delta demo, finite limit only -----
# given a small epsilon, hunt for a delta so that |f(x) - L| < epsilon whenever 0 < |x-x0| < delta.
try:
    L_float = float(L)
    if np.isfinite(L_float):
        epsilon = 0.1
        # sample candidate deltas and test
        deltas = np.geomspace(1e-1, 1e-6, 50)
        delta_found = None
        for d in deltas[::-1]:
            xs_band = np.concatenate([
                np.linspave(x0 - d, x0 - d / 100, 100, endpoint = True),
                np.linspace(x0 + d / 100, x0 + d, 100, endpoint = True)
            ])
            ys_band = f(xs_band)
            ok = np.all(np.isfinite(ys_band)) and np.all(np.abs(ys_band - L_float) < epsilon)
            if ok:
                delta_found = d
                break
        plt.figure()
        plt.plot(xx[mask], yy[mask], linewidth = 2)
        plt.axvline(x0, linewidth = 1)
        plt.axhline(L_float + epsilon, linestyle = '--')
        plt.axhline(L_float - epsilon, linestyle = '--')
        if delta_found is not None:
            plt.axvspan(x0 - delta_found, x0 + delta_found, alpha = 0.15, label = f"δ = {delta_found:.2e}")
        plt.title(f"Epsilon-Delta band (ε = {epsilon})")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        if delta_found is not None:
            plt.legend()
        plt.show()
except Exception:
    pass

# ----- quick report -----
def safe_float(v):
    try:
        return float(v)
    except Exception:
        return v

print("\n--- Summary ---")
print("Two-sided limit: ", safe_float(L))
print("Left-hand limit: ", safe_float(L_left))
print("Right-hand limit: ", safe_float(L_right))
print("Last numeric left:", y_left_seq[-1])
print("Last numeric right:", y_right_seq[-1])







