import numpy as np
import pandas as pd

data1 = pd.read_excel("C:/Users/16046/Desktop/附件1验证数据.xlsx")
data1WithoutNa = data1.dropna()

data1 = np.array(data1)
data1WithoutNa = np.array(data1WithoutNa)

#数据补齐方法 用本阶段其他数据的均值作为本阶段缺失数据
# 填充空缺数据
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

ID = 0  # 标记用户ID
numOfPatient = 0
for i in range(len(data1WithoutNa)):
    if data1WithoutNa[i][0] != ID:  # 统计病人的个数
        numOfPatient += 1
        ID = data1WithoutNa[i][0]

    # CD4和HIV的测量时间有个别不一样 所以分开处理
    if data1WithoutNa[i][2] <= 400:  # CD4数量超过2000就太多了  是异常数据
        if (data1WithoutNa[i][1] >= 0) & (data1WithoutNa[i][1] <= 3):
            CD4Stage1.append(data1WithoutNa[i][2])

        elif (data1WithoutNa[i][1] >= 4) & (data1WithoutNa[i][1] <= 7):
            CD4Stage2.append(data1WithoutNa[i][2])

        elif (data1WithoutNa[i][1] >= 8) & (data1WithoutNa[i][1] <= 13):
            CD4Stage3.append(data1WithoutNa[i][2])

        elif (data1WithoutNa[i][1] >= 14) & (data1WithoutNa[i][1] <= 33):
            CD4Stage4.append(data1WithoutNa[i][2])

        else:
            CD4Stage5.append(data1WithoutNa[i][2])

    # 下面处理HIV数据
    if (data1WithoutNa[i][1] >= 0) & (data1WithoutNa[i][1] <= 3):
        HIVStage1.append(data1WithoutNa[i][4])
    elif (data1WithoutNa[i][1] >= 4) & (data1WithoutNa[i][1] <= 7):
        HIVStage2.append(data1WithoutNa[i][4])
    elif (data1WithoutNa[i][1] >= 8) & (data1WithoutNa[i][1] <= 13):
        HIVStage3.append(data1WithoutNa[i][4])
    elif (data1WithoutNa[i][1] >= 14) & (data1WithoutNa[i][1] <= 33):
        HIVStage4.append(data1WithoutNa[i][4])
    else:
        HIVStage5.append(data1WithoutNa[i][4])

#2类一共10个可能缺失的数据的均值
MeanCD4Stage1 = np.mean(CD4Stage1)
MeanCD4Stage2 = np.mean(CD4Stage2)
MeanCD4Stage3 = np.mean(CD4Stage3)
MeanCD4Stage4 = np.mean(CD4Stage4)
MeanCD4Stage5 = np.mean(CD4Stage5)

MeanHIVStage1 = np.mean(HIVStage1)
MeanHIVStage2 = np.mean(HIVStage2)
MeanHIVStage3 = np.mean(HIVStage3)
MeanHIVStage4 = np.mean(HIVStage4)
MeanHIVStage5 = np.mean(HIVStage5)

# 数据补齐
i=0
for i in range(len(data1)):
    if np.isnan(data1[i][2]):
        if (data1[i][1] >= 0) & (data1[i][1] <= 3):
            data1[i][2] = MeanCD4Stage1

        elif (data1[i][1] >= 4) & (data1[i][1] <= 7):
            data1[i][2] = MeanCD4Stage2

        elif (data1[i][1] >= 8) & (data1[i][1] <= 13):
            data1[i][2] = MeanCD4Stage3

        elif (data1[i][1] >= 14) & (data1[i][1] <= 33):
            data1[i][2] = MeanCD4Stage4

        else:
            data1[i][2] = MeanCD4Stage5

    if np.isnan(data1[i][4]):
        if (data1[i][1] >= 0) & (data1[i][1] <= 3):
            data1[i][4] = MeanHIVStage1

        elif (data1[i][1] >= 4) & (data1[i][1] <= 7):
            data1[i][4] = MeanHIVStage2

        elif (data1[i][1] >= 8) & (data1[i][1] <= 13):
            data1[i][4] = MeanHIVStage3

        elif (data1[i][1] >= 14) & (data1[i][1] <= 33):
            data1[i][4] = MeanHIVStage4

        else:
            data1[i][4] = MeanHIVStage5

    else:
        continue

test1=pd.DataFrame(data=data1)
test1.to_csv('数据补齐验证.csv')