c=[1,1];
D=[20000,10000,5000,2500,1000];
for i=1:5
    a=[-3,-1;3,0;0,1];
    b=[-0.5*D(i);0.6*D(i);0.4*D(i)];
    intcon=[1,2];
    [x1,y1]=intlinprog(c,intcon,a,b,[],[],zeros(2,1));
    fprintf('DVD%d:\n',i);
    disp(x1);
    disp(y1);
end


fprintf('三个月:');
for i=1:5
    a=[-9,-3;9,0;0,3];
    b=[-0.95*D(i);0.6*D(i);0.4*D(i)];
    intcon=[1,2];
    [x2,y2]=intlinprog(c,intcon,a,b,[],[],zeros(2,1));
    fprintf('DVD%d:\n',i);
    disp(x2);
    disp(y2);
end