import numpy as np
import pandas as pd


data = pd.read_csv("数据补齐验证.csv")
data=np.array(data)

# 两种病人 一种是一开始CD4就少于正常值的
CD4Stage1 = []
CD4Stage2 = []
CD4Stage3 = []
CD4Stage4 = []
CD4Stage5 = []

HIVStage1 = []
HIVStage2 = []
HIVStage3 = []
HIVStage4 = []
HIVStage5 = []

# 一种是一开始CD4就多于正常值的
CD4Stage1M = []
CD4Stage2M = []
CD4Stage3M = []
CD4Stage4M = []
CD4Stage5M = []

HIVStage1M = []
HIVStage2M = []
HIVStage3M = []
HIVStage4M = []
HIVStage5M = []


ID = 0  # 标记用户ID
numOfPatient = 0
for i in range(len(data)):
    if data[i][0] != ID:  # 统计病人的个数
        numOfPatient += 1
        ID = data[i][0]

    # CD4和HIV的测量时间有个别不一样 所以分开处理
    if data[i][2] <= 400:  # CD4数量超过2000就太多了  是异常数据
        if data[i][2]<=100:
            if (data[i][1] >= 0) & (data[i][1] <= 3):
                CD4Stage1.append(data[i][2])

            elif (data[i][1] >= 4) & (data[i][1] <= 7):
                CD4Stage2.append(data[i][2])

            elif (data[i][1] >= 8) & (data[i][1] <= 13):
                CD4Stage3.append(data[i][2])

            elif (data[i][1] >= 14) & (data[i][1] <= 33):
                CD4Stage4.append(data[i][2])

            else:
                CD4Stage5.append(data[i][2])
        else:
            if (data[i][1] >= 0) & (data[i][1] <= 3):
                CD4Stage1M.append(data[i][2])

            elif (data[i][1] >= 4) & (data[i][1] <= 7):
                CD4Stage2M.append(data[i][2])

            elif (data[i][1] >= 8) & (data[i][1] <= 13):
                CD4Stage3M.append(data[i][2])

            elif (data[i][1] >= 14) & (data[i][1] <= 33):
                CD4Stage4M.append(data[i][2])

            else:
                CD4Stage5M.append(data[i][2])

    # 下面处理HIV数据
    if data[i][2] <= 100:
        if (data[i][1] >= 0) & (data[i][1] <= 3):
            HIVStage1.append(data[i][4])
        elif (data[i][1] >= 4) & (data[i][1] <= 7):
            HIVStage2.append(data[i][4])
        elif (data[i][1] >= 8) & (data[i][1] <= 13):
            HIVStage3.append(data[i][4])
        elif (data[i][1] >= 14) & (data[i][1] <= 33):
            HIVStage4.append(data[i][4])
        else:
            HIVStage5.append(data[i][4])
    else:
        if (data[i][1] >= 0) & (data[i][1] <= 3):
            HIVStage1M.append(data[i][4])
        elif (data[i][1] >= 4) & (data[i][1] <= 7):
            HIVStage2M.append(data[i][4])
        elif (data[i][1] >= 8) & (data[i][1] <= 13):
            HIVStage3M.append(data[i][4])
        elif (data[i][1] >= 14) & (data[i][1] <= 33):
            HIVStage4M.append(data[i][4])
        else:
            HIVStage5M.append(data[i][4])

print(CD4Stage1)
print(CD4Stage2)
print(CD4Stage3)
print(CD4Stage4)
print(CD4Stage5)
print("\n")
print(CD4Stage1M)
print(CD4Stage2M)
print(CD4Stage3M)
print(CD4Stage4M)
print(CD4Stage5M)
print("\n")
print(HIVStage1)
print(HIVStage2)
print(HIVStage3)
print(HIVStage4)
print(HIVStage5)
print("\n")
print(HIVStage1M)
print(HIVStage2M)
print(HIVStage3M)
print(HIVStage4M)
print(HIVStage5M)
