from data import *
def Corde(a,b,iterations):
    if((a == b) or (a > b)):
        print("a < b ou a différent de b")
        return "Pas de solution"
    x0 = a
    x1 = b
    #calcul des itérations
    for i in range(iterations):
        x_next = x1 - (function(x1) * (x1 - x0))/(function(x1)-function(x0))
        if(abs(x_next-x1) < epslon):
            break
        x0 = x1
        x1 = x_next

    #retourner le résultat
    print(f"Methode de la corde, la solution est {x_next} Pour {i} itérations")
