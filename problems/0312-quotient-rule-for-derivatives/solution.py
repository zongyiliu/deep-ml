import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g = np.poly1d(g_coeffs)
    h = np.poly1d(h_coeffs)

    g_x = g(x)
    h_x = h(x)
    g_prime_x = np.polyder(g)(x)
    h_prime_x = np.polyder(h)(x)

    return float(
        (g_prime_x * h_x - g_x * h_prime_x) / h_x**2
    )