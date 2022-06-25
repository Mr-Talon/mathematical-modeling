import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 10

data1 = pd.read_excel("C:/Users/16046/Desktop/疗法1（去除初值影响）.xlsx")
data1 = np.array(data1)
data2 = pd.read_excel("C:/Users/16046/Desktop/疗法2（去除初值影响）.xlsx")
data2 = np.array(data2)
data3 = pd.read_excel("C:/Users/16046/Desktop/疗法3（去除初值影响）.xlsx")
data3 = np.array(data3)
data4 = pd.read_excel("C:/Users/16046/Desktop/疗法4（去除初值影响）.xlsx")
data4 = np.array(data4)

Y1 = []  # 疗法1
MY1 = []
M1 = []
O1 = []

Y2 = []  # 疗法2
MY2 = []
M2 = []
O2 = []

Y3 = []  # 疗法3
MY3 = []
M3 = []
O3 = []

Y4 = []  # 疗法4
MY4 = []
M4 = []
O4 = []

for i in range(len(data1)):
    if data1[i][1] <= 29:  # 青年组
        Y1.append(data1[i])

    elif (data1[i][1] > 29) & (data1[i][1] <= 39):  # 中青年组
        MY1.append(data1[i])

    elif (data1[i][1] > 39) & (data1[i][1] <= 49):  # 中年组
        M1.append(data1[i])

    else:  # 老年组
        O1.append(data1[i])

for i in range(len(data2)):
    if data2[i][1] <= 29:  # 青年组
        Y2.append(data2[i])

    elif (data2[i][1] > 29) & (data2[i][1] <= 39):  # 中青年组
        MY2.append(data2[i])

    elif (data2[i][1] > 39) & (data2[i][1] <= 49):  # 中年组
        M2.append(data2[i])

    else:  # 老年组
        O2.append(data2[i])

for i in range(len(data3)):
    if data3[i][1] <= 29:  # 青年组
        Y3.append(data3[i])

    elif (data3[i][1] > 29) & (data3[i][1] <= 39):  # 中青年组
        MY3.append(data3[i])

    elif (data3[i][1] > 39) & (data3[i][1] <= 49):  # 中年组
        M3.append(data3[i])

    else:  # 老年组
        O3.append(data3[i])

for i in range(len(data4)):
    if data4[i][1] <= 29:  # 青年组
        Y4.append(data4[i])

    elif (data4[i][1] > 29) & (data4[i][1] <= 39):  # 中青年组
        MY4.append(data4[i])

    elif (data4[i][1] > 39) & (data4[i][1] <= 49):  # 中年组
        M4.append(data4[i])

    else:  # 老年组
        O4.append(data4[i])

# 青年组  每个表示一个病人的数据的横坐标和纵坐标
x_1Y = []
CD41Y = []

x_2Y = []
CD42Y = []

x_3Y = []
CD43Y = []

x_4Y = []
CD44Y = []

x_5Y = []
CD45Y = []

# 中青年组
x_1MY = []
CD41MY = []

x_2MY = []
CD42MY = []

x_3MY = []
CD43MY = []

x_4MY = []
CD44MY = []

x_5MY = []
CD45MY = []

# 中年组
x_1M = []
CD41M = []

x_2M = []
CD42M = []

x_3M = []
CD43M = []

x_4M = []
CD44M = []

x_5M = []
CD45M = []

# 老年组
x_1O = []
CD41O = []

x_2O = []
CD42O = []

x_3O = []
CD43O = []

x_4O = []
CD44O = []

x_5O = []
CD45O = []

countOfPlot = 0
ID = 0
for i in range(len(Y3)):  # 疗法2 青年组
    if countOfPlot <= 5:
        if Y3[i][0] != ID:
            ID = Y3[i][0]
            countOfPlot += 1

        if countOfPlot==1:
            x_1Y.append(Y3[i][2])
            CD41Y.append(Y3[i][3])
        elif countOfPlot==2:
            x_2Y.append(Y3[i][2])
            CD42Y.append(Y3[i][3])
        elif countOfPlot==3:
            x_3Y.append(Y3[i][2])
            CD43Y.append(Y3[i][3])
        elif countOfPlot==4:
            x_4Y.append(Y3[i][2])
            CD44Y.append(Y3[i][3])
        elif countOfPlot==5:
            x_5Y.append(Y3[i][2])
            CD45Y.append(Y3[i][3])
    else:
        break

