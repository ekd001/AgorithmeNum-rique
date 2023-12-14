def gauss_elimination(A, B):
    n = len(A)

    # Étape d'élimination directe
    for i in range(n):
        # Étape de pivotage partiel
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        # Élimination
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]

    # Étape de remontée
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            B[k] -= A[k][i] * X[i]

    return X

# Exemple d'utilisation
def gauss(A,B):
    print("Methode de Gauss la solution est X =",gauss_elimination(A,B))

