import numpy as np
from numpy import array
from scipy.sparse import coo_matrix

from lecture_ecriture_fichier import ecriture_paraview, lecture_fichier
from construction_matrices import calc, verifMD_test

nom_data = "cercle"

chemin_data = "data/" + nom_data + ".msh"
chemin_output = "output/" + nom_data + ".vtu"
#Lecture du fichier gmsh et extraction des elements connectivite 
nodes, nbNodes, segment, triangle, bordext, bordint = lecture_fichier(chemin_data)
E = calc(triangle, nodes, segment, bordext, bordint)

#param
nlambda=15
h=0.1
k=(2*np.pi)/(h*nlambda)
E.matM()
E.matMbord()
E.matD()
E.constructA(k)
E.Dirichlet(k)
E.solve_eq(k)


# [Verif1, Verif2] = verifMD_test((E.M).toarray(),(E.D).toarray(), nbNodes)
# print('verif1: (devrait donner aire de omega) ')
# print(Verif1)
# print('verif2: (devrait donner 0')
# print(Verif2)

ecriture_paraview(triangle, nodes, segment, E.u, chemin_output)