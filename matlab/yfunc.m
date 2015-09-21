function f = yfunc(para)
%fs2steep function :
% f is the function, e is toralable error, (a, b) is the start point
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
f=b*(cos(paray)*sin(parax)*sin(paraz) + cos(paraz)*sin(parax)*sin(paray)) - a*(sin(parax)*sin(paray)*sin(paraz) - cos(paray)*cos(paraz)*sin(parax)) + L1*sin(parax) + c*cos(parax) + L2*cos(paray)*sin(parax) + L3*cos(paray)*cos(paraz)*sin(parax) - L3*sin(parax)*sin(paray)*sin(paraz);



end