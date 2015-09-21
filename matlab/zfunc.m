function f = zfunc(para)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
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

f=b*(cos(paray)*cos(paraz) - sin(paray)*sin(paraz)) - a*(cos(paray)*sin(paraz) + cos(paraz)*sin(paray)) - L2*sin(paray) - L3*cos(paray)*sin(paraz) - L3*cos(paraz)*sin(paray);



end