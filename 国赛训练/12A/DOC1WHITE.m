data1=xlsread('C:\Users\16046\Desktop\T1白酒.xlsx','B2:K29');
data1=zscore(data1);
r=corrcoef(data1);
[x,y,z]=pcacov(r);
f=repmat(sign(sum(x)),size(x,1),1);
x=x.*f;
num=4;
df=data1*x(:,1:num);
tf=df*z(1:num)/100;
[stf,ind]=sort(tf,'descend');
stf=stf';
ind=ind';
disp(stf);
disp(ind);