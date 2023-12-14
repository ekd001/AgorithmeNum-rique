from data import *
def newton_raphson(x0, max_iter=100):
    """
    Résout une équation non linéaire f(x) = 0 par la méthode de Newton-Raphson.

    :param f: Fonction représentant l'équation à résoudre.
    :param df: Dérivée de la fonction f.
    :param x0: Point initial de départ.
    :param tol: Tolérance pour la convergence.
    :param max_iter: Nombre maximal d'itérations.
    :return: La solution approchée x.
    """
    tol = 10e-10
    x = x0
    i = 0
    for i in range(max_iter):
        x_next = x - function(x) / derivative_function(x)

        # Vérifier la convergence en comparant la différence entre les itérations successives
        if abs(x_next - x) < tol:
            break

        x = x_next

    # Si le nombre maximal d'itérations est atteint sans convergence

    print(f"Methode de newtonRaphson, la solution est: {x_next} Pour {i} itérations")
# Exemple d'utilisation



