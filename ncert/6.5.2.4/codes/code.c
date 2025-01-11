#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function definition for f(x) = |sin(4x) + 3|
double f(double x) {
    return fabs(sin(4 * x) + 3);
}

// Derivative of f(x), considering gradient descent is applied
// Note: Numerical approximation of the derivative is used
double df(double x, double delta) {
    return (f(x + delta) - f(x - delta)) / (2 * delta);
}

// Function to generate points for the graph
void generate_points(double *points, int n, double x_min, double x_max) {
    double h = (x_max - x_min) / n;
    double x = x_min;
    for (int i = 0; i < n; i++) {
        points[2 * i] = x;        // x-coordinate
        points[2 * i + 1] = f(x); // f(x) = |sin(4x) + 3|
        x += h;
    }
}

// Function to run gradient descent to find local minima or maxima
void run_gradient_descent(double init_guess, double step_size, double tolerance, double delta, double *minimum) {
    int count = 0;
    double current_guess = init_guess;
    double grad;
    
    while (1) {
        grad = df(current_guess, delta); // Calculate derivative
        if (fabs(grad) < tolerance) {
            break; // Stop when gradient is small enough
        }
        current_guess -= step_size * grad; // Update using gradient descent
        count++;
    }
    
    printf("Number of iterations: %d\n", count);
    *minimum = current_guess;
}

// Free memory allocated for points array
void free_ptr(double *points) {
    free(points);
}
