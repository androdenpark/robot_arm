function distance = point2Plate( plate,point )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
% plate=[ a b c d ] , ax +by +cz +d =0;
% point=[x y z];
[m n]=size(point);
if m>1
    topside=plate(1)*point(1,:)+plate(2)*point(2,:)+plate(3)*point(3,:)+plate(4) * ones(1, length(point(1,:)));
else
    topside=plate(1)*point(1)+plate(2)*point(2)+plate(3)*point(3)+plate(4);
end

bottomside=(plate(1)^2+plate(2)^2+plate(3)^2)^(0.5);
distance=abs(topside)/bottomside;

end

