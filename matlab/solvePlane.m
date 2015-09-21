function paraAus = solvePlane(point1,point2, point3 )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
% point1 point1 point1 defines three points in a defined plane
% the Plate is defined as x+paraAus(1)*y+paraAus(2)*z+paraAus(3)=0

ParaMatrics=[point1(2) point1(3) 1;point2(2) point2(3) 1;point3(2) point3(3) 1];
consMatrics=[-point1(1);-point2(1);-point3(1)];
paraAus=inv(ParaMatrics)*consMatrics;
end

