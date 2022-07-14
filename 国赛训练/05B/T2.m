data=xlsread('dataTrans.xlsx','C2:CX1001');
s=xlsread('data.xls','C2:CX2');

[m,n]=size(data);
prob=optimproblem('ObjectiveSense','min');
x=optimvar('x',m,n,'Type','integer','LowerBound',0,'UpperBound',1);
%b=optimvar('b',1,n,'Type','integer','LowerBound',0);


%con1=[];
%for j=1:n
 %   t=sum(x(:,j:j+1));
 %   con1=[con1;t<=b(j)];
%end
%prob.Constraints.con1=con1;


con2=sum(x)==3*950;
prob.Constraints.con2=con2;



con4=[];
for i=1:m
    t=sum(x(i:i+1,:));
    con4=[con4;t==3];
end
prob.Constraints.con4=con4;
    
[sol,fval] = solve(prob);

ans_x=sol.x;
ans_b=sol.b;
disp(ans_x);
disp(ans_b);