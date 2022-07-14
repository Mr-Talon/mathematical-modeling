import numpy as np
import pandas as pd

data=pd.read_excel("C:/Users/16046/Desktop/dataTrans.xlsx")
data=np.array(data)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i][j]!=0:
            data[i][j]=11-data[i][j]

print(data)
test2=pd.DataFrame(data=data)
test2.to_csv('dataTrans.csv')