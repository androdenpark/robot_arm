function y = fs3steep( f, e, a, b )
%fs2steep function :
% f is the function, e is toralable error, (a, b) is the start point

x1=a;
x2=b;
Q=fs2hesse(f, x1, x2);
x0=[x1, x2]';
fx1=diff(f, 'x1');
fx2=diff(f, 'x2');
g=[fx1 fx2]';
g1=subs(g);
d=-g1;
while (abs(norm(g1))>=e)
    t=(-d)'*d/((-d)'*Q*d)
    x0=x0-t*g1;
    v=x0;
    getFunctionValue(x0(1), x0(2));
    a=[1 0]*x0;
    b=[0 1]*x0;
    x1=a;
    x2=b;
    Q=fs2hesse(f, x1, x2);
    x0=[x1 x2]';
    fx1=diff(f, 'x1');
    fx2=diff(f, 'x2');
    g=[fx1 fx2]';
    g1=subs(g);
    d=-g1;
end;
y=v;
end


function x=fs2hesse(f, a, b)
%fs2hesse is used to get the matrix of the 'f' function

x1=a;
x2=b;
fx=diff(f, 'x1');
fy=diff(f, 'x2');
fxx=diff(fx, 'x1');
fxy=diff(fx, 'x2');
fyx=diff(fy, 'x1');
fyy=diff(fy, 'x2');
fxx=subs(fxx);
fxy=subs(fxy);
fyx=subs(fyx);
fyy=subs(fyy);
x=[fxx, fxy; fyx, fyy];
    


end
function y=getFunctionValue(x1, x2)
y=2*(x2 - 4)^2 + (x1 - 7)^2 + 3;
end



