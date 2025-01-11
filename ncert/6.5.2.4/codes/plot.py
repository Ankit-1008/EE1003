import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = |sin(4x) + 3|
def f(x):
    return np.abs(np.sin(4 * x) + 3)

# Numerical approximation of the derivative of f(x)
def df(x, delta=1e-5):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

# Define the shared library and functions
# Assuming the compiled shared library is named 'code.so'
c_lib = ctypes.CDLL('./code.so')  # Replace with the actual name of your .so file

# Define argument and return types for the C function 'run_gradient_descent'
c_lib.run_gradient_descent.argtypes = [
    ctypes.c_double,  # init_guess
    ctypes.c_double,  # step_size
    ctypes.c_double,  # tolerance
    ctypes.c_double,  # delta
    ctypes.POINTER(ctypes.c_double)  # minimum (output)
]

# Gradient descent via the C function
def run_gradient_descent(init_guess, step_size, tolerance, delta=1e-5):
    minimum = ctypes.c_double(0)  # Placeholder for the result
    c_lib.run_gradient_descent(init_guess, step_size, tolerance, delta, ctypes.byref(minimum))
    return minimum.value

# Generate points for plotting
def generate_points(n, x_min, x_max):
    x = np.linspace(x_min, x_max, n)
    y = f(x)
    return x, y

# Main script
if __name__ == "__main__":
    # Generate points for the function plot
    x_min, x_max = -np.pi, np.pi
    n_points = 1000
    x_vals, y_vals = generate_points(n_points, x_min, x_max)

    # Parameters for gradient descent
    init_guess = 0.5
    step_size = 0.01
    tolerance = 1e-6
    delta = 1e-5

    # Find the minimum using the C function
    minimum = run_gradient_descent(init_guess, step_size, tolerance, delta)

    # Plot the function
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="$f(x) = |sin(4x) + 3|$", color="blue")

    # Highlight the minimum point found
    plt.scatter([minimum], [f(minimum)], color="red", label="Minimum", zorder=5)
    plt.title("Function Plot and Gradient Descent")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

    print(f"Local minimum found at x = {minimum}, f(x) = {f(minimum)}")

