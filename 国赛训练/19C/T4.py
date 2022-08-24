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


def mu(flight, service, rate):
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


def income(s):
    C1 = 11  # 起步价
    S1 = 3  # 起步价距离
    C2 = 2  # 超过起步价之后的价钱
    if s < S1:
        return C1
    else:
        return C1 + C2 * (s - S1)


def A(W, v2):
    s = 41  # 从机场到市中心的距离
    money = income(s)  # 将旅客从机场带到市中心的收入
    oil = 0.65 * s  # 0.65为每公里 油价
    ans = np.array((money - oil) / (W + s / v2))
    return ans


def cal_t(l, w_long, W, v1):
    # l为短途距离
    s = 41
    W_short = income(l)
    W_long = income(s)
    oil = 2 * 0.65 * l + 0.65 * s
    ans = np.array((W_short + W_long - oil) / w_long - W - (2 * l / v1) - s / v1)
    return ans[0]


lambda_t = taxi
v1 = 70  # 出租车的平均速度
v2 = 40  # 出租车市区速度

rho = lambda_t / mu(flight, service=1 / 60, rate=0.5)
# W = Wq(rho, s=2)
W = np.array([1.5] * 12)
w_long = A(W, v2)  # 长途单位之间利润
# t=cal_t(21,w_long,W,v1)[:1]


ans1 = []
for i in range(5, 106):
    l = i / 10
    t1 = cal_t(l, w_long, W, v1)
    ans1.append(t1)
ans1 = np.array(ans1)
print(ans1)
# print(np.mean(ans1) * 60)

ans2 = []
for i in range(105, 206):
    l = i / 10
    t1 = cal_t(l, w_long, W, v1)
    ans2.append(t1)
ans2 = np.array(ans2)
print(ans2)
# print(np.mean(ans2) * 60)

data = pd.DataFrame({
    "0.5-10": ans1,
    "10.5-20": ans2
})
data.to_csv("data.csv")


print(np.mean(np.append(ans1,ans2))*60)