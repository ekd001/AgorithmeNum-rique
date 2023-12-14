import numpy as np

def decomposition_LU(matrice):
    n = len(matrice)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Calcul des éléments de la matrice L
        for k in range(i+1):
            s = sum(L[i][j] * U[j][k] for j in range(k))
            L[i][k] = matrice[i][k] - s

        # Calcul des éléments de la matrice U
        for k in range(i, n):
            s = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = (matrice[i][k] - s) / L[i][i]

    return L,U

def resoudre_systeme(L, U, b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Résolution Ly = b
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]

    # Résolution Ux = y
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return x
#on utilise la méthode de croute
A = np.array([[1,4,4], [4,1,4], [4,4,1]])
b = np.array([1,1,7])

def data(A,b):
    L, U = decomposition_LU(A)
    x = resoudre_systeme(L, U, b)
    print("Pour la methode de decomposition LU : ")
    print("Matrice L:")
    print(L)
    print("\nMatrice U:")
    print(U)
    print("\nSolution du système d'équations, X =",x)
def decompositionLU():
    data(A,b)

