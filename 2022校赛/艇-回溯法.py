import numpy as np
import pandas as pd

data = pd.read_excel('needList.xlsx')  # 读取需求量数据
needList = np.array(data).reshape(-1) # 转换成一维向量
numOfAns = len(needList)  # 解向量的长度   对应周数
Ans = [-1 for i in range(numOfAns)]  # 创建解向量
maxNeed = max(needList)  # 所有周里面对艇的最大需求量
num0 = 13  # 艇的初始个数
print(needList)

def limit(k, i, Ans):
    num = num0  # 当前拥有的艇的个数
    for j in range(k):
        num += Ans[j]
    num += i
    if (num < needList[k + 1] | num - num0 > maxNeed - num0):
        return False
    return True


def func(k, n, Ans):
    temp = 0
    for t in range(k):
        temp += Ans[t]
    if (temp > 0):
        n -= temp
    for i in range(n):
        if (limit(k, i, Ans)):
            Ans[k] = i
            if (k == numOfAns - 1):
                for j in range(numOfAns):
                    print(Ans[j] + ' ')
                print('\n')
        else:
            func(k + 1, numOfAns, Ans)

def func1(n,Ans):
    func(0,n,Ans)

func1(numOfAns, Ans)