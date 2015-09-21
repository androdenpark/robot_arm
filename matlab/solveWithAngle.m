function [ point ] = solveWithAngle(robotPara , angles)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
a=robotPara(1);
b=robotPara(2);
c=robotPara(3);
L1=robotPara(4);
L2=robotPara(5);
L3=robotPara(6);

COSX=cosd(angles(:,1));
SINX=sind(angles(:,1));

COSY=cosd(angles(:,2));
SINY=sind(angles(:,2));

COSZ=cosd(angles(:,3));
SINZ=sind(angles(:,3));

x=b*(COSX.*COSY.*SINZ + COSX.*COSZ.*SINY) - a*(COSX.*SINY.*SINZ - COSX.*COSY.*COSZ) + L1*COSX - c*SINX + L2*COSX.*COSY + L3*COSX.*COSY.*COSZ - L3*COSX.*SINY.*SINZ;
y=a*(COSY.*COSZ.*SINX - SINX.*SINY.*SINZ) + b*(COSY.*SINX.*SINZ + COSZ.*SINX.*SINY) + L1*SINX + c*COSX + L2*COSY.*SINX + L3*COSY.*COSZ.*SINX - L3*SINX.*SINY.*SINZ;
z=b*(COSY.*COSZ - SINY.*SINZ) - a*(COSY.*SINZ + COSZ.*SINY) - L2*SINY - L3*COSY.*SINZ - L3*COSZ.*SINY; 

point=[x y z];
end