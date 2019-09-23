function diatance_draw(matrix,x,y,num)
    for i=0:num-3
        for j=1:3
            line(j,1)=matrix(i+j,1);
            line(j,2)=matrix(i+j,2);
        end
        hold on;
        plot([line(:,1);x],[line(:,2);y]);
    end
    hold off;
end