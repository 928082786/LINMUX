function result=formula(p,C)
AC=dist(p(1,:),p(3,:));
BV=dist(p(2,:),p(4,:));
AV=dist(p(1,:),p(4,:));
BC=dist(p(2,:),p(3,:));
cr=AC*BV/(AV*BC);
result=cr*C;
end