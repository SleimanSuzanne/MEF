import numpy as np
from numpy import array
from scipy.sparse import coo_matrix

from lecture_ecriture_fichier import ecriture_paraview, lecture_fichier
from construction_matrices import calc

#Lecture du fichier gmsh et extraction des elements connectivite 
nodes, nbNodes, segment, triangle, bordext, bordint = lecture_fichier("data/cercle.msh")
E = calc(triangle, nodes, segment, bordext, bordint)
E.matM()
E.matD()
E.Dirichlet()
E.solve_eq()

#Verification
def verif(M,D, nbpts):
	U=np.zeros((nbpts,nbpts))
	for i in range(nbpts):
		U[i][0]=1
	Ut =  np.transpose(U)
	test = (Ut.dot(M)).dot(U)
	test1=D.dot(U)
	return test, test1

[Verif1, Verif2] = verif((E.M).toarray(),(E.D).toarray(), nbNodes) #doit etre egal a aire de omega
# print('verif1: (devrait donner aire de omega) ')
# print(Verif1)
# print('verif2: (devrait donner 0')
# print(Verif2)

ecriture_paraview(triangle, nodes, segment, E.u)