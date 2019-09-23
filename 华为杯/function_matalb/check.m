function num = check(a)
for i=1:100
    if(a(i,1)==0 && a(i,2)==0)
        num=i-1;
        break;
    end
end