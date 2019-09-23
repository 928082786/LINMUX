function p=make_line(matrix,num_a)
for i=1:2:num_a-1
        p{(i+1)/2}=polyfit([matrix(i,1),matrix(i+1,1)],[matrix(i,2),matrix(i+1,2)],1);
end
end