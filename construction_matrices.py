import numpy as np
from numpy import array
from scipy.sparse import coo_matrix


def uinc(x,y,k):
    w=[1,2,3,4,5]
    alpha=np.pi
    #ondes d'herglotz
    #uinc=0
    #for i in range(5):
    #    uinc=uinc+w[i]*np.exp(np.complex(0,1)*i*k*(x*np.cos(alpha)+y*np.sin(alpha)))
    uinc=np.exp(np.complex(0,1)*k*(x*np.cos(alpha)+y*np.sin(alpha)))
    return uinc

#Verification
def verifMD_test(M,D, nbpts):
	U=np.zeros((nbpts,nbpts))
	for i in range(nbpts):
		U[i][0]=1
	Ut =  np.transpose(U)
	test=np.matmul(np.matmul(Ut,M),U)
	test1=np.matmul(D,U)
	return test[0][0], test1


class calc:
	def __init__(self,triangle, points, segment, bordgaminf, bordgam):
		self.triangle = triangle
		self.segment = segment
		self.nodes = points
		self.bordext = bordgaminf
		self.bordint = bordgam
		self.b=np.zeros(len(points))
	def matM(self):
		n=np.asarray(self.nodes)
		nbnodes = len(self.nodes)
		row=[]
		col=[]
		data=[]
		Mep=[[2,1,1],[1,2,1],[1,1,2]]
		for i in range(3):
			for j in range(3):
				Mep[i][j]=Mep[i][j]*(1./24.)#*(k**2)
		
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

	def matMbord(self):
		row=[]
		col=[]
		data=[]
		nbnodes = len(self.nodes)
		Cep=[[2,1],[1,2]]
		for i in range(2):
			for j in range(2):
				Cep[i][j]=Cep[i][j]*(1./6.)#*np.complex(0,1)*(k)*(-1) #np.complex : i 

		for s in range(len(self.bordext)):
			sigma=np.linalg.norm(np.asarray(self.nodes[self.bordext[s][0]-1])-np.asarray(self.nodes[self.bordext[s][1]-1]))
			for i1 in range(2):
				I=self.bordext[s][i1]-1
				for j1 in range(2):
					J=self.bordext[s][j1]-1	
					row.append(I)
					col.append(J)
					val= Cep[i][j]*sigma
					data.append(val)
		self.Mbord = coo_matrix((data, (row, col)), shape=(nbnodes, nbnodes)).tocsr()


	def matD(self):
		nbnodes = len(self.nodes)	
		n=np.asarray(self.nodes)
		row=[]
		col=[]
		data=[]
		Gphi=[[-1,-1],[1,0],[0,1]]
		B=np.zeros((2,2))
		for p in range(len(self.triangle)):
			P1D=(n[self.triangle[p][1]-1][0]-n[self.triangle[p][0]-1][0])*(n[self.triangle[p][2]-1][1]-n[self.triangle[p][0]-1][1])
			P2D=(n[self.triangle[p][2]-1][0]-n[self.triangle[p][0]-1][0])*(n[self.triangle[p][1]-1][1]-n[self.triangle[p][0]-1][1])
			aireD=abs(P1D-P2D)/2
			B[0][0]=(1/(aireD*2))*((n[self.triangle[p][2]-1][1]-n[self.triangle[p][0]-1][1]))
			B[0][1]=(1/(aireD*2))*(-(n[self.triangle[p][1]-1][1]-n[self.triangle[p][0]-1][1]))
			B[1][0]=(1/(aireD*2))*(-(n[self.triangle[p][2]-1][0]-n[self.triangle[p][0]-1][0]))
			B[1][1]=(1/(aireD*2))*((n[self.triangle[p][1]-1][0]-n[self.triangle[p][0]-1][0]))
			BTB=np.matmul(np.transpose(B),B)
			for i in range(3):
				I=self.triangle[p][i]-1
				for j in range(3):
					J=self.triangle[p][j]-1	
					row.append(I);
					col.append(J);
					val= (aireD*np.matmul(np.transpose(Gphi[j]),np.matmul(BTB,Gphi[i])))
					data.append(val)
		self.D = coo_matrix((data, (row, col)), shape=(nbnodes, nbnodes)).tocsr()

	def constructA(self,k):
		self.A =  (k**2)*self.M-np.complex(0,1)*(k)*self.Mbord-self.D
		#self.A = k**2*self.M+i*k*Mbord+D
		self.A = (self.A).toarray()

	def Dirichlet(self,k):
		self.b=np.zeros(len(self.nodes),np.complex128)
		#self.A = self.M+self.D
		#self.A=self.A.toarray()
		for i in range(len(self.bordint)):
			self.b[self.bordint[i][0]-1]=-uinc(self.nodes[self.bordint[i][0]-1][0],self.nodes[self.bordint[i][0]-1][1],k)
			self.b[self.bordint[i][1]-1]=-uinc(self.nodes[self.bordint[i][1]-1][0],self.nodes[self.bordint[i][1]-1][1],k)
			self.A[self.bordint[i][0]-1,:]=0
			self.A[self.bordint[i][1]-1,:]=0
			self.A[self.bordint[i][0]-1,self.bordint[i][0]-1]=1
			self.A[self.bordint[i][1]-1,self.bordint[i][1]-1]=1

	def solve_eq(self,k):
		self.u = np.linalg.solve(self.A, self.b)
		nbnodes = len(self.nodes)
		ui=[]
		for i in range(nbnodes):
			ui.append(uinc(self.nodes[i][0],self.nodes[i][1],k))
		self.u = self.u + ui
