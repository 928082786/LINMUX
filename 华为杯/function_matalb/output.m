function out_vector=output(p)
[~,num_p]=size(p);
for i = 1 : num_p
    out_vector(i,:)=p{i};
end
end