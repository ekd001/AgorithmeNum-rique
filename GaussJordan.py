def gauss_jordan_elimination(matrix):
    # Implémentation de la méthode de Gauss-Jordan pour résoudre un système linéaire

    # Étape 1 : Conversion de la matrice en une forme échelonnée réduite
    for i in range(len(matrix)):
        # Pivotisation partielle : recherche du pivot maximum
        max_row = max(range(i, len(matrix)), key=lambda x: abs(matrix[x][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Normalisation de la ligne du pivot
        pivot = matrix[i][i]
        for j in range(len(matrix[i])):
            matrix[i][j] /= pivot

        # Élimination des autres lignes
        for k in range(len(matrix)):
            if k != i:
                factor = matrix[k][i]
                for j in range(len(matrix[i])):
                    matrix[k][j] -= factor * matrix[i][j]

    return matrix

def gaussJordan(matrix):
    # Afficher la solution du système linéaire
    s = [0]*len(matrix)
    for i in range(len(matrix)):
        s[i] = matrix[i][-1]
    print("Methode de Gauss-Jordan la solution X =",s)

# Exemple d'utilisation
system_matrix = [
    [1, 4, 4, 1],
    [4, 1, 4, 1],
    [4, 4, 1, 7]
]

def solution():
    return  gauss_jordan_elimination(system_matrix)

