# Programa para aproximar derivadas e integrais para funções arbitrárias numericamente.

def approx_derivative(f, x, delta=1e-6):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def approx_derivative_2(f, delta = 1e-6):
    return lambda x: (f(x + delta) - f(x - delta)) / (2 * delta)

def approx_integral(f, lo, hi, num_regions):
    h = (hi - lo) / num_regions
    regions = [(lo + i * h) for i in range(num_regions + 1)]
    results = [f(region) for region in regions]
    return (h / 2) * (results[0] + 2 * sum(results[1:-1]) + results[-1])