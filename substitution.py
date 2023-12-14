
def function_mere(x):
    return pow(x,12) - 1.10
def function(x):

    return x*x + x + 1
epslon = pow(10,-10)
def Substitution():
    i = 0
    x0 = 0.5
    stop = True
    #calcul de x(n+1) = F(x(n))
    while(stop):
        s = function(x0)
        d = s - x0


        x0 = s
        if(i > 1000):
            print("Methode Substitution, la solution n'existe pas")
            break
        if((abs(d) < epslon)):
            print(f"Methode substitution, la solution est :{x0} Pour {i} itérations")


            stop = False
        i += 1

