function average=miedian(p)
[col,row]=size(p);
x=zeros(col,row);
y=zeros(col,row);
sum_x=0;
sum_y=0;
count=0;
for i=1:row-1
    a1=p{1,i};
    for j=i+1:row
        a2=p{1,j};
        x(i,j)=(a2(1,2)-a1(1,2))/(a1(1,1)-a2(1,1));
        y(i,j)=x(i,j)*a1(1,1)+a1(1,2);
        
            axis_x=1:10:5000;
            axis_y1=a1(1,1)*axis_x+a1(1,2);
            axis_y2=a2(1,1)*axis_x+a2(1,2);
            plot(axis_x,axis_y1);
            hold on;
            plot(axis_x,axis_y2);
            hold on;
            plot(x(i,j),y(i,j),'*');

         sum_x=sum_x+x(i,j);
         sum_y=sum_y+y(i,j);
         count=count+1;
    end
    average_x=sum_x/count;
    average_y=sum_y/count;
    average=[average_x,average_y];
end
        


% for i=1:col
%     for j=i+1:row
%         a1=p{i,j};
%             for m=i:col
%                 for n=j:row
%                     a2=p{m,n};
%                     if ((m~=i||n~=j)&&m<n)
%                     x(i,j,m,n)=(a2(1,2)-a1(1,2))/(a1(1,1)-a2(1,1));
%                     y(i,j,m,n)=x(i,j,m,n)*a1(1,1)+a1(1,2);
%                     
%                     axis_x=1:10:5000;
%                     axis_y1=a1(1,1)*axis_x+a1(1,2);
%                     axis_y2=a2(1,1)*axis_x+a2(1,2);
%                     plot(axis_x,axis_y1);
%                     hold on;
%                     plot(axis_x,axis_y2);
%                     hold on;
%                     plot(x(i,j,m,n),y(i,j,m,n),'*');    

%                     sum_x=sum_x+x(i,j,m,n);
%                     sum_y=sum_y+y(i,j,m,n);
%                     count=count+1;
%                     end
%                 end
%             end     
% %         for k=i+1:col
% %             a2=p{k,j};
% %             x(count)=(a1(1,2)-a2(2,2))/(a1(1,1)-a2(2,1));
% %             y(count)=x(count)*a(1,1)+a(1,2);
% %         end  
%     end
% average_x=sum_x/count;
% average_y=sum_y/count;
end
