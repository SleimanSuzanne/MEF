import numpy as np

def lecture_fichier(file):
	f = open(file, "r")
	lignes=f.readlines()
	i=4
	nodes=[]
	nbNodes=0
	triangle=[]
	segment=[]
	# ajout des bords, en fct du tag  
	bordext = [] #gamma inf
	bordint = []
	while i<len(lignes)-1:
		if i==4:
			tmp=lignes[i].rstrip('\n\r').split(" ")
			nbNodes = int(float(tmp[0]))
		elif i>4 and i<nbNodes+5:
			donnees = lignes[i].rstrip('\n\r').split(" ")
			nodes.append([(float(donnees[1])), (float(donnees[2])),0])
		elif i==nbNodes+7: #Connectivite
			nbElements = int(float(lignes[i]))
		elif i>nbNodes+7:
			donnees = lignes[i].rstrip('\n\r').split(" ")
			if int(float(donnees[1]))==1:
				segment.append([int(float(donnees[-2])), int(float(donnees[-1]))])
				tag = int(float(donnees[3]))
				if tag ==1:# or tag ==2 or tag ==3 or tag == 4:
					bordext.append([int(float(donnees[-2])), int(float(donnees[-1]))])
				elif tag == 2:# or tag == 6 or tag ==7 or tag ==8:
					bordint.append([int(float(donnees[-2])), int(float(donnees[-1]))])
				else:
					print("tag inconnu")
			elif int(float(donnees[1]))==2:
				triangle.append([int(float(donnees[-3])), int(float(donnees[-2])), int(float(donnees[-1]))])
			else:
				print("pas un triangle ni segment dans connectivite")
		i=i+1
	return nodes, nbNodes, segment, triangle, bordext, bordint

#pts, s, t, be, bi = lecture_fichier("carre_bord.msh")

def ecriture_paraview(triangle, points, segment, u, output):
	f = open(output, "w")
	f.write('<VTKFile type="UnstructuredGrid" version="1.0" byte_order="LittleEndian" header_type="UInt64">\n<UnstructuredGrid>\n')
	f.write('<Piece NumberOfPoints="'+str(len(points))+'" NumberOfCells="'+str(len(triangle))+'">\n')
	f.write('<Points>\n<DataArray NumberOfComponents="3" type="Float64">\n')
	for i in range(len(points)):
		f.write(str(points[i][0])+' '+str(points[i][1])+' 0.0\n')
	f.write('</DataArray>\n</Points>\n<Cells>\n<DataArray type="Int32" Name="connectivity">\n')
	for i in range(len(triangle)):
		f.write(str(triangle[i][0]-1)+' '+str(triangle[i][1]-1)+' '+str(triangle[i][2]-1)+'\n')
	f.write('</DataArray>\n<DataArray type="Int32" Name="offsets">\n')
	j=0
	for i in range(len(triangle)):
		j=j+3
		f.write(str(j)+'\n')
	f.write('</DataArray>\n<DataArray type="UInt8" Name="types">\n')
	for i in range(len(triangle)):
		f.write('5\n')
	f.write('</DataArray>\n</Cells>\n<PointData Scalars="solution">\n<DataArray type="Float64" Name="Real part" format="ascii">\n')
	for i in u:
		f.write(str(np.real(i))+'\n')
	f.write('</DataArray>\n<DataArray type="Float64" Name="Imag part" format="ascii">\n')
	for i in u:
		f.write(str(np.imag(i))+'\n')
	f.write('</DataArray>\n</PointData>\n</Piece>\n</UnstructuredGrid>\n</VTKFile>')
	f.close()