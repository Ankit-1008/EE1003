import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
code = ctypes.CDLL('./code.so')

# Define the argument and return types for the trapezoidal function
code.trapezoidal.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
code.trapezoidal.restype = ctypes.c_double

# Parameters
x1 = 0.0  # Lower bound of integration
x2 = 1.0  # Upper bound of integration
steps = 1000  # Number of steps (adjust for accuracy)

# Compute the area using the trapezoidal function in C
area = code.trapezoidal(x1, x2, steps)
print(f"Computed area between the curves: {area}")

# Define the Python functions for the curves
def f1(x):
    return np.sqrt(1 - (x - 1)**2)

def f2(x):
    return np.sqrt(1 - x**2)

# Generate x values for plotting
x_values = np.linspace(x1, x2, steps)
f1_values = f1(x_values)
f2_values = f2(x_values)

# Plot the curves
plt.plot(x_values, f1_values, label=r'$f_1(x) = \sqrt{1 - (x-1)^2}$', color='blue')
plt.plot(x_values, f2_values, label=r'$f_2(x) = \sqrt{1 - x^2}$', color='green')
plt.fill_between(x_values, f1_values, f2_values, where=(f1_values > f2_values), 
                 interpolate=True, color='lightblue', alpha=0.5, label='Area')

# Add labels, legend, and show the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Between Curves')
plt.legend()
plt.grid(True)
plt.show()

