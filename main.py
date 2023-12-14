
from substitution import Substitution
from dichotomie import Dichotomie
from corde import Corde
from newtonRaphson import newton_raphson
from Gauss import gauss
from GaussJordan import *
from decomposition import decompositionLU
from data import *

if __name__ == "__main__":
   A = [[1,4,4],[4,1,4],[4,4,1]]
   B = [1,1,7]
   M = [[1,4,4,1],[4,1,4,1],[4,4,1,7]]

   gauss(A,B)
   gaussJordan(solution())
   decompositionLU()