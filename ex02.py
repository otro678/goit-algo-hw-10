import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

def monte_carlo_integral(f, a, b, n_points=10000):
    x_rand = np.random.uniform(a, b, n_points)
    y_rand = f(x_rand)

    integral_estimate = (b - a) * np.mean(y_rand)
    return integral_estimate

a = 0
b = 2
n_points = 100000

mc_result = monte_carlo_integral(f, a, b, n_points)
print(f"Обчислення інтегралу через метод Монте-Карло: {mc_result}")

result, error = spi.quad(f, a, b)

print(f"Точкий інтеграл (quad): {result}, з оціночною похибкою {error}")
