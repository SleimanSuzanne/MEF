h = 0.05; //Taille caractéristique des éléménts
l = 1; //longueur du sous marin

Point(1) = {0,0,0,h};

//Ellipse
R1 = 1;
R2 = 0.5;
Point(2) = {-R1,0,0,h};
Point(3) = {0, R2,0,h};
Point(4) = {R1,0,0,h};
Point(5) = {0,-R2,0,h};

Ellipse(1) = {2,1,2,3};
Ellipse(2) = {3,1,2,4};
Ellipse(3) = {4,1,2,5};
Ellipse(4) = {5,1,2,2};

Line Loop(1) = {1,2,3,4};

//sous marin
Point(6) = {-3*l/16, l/16, 0, h};   // Construction des points
Point(7) = {l/4, l/16, 0, h};
Point(8) = {l/4, 0, 0, h};
Point(9) = {l/4, -l/16, 0, h};
Point(10) = {-l/4, -l/16, 0, h};
Point(11) = {-l/4, 0, 0, h};
Point(12) = {-l/2, 0, 0, h};
Point(13) = {5*l/16, 0, 0, h};

Point(14) = {-l/16,l/16,0,h}; 
Point(15) = {-l/8,l/16,0,h}; 


Point(16) = {-5*l/32,1/8,0,h};
Point (28) ={-3*l/32,1/8,0,h};

Line(6) = {9,10};  
//Cercle droit
Circle(7) = {7,8,13};
Circle(8) = {13,8,9};
//Cercle gauche
Ellipse(9) = {10,11,10,12};
Ellipse(10) = {12,11,10,6};

//Cercle haut 
// Circle(11) = {6,15,16};
// Circle(12) = {16,15,14};
Spline(23)={6,16,28,14};

//fenetre gauche
Point(17) = {-l/4,l/32,0,h};
Point(18) = {-7*l/32, 0,0,h};
Point(19) = {-l/4,-l/32,0,h};
Point(20) = {-9*l/32, 0,0,h};

Circle(13) = {17,11,18};
Circle(14) = {18,11,19};
Circle(15) = {19,11,20};
Circle(16) = {20,11,17};

//fenetre droite
Point(21) = {0,l/32,0,h};
Point(22) = {l/32,0,0,h};
Point(23) = {0,-l/32,0,h};
Point(24) = {-l/32,0,0,h};

Circle(17) = {21,1,22};
Circle(18) = {22,1,23};
Circle(19) = {23,1,24};
Circle(20) = {24,1,21};

//arriere
Point(25) = {3*l/16, l/16, 0, h};
Point(26)={3*l/16 + l/32, 2*l/16,0,h};
Point(27) = {l/4 + l/64, 2*l/16,0,h};

Spline(21) = {25,26,27,7};
Line(5) = {14,25}; 
Line(22) = {25,7};

Line Loop(2) = {5,21,7,8,6,9,10,23};  



Plane Surface(1) = {1,2}; 
Physical Surface(1) = {1,2};
//bord ext tag = 1
Physical Line(1) = {1,2,3,4};
//bord ext tag = 2 
Physical Line(2) = {5,6,7,8,9,10,23,21};


