import pulp
import pandas as pd
import numpy as np
import math

from pulp import COIN_CMD


def round(x):  # 标准四舍五入
    t = x % 1
    if t < 0.5:
        return math.floor(x)
    else:
        return math.ceil(x)


weekConsidered = 104

data = pd.read_excel('needList.xlsx')  # 读取需求量数据
needList = np.array(data).reshape(-1)  # 转换成一维向量
needList = needList[0:weekConsidered]

MyProbLP = pulp.LpProblem("demo", sense=pulp.LpMinimize)

a1= [pulp.LpVariable('hand_already', lowBound=0, cat='Integer') for i1 in range(weekConsidered)]
a2= [pulp.LpVariable('hand_buy', lowBound=0, cat='Integer') for i2 in range(weekConsidered)]
a3= [pulp.LpVariable('hand_work', lowBound=0, cat='Integer') for i3 in range(weekConsidered)]
a4= [pulp.LpVariable('hand_rest', lowBound=0, cat='Integer') for i4 in range(weekConsidered)]
a5= [pulp.LpVariable('hand_train', lowBound=0, cat='Integer') for i5 in range(weekConsidered)]

func=0
for i in range(weekConsidered):
    func+=110*a2[i]+5*a4[i]+10*a5[i]

MyProbLP+=func

for i in range(weekConsidered):
    MyProbLP += (a1[i]==a3[i]+a4[i]+a5[i])
    MyProbLP+=(10*a5[i]>=a2[i])

for i in range(weekConsidered-1):
    MyProbLP+=(a1[i+1]==a1[i]+a2[i]-round(needList[i]*0.2)*4)
    MyProbLP+=(a3[i+1]<=a1[i]+a2[i]-a3[i])
MyProbLP+=(a1[0]==50)

# 5. 求解
MyProbLP.solve(COIN_CMD)

# 6. 打印求解状态
print("Status:", pulp.LpStatus[MyProbLP.status])

print("z= ", pulp.value(MyProbLP.objective))

# 7. 打印出每个变量的最优值
for v in MyProbLP.variables():
    print(v.name, "=", v.varValue)

