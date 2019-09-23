function [x,y]=miedian(p)
[col,row]=size(p);
for i=1:col
    for j=i:row
        a1=p{i,j};
            for m=i:col
                for n=j:row
                    a2=p{m,n};
                    x(i,j,m,n)=(a1(1,2)-a2(2,2))/(a1(1,1)-a2(2,1));
                    y(i,j,m,n)=x(count)*a(1,1)+a(1,2);
                end
            end     
%         for k=i+1:col
%             a2=p{k,j};
%             x(count)=(a1(1,2)-a2(2,2))/(a1(1,1)-a2(2,1));
%             y(count)=x(count)*a(1,1)+a(1,2);
%         end  
    end
end