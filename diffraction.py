import numpy as np
from numpy import array
from scipy.sparse import coo_matrix

from lecture_ecriture_fichier import ecriture_paraview, lecture_fichier
from construction_matrices import calc, verifMD_test

import time

nom_data = "sousmarin_ameliore"

chemin_data = "data/" + nom_data + ".msh"
chemin_output = "output/" + nom_data + ".vtu"
#Lecture du fichier gmsh et extraction des elements connectivite 
nodes, nbNodes, segment, triangle, bordext, bordint = lecture_fichier(chemin_data)
E = calc(triangle, nodes, segment, bordext, bordint)

#param
nlambda=15
h=0.05
k=(2*np.pi)/(h*nlambda)

f = open("temps_exe_fcts.txt", "a")

start = time.time()
E.matM()
end = time.time()

f.write( "M ; " + str(end-start) + "\n")

start = time.time()
E.matMbord()
end = time.time()

f.write("Mbord ; " + str(end-start) + "\n")

start = time.time()
E.matD()
end = time.time()
f.write("D ; " + str(end-start) + "\n")

start = time.time()
E.constructA(k)
end = time.time()
f.write("A ; " + str(end-start) + "\n")

start = time.time()
E.Dirichlet(k)
end = time.time()
f.write("Dirichlet ; " + str(end-start) + "\n")

start = time.time()
E.solve_eq(k)
end = time.time()
f.write("u ; " + str(end-start) + "\n")


f.close()


# [Verif1, Verif2] = verifMD_test((E.M).toarray(),(E.D).toarray(), nbNodes)
# print('verif1: (devrait donner aire de omega) ')
# print(Verif1)
# print('verif2: (devrait donner 0')
# print(Verif2)

ecriture_paraview(triangle, nodes, segment, E.u, chemin_output)