import numpy as np
import pandas as pd
import math

def round(x): # 标准四舍五入
    t=x%1
    if t<0.5:
        return math.floor(x)
    else:
        return math.ceil(x)

weekConsidered=8    # 需要考虑的周数
broken=0.2   #损坏率
num = 13  # 艇的初始个数
numOfHand=50
numOfHandCanBeUsed=50
maxTrain=10

data = pd.read_excel('needList.xlsx')  # 读取需求量数据
needList = np.array(data).reshape(-1)  # 转换成一维向量
needList=needList[0:weekConsidered]
numOfAns = len(needList)  # 解向量的长度   对应周数
Ans = [-1 for i in range(numOfAns)]  # 创建解向量
maxNeed = max(needList)  # 所有周里面对艇的最大需求量

numOfBuy=[]
numOfFixed=[]
numOfTrain=[]

# for i in range(weekConsidered-1):
#     if(needList[i+1]>num-round(needList[i]*broken)):
#         numOfBuy.append(needList[i+1]-num+round(needList[i]*broken))
#         num+=numOfBuy[i]
#     else:
#         numOfBuy.append(0)
#     numOfFixed.append(num - numOfBuy[i] - needList[i])
#     num-=round(broken*needList[i])

for i in range(weekConsidered-1):
    if(needList[i+1]*4>numOfHandCanBeUsed-needList[i]*4):
        numOfBuy.append(needList[i+1]*4-numOfHandCanBeUsed+needList[i]*4)
    else:
        numOfBuy.append(0)
    numOfTrain.append(math.ceil(numOfBuy[i]/maxTrain)+numOfBuy[i])
    if(i>0):
        numOfFixed.append(numOfHandCanBeUsed-needList[i]*4-(numOfTrain[i]-numOfBuy[i])+needList[i-1]*4-round(needList[i-1]*broken)*4)
    else:
        numOfFixed.append(numOfHandCanBeUsed - needList[i] * 4 - (numOfTrain[i] - numOfBuy[i]))
    numOfHandCanBeUsed=numOfFixed[i]+numOfTrain[i]
    numOfHand=numOfHand+numOfBuy[i]-round(needList[i-1]*broken)*4

print(numOfBuy)
print(numOfFixed)
print(numOfTrain)

# test1=pd.DataFrame(data=numOfBuy)
# test1.to_csv('艇购买答案.csv')
# test2=pd.DataFrame(data=numOfFixed)
# test2.to_csv('艇保养答案.csv')
