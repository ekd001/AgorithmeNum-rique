import numpy as np


def thomas_algorithm(a, b, c, d):
    """
    Résout un système linéaire tridiagonal Ax = d par la méthode de Thomas.

    :param a: Coefficients de la diagonale inférieure (sous-diagonale).
    :param b: Coefficients de la diagonale principale.
    :param c: Coefficients de la diagonale supérieure (sur-diagonale).
    :param d: Vecteur du côté droit du système linéaire.
    :return: Vecteur x, solution du système linéaire.
    """
    n = len(d)
    c_prime = np.zeros(n - 1)
    d_prime = np.zeros(n)

    # Étape de prétraitement
    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]

    for i in range(1, n - 1):
        c_prime[i] = c[i] / (b[i] - a[i - 1] * c_prime[i - 1])

    # Étape de substitution avant
    for i in range(1, n):
        d_prime[i] = (d[i] - a[i - 1] * d_prime[i - 1]) / (b[i] - a[i - 1] * c_prime[i - 1])

    # Étape de substitution arrière
    x = np.zeros(n)
    x[-1] = d_prime[-1]

    for i in range(n - 2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i + 1]

    return x


# Exemple d'utilisation
a = np.array([4,4])  # Coefficients de la diagonale inférieure
b = np.array([1,1,1])  # Coefficients de la diagonale principale
c = np.array([4,4])  # Coefficients de la diagonale supérieure
d = np.array([1,1,7])  # Vecteur du côté droit

solution = thomas_algorithm(a, b, c, d)

print(f"La solution du système linéaire tridiagonal est : X = {solution}")
