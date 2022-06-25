import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 10

data = pd.read_csv("数据补齐.csv")
data = np.array(data)

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

ID = data[0][0]  # 标记用户ID
numOfPatient = 0
originPos = 0

for i in range(len(data)):
    if data[i][0] != ID:  # 统计病人的个数
        numOfPatient += 1
        ID = data[i][0]
        originPos = i

    # CD4和HIV的测量时间有个别不一样 所以分开处理
    if data[i][2] <= 400:  # CD4数量超过2000就太多了  是异常数据
        if data[originPos][2] <= 100:
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
    if data[originPos][2] <= 100:
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

# 2类一共10个可能缺失的数据的均值
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

print("晚期CD4：" + str(MeanCD4Stage1) + " " + str(MeanCD4Stage2) + " " + str(MeanCD4Stage3) + " " + str(
    MeanCD4Stage4) + " " + str(MeanCD4Stage5))
print("晚期HIV：" + str(MeanHIVStage1) + " " + str(MeanHIVStage2) + " " + str(MeanHIVStage3) + " " + str(
    MeanHIVStage4) + " " + str(MeanHIVStage5))

print("早期CD4：" + str(MeanCD4Stage1M) + " " + str(MeanCD4Stage2M) + " " + str(MeanCD4Stage3M) + " " + str(
    MeanCD4Stage4M) + " " + str(MeanCD4Stage5M))
print("早期HIV：" + str(MeanHIVStage1M) + " " + str(MeanHIVStage2M) + " " + str(MeanHIVStage3M) + " " + str(
    MeanHIVStage4M) + " " + str(MeanHIVStage5M))

t = [1, 4, 8, 24, 40]
MeanCD4 = [MeanCD4Stage1, MeanCD4Stage2, MeanCD4Stage3, MeanCD4Stage4, MeanCD4Stage5]
MeanHIV = [MeanHIVStage1, MeanHIVStage2, MeanHIVStage3, MeanHIVStage4, MeanHIVStage5]
MeanCD4M = [MeanCD4Stage1M, MeanCD4Stage2M, MeanCD4Stage3M, MeanCD4Stage4M, MeanCD4Stage5M]
MeanHIVM = [MeanHIVStage1M, MeanHIVStage2M, MeanHIVStage3M, MeanHIVStage4M, MeanHIVStage5M]

CD4Sample = []
CD4MSample = []
HIVSample = []
HIVMSample = []

for i in range(5):
    CD4Sample.append(CD4Stage1[i])
    CD4Sample.append(CD4Stage2[i])
    CD4Sample.append(CD4Stage3[i])
    CD4Sample.append(CD4Stage4[i])
    CD4Sample.append(CD4Stage5[i])

    HIVSample.append(HIVStage1[i])
    HIVSample.append(HIVStage2[i])
    HIVSample.append(HIVStage3[i])
    HIVSample.append(HIVStage4[i])
    HIVSample.append(HIVStage5[i])

    CD4MSample.append(CD4Stage1M[i])
    CD4MSample.append(CD4Stage2M[i])
    CD4MSample.append(CD4Stage3M[i])
    CD4MSample.append(CD4Stage4M[i])
    CD4MSample.append(CD4Stage5M[i])

    HIVMSample.append(HIVStage1M[i])
    HIVMSample.append(HIVStage2M[i])
    HIVMSample.append(HIVStage3M[i])
    HIVMSample.append(HIVStage4M[i])
    HIVMSample.append(HIVStage5M[i])

plt.figure("1")
plt.xlabel('test time')
plt.ylabel('CD4')
plt.title('T1')
plt.axis([0, 45, 35, 230])
plt.grid(True)
plt.plot(t, MeanCD4, '-.', color='dodgerblue', label="CD4 less than normal")
plt.plot(t, MeanCD4M, '-.', color='darkorange', label="CD4 more than normal")
plt.legend()

plt.figure("2")
plt.xlabel('test time')
plt.ylabel('HIV')
plt.title('T1')
plt.axis([0, 45, 2, 5])
plt.grid(True)
plt.plot(t, MeanHIV, '-.', color='r', label="CD4 less than normal")
plt.plot(t, MeanHIVM, '-.', color='darkorange', label="CD4 more than normal")
plt.legend()

x_1 = [0, 4, 8, 25, 40]
CD45_1 = [178, 228, 126, 171, 99]
HIV5_1 = [5.5, 3.9, 4.7, 4, 5]

