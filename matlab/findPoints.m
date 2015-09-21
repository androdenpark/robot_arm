function [pointCounts,pointMatrics] = findPoints( robotPara, pointsRange, platePara)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
% robotPara=[L1 L2 L3 a b c]
% pointsRange=[0:150], 0 150 meas the start and the end angle of the joints
% platePara=[a b c d]
%syms X Y Z x y z a b c L1 L2 L3;
%X=b*(cos(x)*cos(y)*sin(z) + cos(x)*cos(z)*sin(y)) - a*(cos(x)*sin(y)*sin(z) - cos(x)*cos(y)*cos(z)) + L1*cos(x) - c*sin(x) + L2*cos(x)*cos(y) + L3*cos(x)*cos(y)*cos(z) - L3*cos(x)*sin(y)*sin(z);
%Y=a*(cos(y)*cos(z)*sin(x) - sin(x)*sin(y)*sin(z)) + b*(cos(y)*sin(x)*sin(z) + cos(z)*sin(x)*sin(y)) + L1*sin(x) + c*cos(x) + L2*cos(y)*sin(x) + L3*cos(y)*cos(z)*sin(x) - L3*sin(x)*sin(y)*sin(z);
%Z=b*(cos(y)*cos(z) - sin(y)*sin(z)) - a*(cos(y)*sin(z) + cos(z)*sin(y)) - L2*sin(y) - L3*cos(y)*sin(z) - L3*cos(z)*sin(y);

%X=subs(X,{x, y, z, a, b, c, L1, L2, L3},[x y z robotPara(1) robotPara(2) robotPara(3) robotPara(4) robotPara(5) robotPara(6)]);
%Y=subs(Y,{x, y, z, a, b, c, L1, L2, L3},[x y z robotPara(1) robotPara(2) robotPara(3) robotPara(4) robotPara(5) robotPara(6)]);
%Z=subs(Z,{x, y, z, a, b, c, L1, L2, L3},[x y z robotPara(1) robotPara(2) robotPara(3) robotPara(4) robotPara(5) robotPara(6)]);

a=robotPara(1);
b=robotPara(2);
c=robotPara(3);
L1=robotPara(4);
L2=robotPara(5);
L3=robotPara(6);

pointCounts=0;
pointMatrics=[];

len=length(pointsRange);
%pointsRange=(pointsRange/360).*(2*pi);
one=0;
two=0;

fid=fopen('g:\elts.txt','a');
for one=1:len
    one
    COSX=cosd(pointsRange(one))*ones(1,len);
    SINX=sind(pointsRange(one))*ones(1,len);
    for two=1:len
        COSY=cosd(pointsRange(two))*ones(1,len);
        SINY=sind(pointsRange(two))*ones(1,len);
        %for three=1:len
            %curr=[num2str(theArray(one)) num2str(theArray(two)) num2str(theArray(three))];
            %tic;
            %curr=[(pointsRange(one)/360)*2*pi (pointsRange(two)/360)*2*pi (pointsRange(three)/360)*2*pi]; 
            COSZ=cosd(pointsRange);
            SINZ=sind(pointsRange);
            %toc;
            %pointx=subs(X,{sin(x),sin(y),sin(z),cos(x),cos(y),cos(z)},[COSX COSY COSZ SINX SINY SINZ]);
            %pointy=subs(Y,{sin(x),sin(y),sin(z),cos(x),cos(y),cos(z)},[COSX COSY COSZ SINX SINY SINZ]);
            %pointz=subs(Z,{sin(x),sin(y),sin(z),cos(x),cos(y),cos(z)},[COSX COSY COSZ SINX SINY SINZ]);
            pointx=b*(COSX.*COSY.*SINZ + COSX.*COSZ.*SINY) - a*(COSX.*SINY.*SINZ - COSX.*COSY.*COSZ) + L1*COSX - c*SINX + L2*COSX.*COSY + L3*COSX.*COSY.*COSZ - L3*COSX.*SINY.*SINZ;
            pointy=a*(COSY.*COSZ.*SINX - SINX.*SINY.*SINZ) + b*(COSY.*SINX.*SINZ + COSZ.*SINX.*SINY) + L1*SINX + c*COSX + L2*COSY.*SINX + L3*COSY.*COSZ.*SINX - L3*SINX.*SINY.*SINZ;
            pointz=b*(COSY.*COSZ - SINY.*SINZ) - a*(COSY.*SINZ + COSZ.*SINY) - L2*SINY - L3*COSY.*SINZ - L3*COSZ.*SINY;           
            %toc;
            distance=point2Plate(platePara,[pointx; pointy; pointz]);
            %toc;
            [i j]=find(distance<0.0001);
            rightLen=length(j);
            pointCounts  = pointCounts+rightLen;
            if rightLen>0
                for index=1:rightLen
                    rightPoint=[distance(j(index)) (pointsRange(one))*180/pi (pointsRange(two))*180/pi (pointsRange(j(index)))*180/pi pointx(j(index)) pointy(j(index)) pointz(j(index))];
                    pointMatrics=[pointMatrics;[pointx(j(index)) pointy(j(index)) pointz(j(index))]];
                    fprintf(fid,'%.2f %d %d %d %.2f %.2f %.2f\r\n', rightPoint);
                end
            end   
        %end       
    end
end

fclose(fid);


end

