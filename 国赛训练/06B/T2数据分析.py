import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 10

data = pd.read_excel("C:/Users/16046/Desktop/T2疗法4.xlsx")
data = np.array(data)

# 分成四个年龄组 每个年龄组6个测试阶段
# 青年组
Y1 = []
Y2 = []
Y3 = []
Y4 = []
Y5 = []
Y6 = []

# 中青年组
MY1 = []
MY2 = []
MY3 = []
MY4 = []
MY5 = []
MY6 = []

# 中年组
M1 = []
M2 = []
M3 = []
M4 = []
M5 = []
M6 = []

# 老年组
O1 = []
O2 = []
O3 = []
O4 = []
O5 = []
O6 = []

ID = 0  # 标记用户ID
numOfPatient = 0
for i in range(len(data)):
    if data[i][0] != ID:  # 统计病人的个数
        numOfPatient += 1
        ID = data[i][0]

    if data[i][1] <= 29:  # 青年组
        if (data[i][2] >= 0) & (data[i][2] < 7):
            Y1.append(data[i][3])

        elif (data[i][2] >= 7) & (data[i][2] < 15):
            Y2.append(data[i][3])

        elif (data[i][2] >= 15) & (data[i][2] < 23):
            Y3.append(data[i][3])

        elif (data[i][2] >= 23) & (data[i][2] < 31):
            Y4.append(data[i][3])

        elif (data[i][2] >= 31) & (data[i][2] < 38):
            Y5.append(data[i][3])

        else:
            Y6.append(data[i][3])

    elif (data[i][1] > 29) & (data[i][1] <= 39):  # 中青年组
        if (data[i][2] >= 0) & (data[i][2] < 7):
            MY1.append(data[i][3])

        elif (data[i][2] >= 7) & (data[i][2] < 15):
            MY2.append(data[i][3])

        elif (data[i][2] >= 15) & (data[i][2] < 23):
            MY3.append(data[i][3])

        elif (data[i][2] >= 23) & (data[i][2] < 31):
            MY4.append(data[i][3])

        elif (data[i][2] >= 31) & (data[i][2] < 38):
            MY5.append(data[i][3])

        else:
            MY6.append(data[i][3])

    elif (data[i][1] > 39) & (data[i][1] <= 49):  # 中年组
        if (data[i][2] >= 0) & (data[i][2] < 7):
            M1.append(data[i][3])

        elif (data[i][2] >= 7) & (data[i][2] < 15):
            M2.append(data[i][3])

        elif (data[i][2] >= 15) & (data[i][2] < 23):
            M3.append(data[i][3])

        elif (data[i][2] >= 23) & (data[i][2] < 31):
            M4.append(data[i][3])

        elif (data[i][2] >= 31) & (data[i][2] < 38):
            M5.append(data[i][3])

        else:
            M6.append(data[i][3])

    else:  # 老年组
        if (data[i][2] >= 0) & (data[i][2] < 7):
            O1.append(data[i][3])

        elif (data[i][2] >= 7) & (data[i][2] < 15):
            O2.append(data[i][3])

        elif (data[i][2] >= 15) & (data[i][2] < 23):
            O3.append(data[i][3])

        elif (data[i][2] >= 23) & (data[i][2] < 31):
            O4.append(data[i][3])

        elif (data[i][2] >= 31) & (data[i][2] < 38):
            O5.append(data[i][3])

        else:
            O6.append(data[i][3])

# 4类一共24个
MeanY1 = np.mean(Y1)
MeanY2 = np.mean(Y2)
MeanY3 = np.mean(Y3)
MeanY4 = np.mean(Y4)
MeanY5 = np.mean(Y5)
MeanY6 = np.mean(Y6)

MeanMY1 = np.mean(MY1)
MeanMY2 = np.mean(MY2)
MeanMY3 = np.mean(MY3)
MeanMY4 = np.mean(MY4)
MeanMY5 = np.mean(MY5)
MeanMY6 = np.mean(MY6)

MeanM1 = np.mean(M1)
MeanM2 = np.mean(M2)
MeanM3 = np.mean(M3)
MeanM4 = np.mean(M4)
MeanM5 = np.mean(M5)
MeanM6 = np.mean(M6)

MeanO1 = np.mean(O1)
MeanO2 = np.mean(O2)
MeanO3 = np.mean(O3)
MeanO4 = np.mean(O4)
MeanO5 = np.mean(O5)
MeanO6 = np.mean(O6)

print("病人人数：" + str(numOfPatient) + "\n")
print("青年组：\n" + str(Y1) + "\n" + str(Y2) + "\n" + str(Y3) + "\n" + str(Y4) + "\n" + str(Y5) + "\n" + str(Y6) + "\n")
print("青年组各阶段均值\n" + str(MeanY1) + "\n" + str(MeanY2) + "\n" + str(MeanY3) + "\n" + str(MeanY4) + "\n" + str(
    MeanY5) + "\n" + str(MeanY6) + "\n")

print("中青年组：\n" + str(MY1) + "\n" + str(MY2) + "\n" + str(MY3) + "\n" + str(MY4) + "\n" + str(MY5) + "\n" + str(
    MY6) + "\n")
print("中青年组各阶段均值\n" + str(MeanMY1) + "\n" + str(MeanMY2) + "\n" + str(MeanMY3) + "\n" + str(MeanMY4) + "\n" + str(
    MeanMY5) + "\n" + str(MeanMY6) + "\n")

print("中年组：\n" + str(M1) + "\n" + str(M2) + "\n" + str(M3) + "\n" + str(M4) + "\n" + str(M5) + "\n" + str(M6) + "\n")
print("中年组各阶段均值\n" + str(MeanM1) + "\n" + str(MeanM2) + "\n" + str(MeanM3) + "\n" + str(MeanM4) + "\n" + str(
    MeanM5) + "\n" + str(MeanM6) + "\n")

print("老年组：\n" + str(O1) + "\n" + str(O2) + "\n" + str(O3) + "\n" + str(O4) + "\n" + str(O5) + "\n" + str(O6) + "\n")
print("老组各阶段均值\n" + str(MeanO1) + "\n" + str(MeanO2) + "\n" + str(MeanO3) + "\n" + str(MeanO4) + "\n" + str(
    MeanO5) + "\n" + str(MeanO6) + "\n")

MeanY = [MeanY1, MeanY2, MeanY3, MeanY4, MeanY5, MeanY6]
MeanMY = [MeanMY1, MeanMY2, MeanMY3, MeanMY4, MeanMY5, MeanMY6]
MeanM = [MeanM1, MeanM2, MeanM3, MeanM4, MeanM5, MeanM6]
MeanO = [MeanO1, MeanO2, MeanO3, MeanO4, MeanO5, MeanO6]

T = [1, 8, 16, 24, 32, 40]
plt.figure("1")
plt.xlabel('测量时间/（周）')
plt.ylabel('Log(CD4 count+1) ')
plt.title('疗法4不同年龄组CD4曲线')
plt.axis([0, 45, 0, 3.8])
plt.grid(True)
plt.plot(T, MeanY, '-.', color='dodgerblue', label="青年组")
plt.plot(T, MeanMY, '-.', color='darkorange', label="中青年组")
plt.plot(T, MeanM, '-.', color='r', label="中年组")
plt.plot(T, MeanO, '-.', color='g', label="老年组")
plt.legend()
plt.show()