countOfPlot = 0
ID = 0
for i in range(len(MY3)):  # 疗法2 中青年组
    if countOfPlot <= 5:
        if MY3[i][0] != ID:
            ID = MY3[i][0]
            countOfPlot += 1

        if countOfPlot==1:
            x_1MY.append(MY3[i][2])
            CD41MY.append(MY3[i][3])
        elif countOfPlot==2:
            x_2MY.append(MY3[i][2])
            CD42MY.append(MY3[i][3])
        elif countOfPlot==3:
            x_3MY.append(MY3[i][2])
            CD43MY.append(MY3[i][3])
        elif countOfPlot==4:
            x_4MY.append(MY3[i][2])
            CD44MY.append(MY3[i][3])
        elif countOfPlot==5:
            x_5MY.append(MY3[i][2])
            CD45MY.append(MY3[i][3])
    else:
        break

countOfPlot = 0
ID = 0
for i in range(len(M3)):  # 疗法2 中年组
    if countOfPlot <= 5:
        if M3[i][0] != ID:
            ID = M3[i][0]
            countOfPlot += 1

        if countOfPlot==1:
            x_1M.append(M3[i][2])
            CD41M.append(M3[i][3])
        elif countOfPlot==2:
            x_2M.append(M3[i][2])
            CD42M.append(M3[i][3])
        elif countOfPlot==3:
            x_3M.append(M3[i][2])
            CD43M.append(M3[i][3])
        elif countOfPlot==4:
            x_4M.append(M3[i][2])
            CD44M.append(M3[i][3])
        elif countOfPlot==5:
            x_5M.append(M3[i][2])
            CD45M.append(M3[i][3])
    else:
        break

countOfPlot = 0
ID = 0
for i in range(len(O3)):  # 疗法2 老年组
    if countOfPlot <= 5:
        if O3[i][0] != ID:
            ID = O3[i][0]
            countOfPlot += 1

        if countOfPlot==1:
            x_1O.append(O3[i][2])
            CD41O.append(O3[i][3])
        elif countOfPlot==2:
            x_2O.append(O3[i][2])
            CD42O.append(O3[i][3])
        elif countOfPlot==3:
            x_3O.append(O3[i][2])
            CD43O.append(O3[i][3])
        elif countOfPlot==4:
            x_4O.append(O3[i][2])
            CD44O.append(O3[i][3])
        elif countOfPlot==5:
            x_5O.append(O3[i][2])
            CD45O.append(O3[i][3])
    else:
        break

plt.figure("1")
plt.xlabel('测量时间/（周）')
plt.ylabel('Log(CD4 count+1) ')
plt.title('疗法3对不同年龄段CD4的影响')
plt.axis([0, 45, 0, 2])
plt.grid(True)
plt.plot(x_1Y, CD41Y, '-.', color='dodgerblue', label="青年组")
plt.plot(x_2Y, CD42Y, '-.', color='dodgerblue')
plt.plot(x_3Y, CD43Y, '-.', color='dodgerblue')
plt.plot(x_4Y, CD44Y, '-.', color='dodgerblue')
plt.plot(x_5Y, CD45Y, '-.', color='dodgerblue')

plt.plot(x_1MY, CD41MY, '-.', color='pink', label="中青年组")
plt.plot(x_2MY, CD42MY, '-.', color='pink')
plt.plot(x_3MY, CD43MY, '-.', color='pink')
plt.plot(x_4MY, CD44MY, '-.', color='pink')
plt.plot(x_5MY, CD45MY, '-.', color='pink')

plt.plot(x_1M, CD41M, '-.', color='r', label="中年组")
plt.plot(x_2M, CD42M, '-.', color='r')
plt.plot(x_3M, CD43M, '-.', color='r')
plt.plot(x_4M, CD44M, '-.', color='r')
plt.plot(x_5M, CD45M, '-.', color='r')

plt.plot(x_1O, CD41O, '-.', color='g', label="老年组")
plt.plot(x_2O, CD42O, '-.', color='g')
plt.plot(x_3O, CD43O, '-.', color='g')
plt.plot(x_4O, CD44O, '-.', color='g')
plt.plot(x_5O, CD45O, '-.', color='g')
plt.legend()
plt.show()
