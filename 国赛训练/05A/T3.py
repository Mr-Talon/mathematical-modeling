import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 10


def func(t):  # 污水排放回归方程
    return 12.864 * t + 149


average = 9894.106


def fuc11(t):  # 一类全流域
    return 96.839641 - 0.148919 * func(t) + 0.001581 * average


def fuc12(t):  # 一类干流
    return 115.864315 - 0.212051 * func(t) + 0.001328 * average


def fuc13(t):  # 一类支流
    return 115.925818 - 0.130349 * func(t) - 0.000974 * average


def fuc22(t):  # 二类干流
    return -5.493799 + 0.137599 * func(t) - 0.000993 * average


def fuc31(t):  # 三类全流域
    return -10.999802 + 0.091765 * func(t) - 0.000361 * average


def fuc32(t):  # 三类干流
    return -10.361764 + 0.074253 * func(t) - 0.000334 * average


def fuc33(t):  # 三类支流
    return -8.451039 + 0.084830 * func(t) - 0.000349 * average


x = np.arange(11, 21)
print("一类全流域：" + str(fuc11(x)) + "\n")
print("一类干流：" + str(fuc12(x)) + "\n")
print("一类支流：" + str(fuc13(x)) + "\n")

print("二类全流域：" + str(100 - fuc11(x) - fuc31(x)) + "\n")
print("二类干流：" + str(fuc22(x)) + "\n")
print("二类支流：" + str(100 - fuc13(x) - fuc33(x)) + "\n")

print("三类全流域：" + str(fuc31(x)) + "\n")
print("三类干流：" + str(fuc32(x)) + "\n")
print("三类支流：" + str(fuc33(x)) + "\n")

t = np.arange(1, 21)
# 前10年真实数据
t1 = np.arange(1, 11)
y11 = [93.1, 85.3, 80.7, 88.4, 80.2, 74, 73.7, 76.7, 77.5, 68]
y12 = [90.4, 99.2, 86.7, 100, 87.2, 74.5, 67.7, 68.8, 93.8, 67.5]
y13 = [95.3, 74.1, 75.9, 80.2, 76.2, 74, 75, 78.3, 74.3, 68.1]
y21 = [6.9, 11.6, 15.9, 10, 15.7, 21, 19.5, 13.2, 12.2, 20.7]
y22 = [9.6, 0.8, 13.3, 0, 12.8, 25.4, 26.5, 22.5, 6.1, 23.5]
y23 = [4.7, 20.3, 18, 17, 16.4, 20.1, 18, 11.3, 13.4, 20.1]
y31 = [0, 3.1, 3.4, 1.6, 4.1, 5.3, 6.8, 10, 10.3, 11.3]
y32 = [0, 0, 0, 0, 0, 0, 5.8, 8.7, 0, 9]
y33 = [0, 5.6, 6.2, 2.8, 5.1, 6.4, 7, 10.3, 12.3, 11.7]
plt.figure("1")
plt.xlabel('时间/年')
plt.ylabel('百分比')
plt.title('长江20年各级别水域变化图')
plt.axis([0, 22, -5, 105])
plt.grid(True)
plt.plot(t, fuc11(t), '-.', color='black', label="一类全流域、干流、支流占比预测曲线")
plt.plot(t, fuc12(t), '-.', color='black')
plt.plot(t, fuc13(t), '-.', color='black')

plt.plot(t, 100 - fuc11(t) - fuc31(t), '-+', color='black', label="二类全流域、干流、支流占比预测曲线")
plt.plot(t, fuc22(t), '-+', color='black')
plt.plot(t, 100 - fuc13(t) - fuc33(t), '-+', color='black')

plt.plot(t, fuc31(t), '-*', color='black', label="三类全流域、干流、支流占比预测曲线")
plt.plot(t, fuc32(t), '-*', color='black')
plt.plot(t, fuc33(t), '-*', color='black')

plt.scatter(t1, y11, color='red', label="一类全流域、干流、支流占比测量值")
plt.scatter(t1, y12, color='red')
plt.scatter(t1, y13, color='red')
plt.scatter(t1, y21, marker="+", color='orange', label="二类全流域、干流、支流占比测量值")
plt.scatter(t1, y22, marker="+", color='orange')
plt.scatter(t1, y23, marker="+", color='orange')
plt.scatter(t1, y31, marker="*", color='pink', label="三类全流域、干流、支流占比测量值")
plt.scatter(t1, y32, marker="*", color='pink')
plt.scatter(t1, y33, marker="*", color='pink')
plt.legend()
plt.show()
