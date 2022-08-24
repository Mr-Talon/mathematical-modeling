import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 15

flight_data = pd.read_excel("C:/Users/16046/Desktop/4-18进港航班数量.xlsx")
flight = np.array(flight_data["两小时"])[:12]  # 每两小时航班到达数量
taxi = pd.read_excel("C:/Users/16046/Desktop/出租车数据.xlsx")
taxi = np.array(taxi["两小时"] / 2)[:12]  # 每两小时出租车到达数

'''
超参数表：

mu函数：
rate 选择乘坐出租车的比例
T_service 乘客放行李上车时间——服务时间

Wq函数：
s 车道数

A;B函数:
minute: 表示城区一单多少分钟
'''


def mu(flight,service,rate):
    k = [1, 1, 1, rate, rate, rate, rate, rate, rate, rate, rate, (1 + rate) / 2]
    k = np.array(k)  # 乘坐出租车的比例  夜间地铁停运只能选择出租车
    n = 150  # 每架飞机的旅客数
    Np = k * n * flight
    T_service = service

    mu = []

    for Np_t in Np:
        if Np_t / 2 < 1 / T_service:
            mu.append(Np_t)
        else:
            mu.append(1 / T_service)
    mu = np.array(mu)
    return mu


def Wq(rho, s):
    W = []
    for rho_t in rho:
        # 计算P0
        t = 0
        for n in range(s):
            t += rho_t ** n / math.factorial(n) + rho_t ** s / (math.factorial(s) * (1 - rho_t / s))
        P0 = 1 / t

        # 计算Lq
        Lq = P0 * rho_t ** s * rho_t / s / (math.factorial(s) * (1 - rho_t / s) ** 2)

        # 计算W
        if Lq + rho_t >= 0:
            W.append(Lq + rho_t)
        else:
            W.append(0)

    W = np.array(W)
    return W


# def income_list(s):
#     C1 = 11  # 起步价
#     S1 = 3  # 起步价距离
#     C2 = 2  # 超过起步价之后的价钱
#     money = []
#     for s_t in s:
#         if s_t < S1:
#             money.append(C1)
#         else:
#             money.append(C1 + C2 * (s - S1))
#     return np.array(money)


def income(s):
    C1 = 11  # 起步价
    S1 = 3  # 起步价距离
    C2 = 2  # 超过起步价之后的价钱
    if s < S1:
        return C1
    else:
        return C1 + C2 * (s - S1)


def A(W, v2, minute=20):
    s = 41  # 从机场到市中心的距离
    money = income(s)  # 将旅客从机场带到市中心的收入
    oil = 0.65 * s  # 0.65为每公里 油价
    wait = W // (minute / 60) * income(v2 * minute / 60)  # 等待时间的长度一般市中心旅客   假设市区一单20分钟
    ans = np.array(money - oil - wait)
    return ans


def B(W, v1, v2, incomeA,minute=20):
    s = 41 + (W * v2)
    oil = 0.65 * s
    money = W // (minute / 60) * income(v2 * minute / 60)  # 假设市区一单20分钟
    E = []
    for i in range(len(W)):
        if W[i] < 41 / v1:
            E.append((41 / v1 - W[i]) * incomeA[i] / (41 / v1))
        else:
            E.append(0)
    E=np.array(E)
    ans = money - oil - E
    return ans


lambda_t = taxi
v1 = 70  # 出租车的平均速度
v2 = 40  # 出租车市区速度


'''正常结果'''
# rho = lambda_t / mu(flight,service=1/60,rate=0.5)
# W = Wq(rho, s=2)
# incomeA = A(W, v2,minute=20)
# incomeB = B(W, v1, v2, incomeA,minute=20)
# choose = []
# for i in range(len(incomeA)):
#     if incomeA[i] > incomeB[i]:
#         choose.append(True)
#     else:
#         choose.append(False)
#
# plt.figure("2")
# plt.xlabel('时间段（2小时一段）')
# plt.ylabel('收入差/元')
# plt.title('各时间段方案B与方案A的收入差')
# plt.axis([0, 13, -250, 1050])
# plt.grid(True)
# x=np.arange(1,13)
# plt.plot(x, incomeB-incomeA, '-.')
# plt.legend()
# plt.show()


'''灵敏度分析'''
# 不同rate的选择

ans=[]
for s in range(2,11):
    rho = lambda_t / mu(flight,service=1/60,rate=0.5)
    W = Wq(rho, s=s)
    incomeA = A(W, v2,minute=20)
    incomeB = B(W, v1, v2, incomeA,minute=20)
    choose = []
    for j in range(len(incomeA)):
        if incomeA[j] > incomeB[j]:
            choose.append(True)
        else:
            choose.append(False)

    print(choose)
    ans.append(W)

ans=np.array(ans)

plt.figure("2")
plt.xlabel('时间段（2小时一段）')
plt.ylabel('收益/元')
plt.title('不同k对等待时间的影响')
plt.axis([0, 13, -1, 10])
plt.grid(True)
x=np.arange(1,13)
for i in range(len(ans)):
    plt.plot(x, ans[i], '-.',label="k="+str(i+2))
plt.legend()
plt.show()