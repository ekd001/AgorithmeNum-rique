from data import  *

def Dichotomie(a,b):
    # Vérifier que f(a) et f(b) ont des signes opposés
    if function(a) * function(b) > 0:
        print("Methode de dichotomie,la solution n'existe pas sur l'intervalle mais après subdivision de l'intervalle on peut ou ne pas avoir une solution")

    # Initialiser la valeur de la racine
    c = (a + b) / 2

    # Itérer jusqu'à ce que la tolérance soit atteinte
    i = 0
    while (abs(b-a) > epslon):
        # Mettre à jour l'intervalle [a, b]
        if function(c) * function(a) < 0:
            b = c
        else:
            a = c

        # Recalculer la nouvelle valeur de c
        c = (a + b) / 2
        i = i + 1


    print(f"Pour dichotomie, la solution est : {c} Pour {i} itérations")

