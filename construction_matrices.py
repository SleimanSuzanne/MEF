import numpy as np
from numpy import array
from scipy.sparse import coo_matrix


def uinc(x,y):
    alpha=np.pi
    k=2*np.pi
    uinc=np.exp(np.complex(0,1)*k*(x*np.cos(alpha)+y*np.sin(alpha)))
    return uinc

#Conditions de dirichlet - modifie A et b avec les conditions de dirichlet 

class calc:
	def __init__(self,triangle, points, segment, bordgaminf, bordgam):
		self.triangle = triangle
		self.segment = segment
		self.nodes = points
		self.bordext = bordgaminf
		self.bordint = bordgam
		self.b=np.zeros(len(points))
	def matM(self):
		k=4*np.pi/15
		n=np.asarray(self.nodes)
		nbnodes = len(self.nodes)
		row=[]
		col=[]
		data=[]
		Mep=[[2,1,1],[1,2,1],[1,1,2]]
		for i in range(3):
			for j in range(3):
				Mep[i][j]=Mep[i][j]*(1./24.)*(k**2)
		C=np.zeros((nbnodes, nbnodes))
		Cep=[[2,1],[1,2]]
		for i in range(2):
			for j in range(2):
				Cep[i][j]=Cep[i][j]*np.complex(0,1)*(k)*(1./6.)*(-1) #np.complex : i 

		for s in range(len(self.bordext)):
			sigma=np.linalg.norm(np.asarray(self.nodes[self.bordext[s][0]-1])-np.asarray(self.nodes[self.bordext[s][1]-1]))
			for i1 in range(2):
				I=self.bordext[s][i1]-1
				for j1 in range(2):
					J=self.bordext[s][j1]-1	
					row.append(I);
					col.append(J);
					val= Cep[i][j]*sigma
					data.append(val)
		for p in range(len(self.triangle)):
			P1=(n[self.triangle[p][1]-1][0]-n[self.triangle[p][0]-1][0])*(n[self.triangle[p][2]-1][1]-n[self.triangle[p][0]-1][1])
			P2=(n[self.triangle[p][2]-1][0]-n[self.triangle[p][0]-1][0])*(n[self.triangle[p][1]-1][1]-n[self.triangle[p][0]-1][1])
			aire=abs(P1-P2)
			for i in range(3):
				I=self.triangle[p][i]-1
				for j in range(3):
					J=self.triangle[p][j]-1	
					row.append(I);
					col.append(J);
					val= Mep[i][j]*aire
					data.append(val)

		self.M = coo_matrix((data, (row, col)), shape=(nbnodes, nbnodes)).tocsr()

	def matD(self):
		nbnodes = len(self.nodes)
		#D=np.zeros((nbnodes, nbnodes))
		Dep=[[2,-1,-1],[-1,1,0],[-1,0,1]]
		for i in range(3):
			for j in range(3):
				Dep[i][j]=Dep[i][j]*(1./2.)*(-1)
	
		n=np.asarray(self.nodes)
		row=[]
		col=[]
		data=[]
		for p in range(len(self.triangle)):
			P1D=(n[self.triangle[p][1]-1][0]-n[self.triangle[p][0]-1][0])*(n[self.triangle[p][2]-1][1]-n[self.triangle[p][0]-1][1])
			P2D=(n[self.triangle[p][2]-1][0]-n[self.triangle[p][0]-1][0])*(n[self.triangle[p][1]-1][1]-n[self.triangle[p][0]-1][1])
			aireD=abs(P1D-P2D)
			for i in range(3):
				I=self.triangle[p][i]-1
				for j in range(3):
					J=self.triangle[p][j]-1	
					row.append(I);
					col.append(J);
					val= Dep[i][j]*aireD
					data.append(val)
		self.D = coo_matrix((data, (row, col)), shape=(nbnodes, nbnodes)).tocsr()

	def Dirichlet(self):
		self.b=np.zeros(len(self.nodes),np.complex128)
		self.A = self.M+self.D
		self.A=self.A.toarray()
		for i in range(len(self.segment)):
			self.b[self.segment[i][0]-1]=-uinc(self.nodes[self.segment[i][0]-1][0],self.nodes[self.segment[i][0]-1][1])
			self.b[self.segment[i][1]-1]=-uinc(self.nodes[self.segment[i][1]-1][0],self.nodes[self.segment[i][1]-1][1])
			self.A[self.segment[i][0]-1,:]=0
			self.A[self.segment[i][1]-1,:]=0
			self.A[:,self.segment[i][0]-1]=0
			self.A[:,self.segment[i][0]-1]=0
			self.A[self.segment[i][0]-1,self.segment[i][0]-1]=1
			self.A[self.segment[i][1]-1,self.segment[i][1]-1]=1

	def solve_eq(self):
		self.u = np.linalg.solve(self.A, self.b)
