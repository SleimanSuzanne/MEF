# MEF
Projet maillage Elements Finis, diffraction ondes
Réalisé avec Isma Bentoumi (Isma04) - Hiver 2018/2019 - MAIN5 Polytech Sorbonne

Dossiers:
  - data: contient les fichiers .msh (et les .geo à partir des quels ils sont générés)
  - output: fichiers .vtu après avoir lancé diffraction.py 
  
 Fichiers:
  - "lecture_ecriture_fichier.py" : contient 2 fonctions
        - "lecture_fichier(*.msh)" : prend un entrée un fichier .msh et retourne les noeuds, segments, triangles 
        - "ecriture_paraview()" qui écrit le fichier .vtu dans le dossier output pour visualiser u 
  - "construction_matrices.py" : contient 2 fonctions et une classe:
        - "uinc()" : définit l'onde incidente 
        - "verifMD_test()" : fais 2 tests sur les matrices M et D 
        - classe calc: contient plusieurs fonctions pour construire les matrices de rigidité (matD), de masse (matM) et de 
          masse de bord (matMbord), la matrice A finale construite à partir des matrices M, Mbord et D, une fonction Dirichlet 
          pour définir les conditions de Dirichlet sur les matrices A et b, et solve_eq qui résoud le système et donne u
  - "diffraction.py" : appel des fonctions 
  
  
  Utilisation:
  Dans diffraction.py, dans la variable "nom_data" mettre le nom d'un fichier du dossier data (sans l'extension), ex: cercle
Lancer dans le terminal:
$python2 diffraction.py
$cd output/
$paraview cercle.vtu 

          
        
