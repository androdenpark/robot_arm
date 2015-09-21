function [ pointAngle ] = solveAngleByPoints( robot,point )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
%point=[x y z];
%robot=[a b c L1 L2 L3]
a=robot(1);
b=robot(2);
c=robot(3);
L1=robot(4);
L2=robot(5);
L3=robot(6);

Px=point(1);
Py=point(2);
Pz=point(3);

Para1=-Px;
Para2=Py;
Para3=c;

%tempAngle=asin(checkResults(Para1/((Para1^2+Para2^2)^(1/2))));
%xValue=acos(checkResults(Para3/((Para1^2+Para2^2)^(1/2))));
%xValue=mod([xValue+tempAngle 2*pi-xValue-tempAngle],2*pi);

xValue=mod(dealSin(Para1,Para2,Para3),2*pi);

XSIN=sin(xValue);
XCOS=cos(xValue);
CONS=(L3^2+ a^2+ b^2+ 2*L3*a-(L1^2 + Pz^2 + L2^2+ Px^2))*ones(1,length(xValue))/2;

Para1=(L2*Pz)*ones(1,length(xValue));
Para2=(L1*L2*ones(1,length(xValue)) - L2*Px*XCOS- L2*Py*XSIN);
Para3=CONS+ L1*Px*XCOS+ L1*Py*XSIN - Px*Py*XCOS.*XSIN;

%tempAngle=asin(checkResults(Para1./((Para1.^2+Para2.^2).^(1/2))));
%yValue=acos(checkResults(Para3./((Para1.^2+Para2.^2).^(1/2))));
%yValue=mod([yValue+tempAngle;2*pi*ones(1,length(xValue))-yValue-tempAngle],2*pi);
yValue=mod([dealSin(Para1(1),Para2(1),Para3(1));dealSin(Para1(2),Para2(2),Para3(2))], 2*pi);


YSIN=sin(yValue);
YCOS=cos(yValue);

Para1=b*ones(2,length(xValue));
Para2=(L3+a)*ones(2,length(xValue));
Para3=YCOS.*(Px*[XCOS' XCOS'] - L1*ones(2,length(xValue)) + Py*[XSIN' XSIN']) - Pz*YSIN - L2*ones(2,length(xValue));

%tempAngle=asin(checkResults(Para1./((Para1.^2+Para2.^2).^(1/2))));
%zValue=acos(checkResults(Para3./((Para1.^2+Para2.^2).^(1/2))));
%zValue=mod([zValue+tempAngle;2*pi*ones(2,length(xValue))-zValue-tempAngle],2*pi);
zValue=mod([dealSin(Para1(1,1),Para2(1,1),Para3(1,1));dealSin(Para1(1,2),Para2(1,2),Para3(1,2));
    dealSin(Para1(2,1),Para2(2,1),Para3(2,1));dealSin(Para1(2,2),Para2(2,2),Para3(2,2))], 2*pi);



pointAngle=[xValue(1) yValue(1,1) zValue(1,1);xValue(1) yValue(1,1) zValue(1,2);
    xValue(1) yValue(1,2) zValue(2,1);xValue(1) yValue(1,2) zValue(2,2);
    xValue(2) yValue(2,1) zValue(3,1);xValue(2) yValue(2,1) zValue(3,2);
    xValue(2) yValue(2,2) zValue(4,1);xValue(2) yValue(2,2) zValue(4,2)]

pointAngle=(180/pi)*[xValue(1) yValue(1,1) zValue(1,1);xValue(1) yValue(1,1) zValue(1,2);
    xValue(1) yValue(1,2) zValue(2,1);xValue(1) yValue(1,2) zValue(2,2);
    xValue(2) yValue(2,1) zValue(3,1);xValue(2) yValue(2,1) zValue(3,2);
    xValue(2) yValue(2,2) zValue(4,1);xValue(2) yValue(2,2) zValue(4,2)];


pointAngle=checkPoints(robot, pointAngle, point);

end




function [y]=checkResults(acosValue)
[m n]=find(abs(acosValue)>1);
len=length(m);
for index=1:len
    acosValue(m(index),n(index))=NaN;
end
y=acosValue;
end


function [y]=checkPoints(robot, pointAngles, point)
pointMat=solveWithAngle(robot, pointAngles);
x0=point(1);
y0=point(2);
z0=point(3);
y=[];

[m n]=size(pointMat);

for index=1:m
    pointForCheck=pointMat(index,:);
    if (pointForCheck(1)-x0)^2+(pointForCheck(2)-y0)^2+(pointForCheck(3)-z0)^2 < 10 
        y=[y;pointAngles(index,:)];
    end
end

end


function [y]=dealSin(Para1,Para2,Para3)
%Para1*sin(x)+Para2*cos(x)=Para3

para1Arientation=round(Para1/abs(Para1));
para2Arientation=round(Para2/abs(Para2));
%make sure the serTa value is always between 0~pi/2 %
serTa=acos(checkResults((para2Arientation*Para2/((Para1^2+Para2^2)^(1/2)))));
% the acos value is always between 0~`pi %
equtionAsu=acos(checkResults((para2Arientation*Para3)/((Para1^2+Para2^2)^(1/2))));

baseAus=equtionAsu+(para2Arientation*para1Arientation)*serTa;
anotherAus=2*pi-equtionAsu+(para2Arientation*para1Arientation)*serTa;

y=[baseAus anotherAus];

end

