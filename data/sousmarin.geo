h = 2; //Taille caractéristique des éléménts

// stade
Point(1) = {-0.25, 0.125, 0, h};   // Construction des points
Point(2) = {0.25, 0.125, 0, h};
Point(3) = {0.25, 0, 0, h};
Point(4) = {0.25, -0.125, 0, h};
Point(5) = {-0.25, -0.125, 0, h};
Point(6) = {-0.25, 0, 0, h};
Point(7) = {-0.5, 0, 0, h};
Point(8) = {0.375, 0, 0, h};

Point(9) = {0,0.125,0,h}; 
Point(10) = {-0.125,0.125,0,h}; 
Point(11) = {-0.125,0.25,0,h};

Point(12) = {0,0,0,h};

Line(1) = {9,2};  
Line(2) = {4,5};  

//Cercle droit
Circle(3) = {2,3,8};
Circle(4) = {8,3,4};
//Cercle gauche
Ellipse(5) = {5,6,5,7};
Ellipse(6) = {7,6,5,1};

//Cercle haut 
Circle(7) = {1,10,11};
Circle(8) = {11,10,9};

Line Loop(1) = {1,3,4,2,5,6,7,8};  

//Ellipse
Point(13) = {-2.5,0,0,h};
Point(14) = {0, 1.5,0,h};
Point(15) = {2.5,0,0,h};
Point(16) = {0,-1.5,0,h};

Ellipse(9) = {13,12,13,14};

Ellipse(10) = {14,12,13,15};

Ellipse(11) = {15,12,13,16};

Ellipse(12) = {16,12,13,13};

Line Loop(2) = {9,10,11,12};


Plane Surface(1) = {1,2}; 
Physical Surface(1) = {1,2};
//bord ext tag = 1
Physical Line(1) = {9,10,11,12};
//bord ext tag = 2 
Physical Line(2) = {1,2,3,4,5,6,7,8};


