function [x y z theX theY theZ] = findLinePoints( robotPara, pointMatrics)

a=robotPara(1);
b=robotPara(2);
c=robotPara(3);
L1=robotPara(4);
L2=robotPara(5);
L3=robotPara(6);

pointsRange=[0:359];

len=length(pointsRange);

one=0;
two=0;
three=0;

for one=1:len
    theX=pointsRange(one);
    COSX=cosd(pointsRange(one));
    SINX=sind(pointsRange(one));
    for two=1:len
        theY=pointsRange(two);
        COSY=cosd(pointsRange(two));
        SINY=sind(pointsRange(two));
        for three=1:len
            theZ=pointsRange(three);
            COSZ=cosd(pointsRange(three));
            SINZ=sind(pointsRange(three));
            x=b*(COSX.*COSY.*SINZ + COSX.*COSZ.*SINY) - a*(COSX.*SINY.*SINZ - COSX.*COSY.*COSZ) + L1*COSX - c*SINX + L2*COSX.*COSY + L3*COSX.*COSY.*COSZ - L3*COSX.*SINY.*SINZ;
            y=a*(COSY.*COSZ.*SINX - SINX.*SINY.*SINZ) + b*(COSY.*SINX.*SINZ + COSZ.*SINX.*SINY) + L1*SINX + c*COSX + L2*COSY.*SINX + L3*COSY.*COSZ.*SINX - L3*SINX.*SINY.*SINZ;
            z=b*(COSY.*COSZ - SINY.*SINZ) - a*(COSY.*SINZ + COSZ.*SINY) - L2*SINY - L3*COSY.*SINZ - L3*COSZ.*SINY; 

            deltaX=abs(x-pointMatrics(1));
            deltaY=abs(y-pointMatrics(2));
            deltaZ=abs(z-pointMatrics(3));

            if deltaX<0.5 & deltaZ<0.5 & deltaY>50
               return
            end 
        end
    end
end

end
