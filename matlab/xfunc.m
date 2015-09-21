function f = xfunc(para)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
parax=para(1);
paray=para(2);
paraz=para(3);
L1=para(4);
L2=para(5);
L3=para(6);
a=para(7);
b=para(8);
c=para(9);
parax=para(1);
paray=para(2);
paraz=para(3);
f=L1*cos(parax) - c*sin(parax) + a*(cos(parax)*cos(paray)*cos(paraz) - cos(parax)*sin(paray)*sin(paraz)) + b*(cos(parax)*cos(paray)*sin(paraz) + cos(parax)*cos(paraz)*sin(paray)) + L2*cos(parax)*cos(paray) + L3*cos(parax)*cos(paray)*cos(paraz) - L3*cos(parax)*sin(paray)*sin(paraz);



end










