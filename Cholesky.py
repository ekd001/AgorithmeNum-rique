import numpy as np

def cholesky_decomposition(matrix):
    """
    Effectue la décomposition de Cholesky d'une matrice symétrique définie positive.

    :param matrix: Matrice symétrique définie positive.
    :return: Matrice L, telle que matrix = LL^T.
    """
    n = len(matrix)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i, i] = np.sqrt(matrix[i, i] - np.sum(L[i, :]**2))
            else:
                L[i, j] = (matrix[i, j] - np.sum(L[i, :] * L[j, :])) / L[j, j]

    return L

# Exemple d'utilisation
matrix = np.array([[1, 4, 4],
                   [4, 1, 4],
                   [4, 4, 1]])

cholesky_matrix = cholesky_decomposition(matrix)

print("Matrice d'origine :\n", matrix)
print("\nMatrice de décomposition de Cholesky (L) :\n", cholesky_matrix)
