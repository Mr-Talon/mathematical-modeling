import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def valueOfTakeoff(isPreCheck):
    if (isPreCheck):
        return 15, 5
    else:
        return 45, 10


def function(numberOfTraveler, numberOfIDCheck, numberOfScanner, isPreCheck):
    result = np.zeros([5, numberOfTraveler], dtype=float)
    IDcheck = np.zeros(numberOfIDCheck, dtype=float)  # 记录ID队列的情况
    scanner = np.zeros(numberOfScanner, dtype=float)  # 记录scan队列的情况

    '''
     第一行表示旅客到达时间，时间间隔符合指数分布
     第二行表示旅客开始ID检查的时间点
     第三行表示旅客完成ID检查的时间点
     第四行表示旅客开始scan检查的时间点
     第五行表示旅客完成全部安检流程的时间
    '''
    # 生成result数据
    for i in range(numberOfTraveler - 1):
        result[0][i + 1] = result[0][i] + np.random.exponential(0.07)  # 生成旅客到达机场的时间
    for i in range(numberOfTraveler):
        result[1][i] = max(result[0][i], min(IDcheck))  # 旅客开始进行id检查的时间节点
        result[2][i] = result[1][i] + np.random.normal(11.2, 3.7)  # 根据开始时间节点 随机生成结束时间节点
        IDcheck[np.argmin(IDcheck)] = result[2][i]  # 更新ID队列的属性
        result[3][i] = max(result[2][i], min(scanner))  # 旅客开始进行scan检查的时间节点
        result[4][i] = result[3][i] + np.random.normal(valueOfTakeoff(isPreCheck)[0],
                                                       valueOfTakeoff(isPreCheck)[1]) + max(np.random.normal(11.6, 5.7),
                                                                                            2.26 * np.random.normal(5.9,
                                                                                                                    6.9))
        # 旅客结束scan检查的时间的是  开始加上脱衣服的时间  加上毫米波或者x光的最大值，（要么是人等行李，要么是行李等人）
        scanner[np.argmin(scanner)] = result[4][i]  # 更新scan队列属性

    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(numberOfTraveler):
        sum1 += result[1][i] - result[0][i]
        sum2 += result[3][i] - result[2][i]
        sum3 += result[4][i] - result[0][i]
    avgtimeOfIDCheckQueue = sum1 / numberOfTraveler
    avgtimeOfScanQueue = sum2 / numberOfTraveler
    avgtimeOfTotal = sum3 / numberOfTraveler
    return avgtimeOfIDCheckQueue, avgtimeOfScanQueue, avgtimeOfTotal


inf = float("inf")


def expectationOfXRay(x):
    return (1 / (np.sqrt(2 * np.pi) * 6.9)) * np.exp(-((x - 5.9) ** 2) / (2 * 6.9 ** 2))


def expectationOfMM(x):
    return (1 / (np.sqrt(2 * np.pi) * 5.7)) * np.exp(-((x - 11.6) ** 2) / (2 * 5.7 ** 2))


f1 = integrate.quad(expectationOfXRay, 0, inf)
f2 = integrate.quad(expectationOfMM, 0, inf)


def tempfunc(x):
    return (f1[0] * expectationOfXRay(x) + f2[0] * expectationOfMM(x)) * x


S2 = integrate.quad(tempfunc, 0, inf)

xs = np.arange(50, 4000, 100)  # 模拟乘客数量的增长
ysOfID = []  # 仿真得到的数据
ysOfScan = []
ysOfTotal = []
thOfId = []  # 理论的数据
thOfScan = []
thOfTotal = []
for x in xs:
    data = function(x, 1, 1, False)
    ysOfID.append(data[0])
    ysOfScan.append(data[1])
    ysOfTotal.append(data[2])
    thOfId.append((x - 1) / 2 * (11.2 - 1 / 3.7))
    thOfScan.append((x - 1) / 2 * (S2[0] - 11.2 + valueOfTakeoff(False)[0]))
    thOfTotal.append((x - 1) / 2 * (valueOfTakeoff(False)[0] - 1 / 3.7) + (x + 1) / 2 * S2[0] + 11.2)

plt.figure(1)
plt.plot(xs, ysOfTotal, label="simulation")
plt.plot(xs, thOfTotal, label='theory', color='red')
plt.legend()
plt.title("Ttotal-number")
plt.xlabel("number")
plt.ylabel("Ttotal")
plt.figure(2)
plt.plot(xs, ysOfID, label="simulation")
plt.plot(xs, thOfId, label='theory', color='red')
plt.legend()
plt.title("TID-number")
plt.xlabel("number")
plt.ylabel("TId")
plt.figure(3)
plt.plot(xs, ysOfScan, label="simulation")
plt.plot(xs, thOfScan, label='theory', color='red')
plt.legend()
plt.title("Tscan-number")
plt.xlabel("number")
plt.ylabel("Tscan")
plt.show()
