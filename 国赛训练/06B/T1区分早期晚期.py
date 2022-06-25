import numpy as np
import pandas as pd

data = pd.read_csv("数据补齐.csv")
data = np.array(data)

early=[]
lata=[]

ID = data[0][0]  # 标记用户ID
originPos = 0

for i in range(len(data)):
    if data[i][0] != ID:  # 统计病人的个数
        ID = data[i][0]
        originPos = i

    # CD4和HIV的测量时间有个别不一样 所以分开处理
    if data[i][2] <= 400:  # CD4数量超过2000就太多了  是异常数据
        if data[originPos][2] <= 100:
            lata.append(data[i])
        else:
            early.append(data[i])

test1=pd.DataFrame(data=early)
test1.to_csv('T1早期.csv')

test2=pd.DataFrame(data=lata)
test2.to_csv('T1晚期.csv')