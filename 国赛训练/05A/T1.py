import numpy as np
import pandas as pd

data = pd.read_excel("C:/Users/16046/Desktop/17个观测点数据.xlsx")
data = np.array(data[['PH标准化', 'DO按区间标准化', 'CODMn按区间标准化', 'NH3-N按区间标准化']])


def fun1(x):
    if x <= 0.1333:
        return 0
    else:
        return 1 - np.exp(-((x - 0.1333) / 0.1751) ** 2)


def fun2(x):
    if x <= 0.0667:
        return 0
    else:
        return 1 - np.exp(-((x - 0.0667) / 0.2197) ** 2)


def fun3(x):
    if x <= 0.0375:
        return 0
    else:
        return 1 - np.exp(-((x - 0.0375) / 0.3048) ** 2)


score = []  # 综合评价得分  使用动态加权综合评价
for i in range(len(data)):
    sum = 0.8 * (fun1(data[i][1]) * data[i][1] + fun2(data[i][2]) * data[i][2] + fun3(data[i][3]) * data[i][3]) + 0.2 * \
          data[i][0]
    score.append(sum)

res = pd.DataFrame(data=score)
res.to_csv('综合评价得分.csv')

i = 0
j = 0
ans = [[0] * 28 for _ in range(17)]  # 评价矩阵初始化
for j in range(28):
    for i in range(17):
        ans[i][j] = score[j * 17 + i]  # 评价矩阵输出格式转换
ans = np.array(ans)  # 评价矩阵

rank = [[0] * 28 for _ in range(17)]  # 排名矩阵初始化
i = 0
for i in range(28):
    list = [ls[i] for ls in ans]  # list 取出评价矩阵的每一列
    rankOfList = np.argsort(np.argsort(list))
    for row in range(len(rankOfList)):  # 将排名存入排名矩阵
        rank[row][i] = rankOfList[row]
rank = np.array(rank)

totalRank = rank.sum(axis=1)
print(totalRank)
print(np.argsort(np.argsort(totalRank)) + 1)
