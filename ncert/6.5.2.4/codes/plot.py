import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = |sin(4x) + 3|
def f(x):
    return np.abs(np.sin(4 * x) + 3)

# Numerical approximation of the derivative of f(x)
def df(x, delta=1e-5):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

# Gradient descent function to find local minima
def gradient_descent(init_guess, step_size, tolerance, delta=1e-5):
    current_guess = init_guess
    grad = df(current_guess, delta)
    iterations = 0

    while np.abs(grad) > tolerance:
        grad = df(current_guess, delta)
        current_guess -= step_size * grad
        iterations += 1

    print(f"Gradient descent converged after {iterations} iterations.")
    return current_guess

# Generate points for the plot
def generate_points(n, x_min, x_max):
    x = np.linspace(x_min, x_max, n)
    y = f(x)
    return x, y

# Main script
if __name__ == "__main__":
    # Generate points for the function plot
    x_min, x_max = -np.pi, np.pi
    n_points = 1000
    x, y = generate_points(n_points, x_min, x_max)

    # Run gradient descent
    init_guess = 0.5
    step_size = 0.01
    tolerance = 1e-6
    minimum = gradient_descent(init_guess, step_size, tolerance)

    # Plot the function
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="$f(x) = |sin(4x) + 3|$", color="blue")

    # Highlight the minimum point found
    plt.scatter([minimum], [f(minimum)], color="red", label="Minimum", zorder=5)
    plt.title("Function Plot and Gradient Descent")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

    print(f"Local minimum found at x = {minimum}, f(x) = {f(minimum)}")

