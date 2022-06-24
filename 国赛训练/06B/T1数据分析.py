import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("数据补齐.csv")
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

MeanCD4Stage1M = np.mean(CD4Stage1M)
MeanCD4Stage2M = np.mean(CD4Stage2M)
MeanCD4Stage3M = np.mean(CD4Stage3M)
MeanCD4Stage4M = np.mean(CD4Stage4M)
MeanCD4Stage5M = np.mean(CD4Stage5M)

MeanHIVStage1M = np.mean(HIVStage1M)
MeanHIVStage2M = np.mean(HIVStage2M)
MeanHIVStage3M = np.mean(HIVStage3M)
MeanHIVStage4M = np.mean(HIVStage4M)
MeanHIVStage5M = np.mean(HIVStage5M)

print("晚期CD4："+str(MeanCD4Stage1)+" "+str(MeanCD4Stage2)+" "+str(MeanCD4Stage3)+" "+str(MeanCD4Stage4)+" "+str(MeanCD4Stage5))
print("晚期HIV："+str(MeanHIVStage1)+" "+str(MeanHIVStage2)+" "+str(MeanHIVStage3)+" "+str(MeanHIVStage4)+" "+str(MeanHIVStage5))

print("早期CD4："+str(MeanCD4Stage1M)+" "+str(MeanCD4Stage2M)+" "+str(MeanCD4Stage3M)+" "+str(MeanCD4Stage4M)+" "+str(MeanCD4Stage5M))
print("早期HIV："+str(MeanHIVStage1M)+" "+str(MeanHIVStage2M)+" "+str(MeanHIVStage3M)+" "+str(MeanHIVStage4M)+" "+str(MeanHIVStage5M))

t=[1,4,8,24,40]
MeanCD4=[MeanCD4Stage1,MeanCD4Stage2,MeanCD4Stage3,MeanCD4Stage4,MeanCD4Stage5]
MeanHIV=[MeanHIVStage1,MeanHIVStage2,MeanHIVStage3,MeanHIVStage4,MeanHIVStage5]
MeanCD4M=[MeanCD4Stage1M,MeanCD4Stage2M,MeanCD4Stage3M,MeanCD4Stage4M,MeanCD4Stage5M]
MeanHIVM=[MeanHIVStage1M,MeanHIVStage2M,MeanHIVStage3M,MeanHIVStage4M,MeanHIVStage5M]


plt.figure("1")
plt.xlabel('test time')
plt.ylabel('CD4')
plt.title('T1')
plt.axis([0, 45, 35, 230])
plt.grid(True)
plt.plot(t, MeanCD4, '-.', color = 'dodgerblue', label="CD4 less than normal")
plt.plot(t, MeanCD4M, '-.', color = 'darkorange', label="CD4 more than normal")
plt.legend()

plt.figure("2")
plt.xlabel('test time')
plt.ylabel('HIV')
plt.title('T1')
plt.axis([0, 45, 2, 5])
plt.grid(True)
plt.plot(t, MeanHIV, '-.', color = 'r', label="CD4 less than normal")
plt.plot(t, MeanHIVM, '-.', color = 'darkorange', label="CD4 more than normal")
plt.legend()
plt.show()