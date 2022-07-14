import pandas as pd
import numpy as np

data1 = pd.read_excel("C:/Users/16046/Desktop/T3ans.xlsx")
data2 = pd.read_excel("C:/Users/16046/Desktop/T3mid.xlsx")
data3= pd.read_excel("C:/Users/16046/Desktop/T3理想解法.xlsx")
p=pd.read_excel("C:/Users/16046/Desktop/dataTrans.xlsx")
data4=pd.read_excel("C:/Users/16046/Desktop/T2ans.xlsx")

data1=np.array(data1)
data1=np.delete(data1,0,0)
data2=np.array(data2)
p=np.array(p)
data3=np.array(data3)
data3=np.delete(data3,0,0)
data4=np.array(data4)

# print(data1.shape)
# print(data2.shape)

# for i in range(1000):
#     for j in range(100):
#         if data1[i][j]!=data2[i][j]:
#             print(i,j)

# z=np.array(p*data1)
# print(z.shape)
# print(z)
# print(sum(sum(z)))
#
# z2=np.array(p*data3)
# print(sum(sum(z2)))]

for i in range(1000):
    for j in range(100):
        if p[i][j]==0:
            if data4[i][j]!=0:
                print("!")
                break