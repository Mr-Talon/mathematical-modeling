data=xlsread('C:\Users\16046\Desktop\白综合得分.xlsx','B2:C29');
data=zscore(data);
y=pdist(data);
z=linkage(y,'average');
dendrogram(z);
k=5;
T=cluster(z,'maxclust',k);
for i=1:k
    tm=find(T==i);
    tm=reshape(tm,1,length(tm));
    fprintf('第%d类的有%s\n',i,int2str(tm));
end