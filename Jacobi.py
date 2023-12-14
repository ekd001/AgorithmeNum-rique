import numpy as np

def jacobi_iteration(A, b, x0=None, tol=1e-6, max_iter=1000):
    """
    Résout un système linéaire Ax = b par la méthode itérative de Jacobi.

    :param A: Matrice du système linéaire.
    :param b: Vecteur du côté droit du système linéaire.
    :param x0: Vecteur initial (optionnel, par défaut, utilise un vecteur nul).
    :param tol: Tolérance pour la convergence.
    :param max_iter: Nombre maximal d'itérations.
    :return: Vecteur x, solution du système linéaire.
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)

    x = np.copy(x0)

    for _ in range(max_iter):
        x_new = np.zeros(n)

        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sigma) / A[i, i]

        # Vérifier la convergence en comparant la différence entre les itérations successives
        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = np.copy(x_new)

    # Si le nombre maximal d'itérations est atteint sans convergence
    raise ValueError("La méthode de Jacobi n'a pas convergé.")

# Exemple d'utilisation
A = np.array([[1, 4, 4],
              [4, 1, 4],
              [4, 4, 1]])

b = np.array([1,1,7])

vecteur_initial = np.zeros(len(b))
s = jacobi_iteration(A, b, x0=vecteur_initial)
def solution(solution):
    return print(f"La solution du système linéaire est approximativement : X = {solution}")
def Jacobi():
    solution(s)