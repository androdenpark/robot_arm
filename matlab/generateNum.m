function y = generateNum( theArray)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

%X=b*(cos(x)*cos(y)*sin(z) + cos(x)*cos(z)*sin(y)) - a*(cos(x)*sin(y)*sin(z) - cos(x)*cos(y)*cos(z)) + L1*cos(x) - c*sin(x) + L2*cos(x)*cos(y) + L3*cos(x)*cos(y)*cos(z) - L3*cos(x)*sin(y)*sin(z)
%Y=a*(cos(y)*cos(z)*sin(x) - sin(x)*sin(y)*sin(z)) + b*(cos(y)*sin(x)*sin(z) + cos(z)*sin(x)*sin(y)) + L1*sin(x) + c*cos(x) + L2*cos(y)*sin(x) + L3*cos(y)*cos(z)*sin(x) - L3*sin(x)*sin(y)*sin(z)
%Z=b*(cos(y)*cos(z) - sin(y)*sin(z)) - a*(cos(y)*sin(z) + cos(z)*sin(y)) - L2*sin(y) - L3*cos(y)*sin(z) - L3*cos(z)*sin(y)


a=theArray;
b=theArray;
c=theArray;
len=length(a);
one=0;
two=0;
three=0;

fid=fopen('g:\tst.txt','a');
for one=1:len
    one
    for two=1:len
        for three=1:len
            %curr=[num2str(theArray(one)) num2str(theArray(two)) num2str(theArray(three))];
            curr=[(theArray(one)) (theArray(two)) (theArray(three))]; 
            X=
            fprintf(fid,'%d %d %d \r\n',curr);
        end
    end
end

fclose(fid);



end

