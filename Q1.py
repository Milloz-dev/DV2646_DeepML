import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x, y):
    return (x - 3)**2 + (y + 2)**2

# Partial derivatives
def grad_f(x, y):
    dfdx = 2 * (x - 3)
    dfdy = 2 * (y + 2)
    return dfdx, dfdy

# Gradient descent
learning_rate = 0.1
num_iterations = 50

# Initial values
x, y = 0.0, 0.0

# Store history
x_history = [x]
y_history = [y]
loss_history = [f(x, y)]

for i in range(num_iterations):
    dfdx, dfdy = grad_f(x, y)

    x = x - learning_rate * dfdx
    y = y - learning_rate * dfdy

    x_history.append(x)
    y_history.append(y)
    loss_history.append(f(x, y))

print(f"Final x: {x:.6f}")
print(f"Final y: {y:.6f}")
print(f"Final function value: {f(x, y):.6f}")

# Plot loss curve
plt.figure(figsize=(8, 5))
plt.plot(loss_history, marker='o')
plt.title("Gradient Descent Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("f(x, y)")
plt.grid(True)
plt.show()

# Plot optimization trajectory
x_vals = np.linspace(-1, 5, 200)
y_vals = np.linspace(-5, 2, 200)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)

plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=20)
plt.plot(x_history, y_history, marker='o', color='red')
plt.title("Gradient Descent Optimization Trajectory")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()