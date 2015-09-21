
function [ point ] = drawBall(robotPara)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
a=robotPara(1);
b=robotPara(2);
c=robotPara(3);
L1=robotPara(4);
L2=robotPara(5);
L3=robotPara(6);


dotVector=[0:3:359];

COSX=cosd(dotVector);
SINX=sind(dotVector);

COSY=cosd(dotVector);
SINY=sind(dotVector);

COSZ=cosd(dotVector);
SINZ=sind(dotVector);

[COSX COSY COSZ]=meshgrid(COSX, COSY, COSZ);
[SINX SINY SINZ]=meshgrid(SINX, SINY, SINZ);

x=b*(COSX.*COSY.*SINZ + COSX.*COSZ.*SINY) - a*(COSX.*SINY.*SINZ - COSX.*COSY.*COSZ) + L1*COSX - c*SINX + L2*COSX.*COSY + L3*COSX.*COSY.*COSZ - L3*COSX.*SINY.*SINZ;
y=a*(COSY.*COSZ.*SINX - SINX.*SINY.*SINZ) + b*(COSY.*SINX.*SINZ + COSZ.*SINX.*SINY) + L1*SINX + c*COSX + L2*COSY.*SINX + L3*COSY.*COSZ.*SINX - L3*SINX.*SINY.*SINZ;
z=b*(COSY.*COSZ - SINY.*SINZ) - a*(COSY.*SINZ + COSZ.*SINY) - L2*SINY - L3*COSY.*SINZ - L3*COSZ.*SINY; 

len=length(COSX);

COSX=[];
SINX=[];

COSY=[];
SINY=[];

COSZ=[];
SINZ=[];

for index=1:len
    [indexX indexY indexZ]=filterPoints([1 0 0 0], x(:,:,index), y(:,:,index), z(:,:,index));
    surf(indexX, indexY, indexZ);
    hold on;
end

end


function [x y z]=filterPoints(thePlane, pointX, pointY, pointZ)
[m n]=size(pointX);
x=pointX;
y=pointY;
z=pointZ;
pointForOverride=[];
for indexM=1:m
    for indexN=1:n
        if thePlane(1)*pointX(indexM, indexN)+thePlane(2)*pointY(indexM, indexN)+thePlane(3)*pointZ(indexM, indexN)+thePlane(4)>0
            pointForOverride=[x(indexM, indexN) y(indexM, indexN) z(indexM, indexN)];
            break;
        end
    end
    
    if ~isempty(pointForOverride)
        break;
    end
end
        
        
        
for indexM=1:m
    for indexN=1:n
        if thePlane(1)*pointX(indexM, indexN)+thePlane(2)*pointY(indexM, indexN)+thePlane(3)*pointZ(indexM, indexN)+thePlane(4)<0
            x(indexM, indexN)=pointForOverride(1);
            y(indexM, indexN)=pointForOverride(2);
            z(indexM, indexN)=pointForOverride(3);
        end
    end
end

end

