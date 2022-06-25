import numpy as np
import pandas as pd

data2 = pd.read_excel("C:/Users/16046/Desktop/处理后附件2.xlsx")
data = np.array(data2)

originPos = 0
ID = data[0][0]
for i in range(len(data)):
    if data[i][0] != ID:
        if data[originPos][4] != 0:
            data[originPos][4] = 1
        originPos = i
        ID = data[i][0]

    if (data[originPos][4] == 0) | (i == originPos):
        if data[originPos][4]==0:
            data[i][4]=0
        else:
            continue
    else:
        data[i][4] /= data[originPos][4]

print(data)
test1 = pd.DataFrame(data=data)
test1.to_csv('T2去除初值影响.csv')
