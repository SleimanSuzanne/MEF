h = 1; //Taille caractéristique des éléménts
Point(1) = {0, 10, 0, h};   // Construction des points
Point(2) = {20, 10, 0, h};
Point(3) = {20, 0, 0, h};
Point(4) = {20, -10, 0, h};
Point(5) = {0, -10, 0, h};
Point(6) = {0, 0, 0, h};
Point(7) = {-10, 0, 0, h};
Point(8) = {30, 0, 0, h};

Line(1) = {1,2};  
Line(2) = {4,5};  

//Cercle droit
Circle(3) = {2,3,8};
Circle(4) = {8,3,4};
//Cercle gauche
Circle(5) = {5,6,7};
Circle(6) = {7,6,1};

Line Loop(1) = {1,3,4,2,5,6};  


Plane Surface(1) = {1}; 