x_2 = [0, 4, 8, 26, 46, 54]
CD45_2 = [101, 151, 115, 149, 120, 141]
HIV5_2 = [4.5, 1.7, 1.7, 2.8, 3.4, 2.909195402]

x_3 = [0, 3, 8, 24, 40]
CD45_3 = [161, 220, 316, 645, 451]
HIV5_3 = [5.5, 2.5, 1.9, 1.7, 1.7]

x_4 = [0, 4, 8, 24, 39]
CD45_4 = [139, 289, 209, 238, 196]
HIV5_4 = [5.3, 4.3, 4.6, 4.9, 5.1]

x_5 = [0, 3, 7, 23, 40]
CD45_5 = [140, 189, 324, 252, 305]
HIV5_5 = [4.9, 3.3, 2.4, 4.4, 4.7]

plt.figure("3")
plt.xlabel('测量时间')
plt.ylabel('CD4')
plt.title('早期病人CD4变化折线图')
plt.axis([0, 45, 0, 700])
plt.grid(True)
plt.plot(x_1, CD45_1, '-.', color='r', label="病人1")
plt.plot(x_2, CD45_2, '-.', color='darkorange', label="病人2")
plt.plot(x_3, CD45_3, '-.', color='g', label="病人3")
plt.plot(x_4, CD45_4, '-.', color='b', label="病人4")
plt.plot(x_5, CD45_5, '-.', color='pink', label="病人5")
plt.legend()

plt.figure("4")
plt.xlabel('测量时间')
plt.ylabel('HIV')
plt.title('早期病人HIV变化折线图')
plt.axis([0, 45, 0, 6])
plt.grid(True)
plt.plot(x_1, HIV5_1, '-.', color='r', label="病人1")
plt.plot(x_2, HIV5_2, '-.', color='darkorange', label="病人2")
plt.plot(x_3, HIV5_3, '-.', color='g', label="病人3")
plt.plot(x_4, HIV5_4, '-.', color='b', label="病人4")
plt.plot(x_5, HIV5_5, '-.', color='pink', label="病人5")
plt.legend()

x_1 = [0, 4, 7, 24, 39]
CD45_1 = [78, 140, 245, 201, 220]
HIV5_1 = [5.6, 2.1, 1.8, 1.7, 1.7]

x_2 = [0, 4, 9, 22, 38]
CD45_2 = [53, 187, 285, 200, 248]
HIV5_2 = [5.2, 1.8, 1.9, 1.7, 3.2]

x_3 = [0, 4, 9, 23, 42]
CD45_3 = [96, 79, 92, 257, 137]
HIV5_3 = [5.7, 3.8, 2.5, 3.4, 4.6]

x_4 = [0, 4, 8, 25, 40]
CD45_4 = [84, 82, 127, 137, 81]
HIV5_4 = [5.6, 4.5, 3.6, 1.7, 2.4]

x_5 = [0, 5, 8, 24, 46]
CD45_5 = [21, 86, 149, 117, 127]
HIV5_5 = [5.4, 3.6, 3.4, 4.1, 3.9]

plt.figure("5")
plt.xlabel('测量时间')
plt.ylabel('CD4')
plt.title('晚期病人CD4变化折线图')
plt.axis([0, 50, 0, 300])
plt.grid(True)
plt.plot(x_1, CD45_1, '-.', color='r', label="病人1")
plt.plot(x_2, CD45_2, '-.', color='darkorange', label="病人2")
plt.plot(x_3, CD45_3, '-.', color='g', label="病人3")
plt.plot(x_4, CD45_4, '-.', color='b', label="病人4")
plt.plot(x_5, CD45_5, '-.', color='pink', label="病人5")
plt.legend()

plt.figure("6")
plt.xlabel('测量时间')
plt.ylabel('HIV')
plt.title('晚期病人HIV变化折线图')
plt.axis([0, 50, 0, 6])
plt.grid(True)
plt.plot(x_1, HIV5_1, '-.', color='r', label="病人1")
plt.plot(x_2, HIV5_2, '-.', color='darkorange', label="病人2")
plt.plot(x_3, HIV5_3, '-.', color='g', label="病人3")
plt.plot(x_4, HIV5_4, '-.', color='b', label="病人4")
plt.plot(x_5, HIV5_5, '-.', color='pink', label="病人5")
plt.legend()
plt.show()
