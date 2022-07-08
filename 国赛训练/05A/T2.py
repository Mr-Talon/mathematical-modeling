import numpy as np
import pandas as pd

data = pd.read_excel("C:/Users/16046/Desktop/污染源.xlsx")

COD = np.array(data['CODMn'])  # 高锰酸盐 第二个维度是氨氮 单位：mg/L
NH3 = np.array(data['NH3-N'])  # 氨氮 单位：mg/L

distanceOfOri = [0, 950, 1728, 2123, 2623, 2787, 3251]  # 七个站点距离第一个站点的距离 单位：km
distance = [0]  # 七个站点的间隔距离  单位：km
for i in range(len(distanceOfOri) - 1):
    distance.append(distanceOfOri[i + 1] - distanceOfOri[i])

Q = np.array(data['水流量'])  # 水流量 单位：m^3/s

V = np.array(data['水流速'])  # 水流量 单位：m/s

degradation = 0.2  # 降解系数 单位：1/天

M = [COD * Q, NH3 * Q]  # 每个站点在不同月份 每秒通过的污染物的含量  单位：g/s
M = np.array(M).T

t = []  # 水流进过两个站点之间的时间  单位：天   形状：6*13=78
i = 0
for i in range(int(len(data) / 7)):
    for j in range(6):
        time = distance[j + 1] / (0.5 * (V[i * 7 + j] + V[i * 7 + j + 1]))  # 单位:1000*s
        t.append(time / 86.4)  # 单位：天
t = np.array(t)

p = []  # 每一个月每一个站点收到来自上一个站点的污染物   单位：g/s  形状：78*2
i = 0
j = 0
for i in range(int(len(data) / 7)):
    for j in range(6):
        get = M[i * 7 + j] * (1 - degradation) ** t[i * 6 + j]   # 每一个月只取M的前6个站点
        p.append(get)
p = np.array(p)

M_inside = []  # 每一个月每一个站点自身产生的污染物  第一个站点就是M  其他站点要减去来自上一个站点的污染物  单位：g/s   形状：91*2
i = 0
j = 0
for i in range(int(len(data) / 7)):
    M_inside.append(M[i * 7])
    for j in range(6):
        M_inside.append(M[i * 7 + j + 1] - p[i * 6 + j])
M_inside = np.array(M_inside)

i = 0
j = 0
sum = np.zeros([7,2])    # 每个站点 13个月 自身产生的两种污染物的平均值  单位：g/s
for i in range(int(len(data) / 7)):
    for j in range(7):
        sum[j]+=M_inside[i*7+j]
print(sum/13)
# print("\n")
#
# i = 0
# j = 0
# sum = np.zeros([7,2])    # 每个站点 13个月 自身产生的两种污染物的平均值  单位：g/s
# for i in range(int(len(data) / 7)):
#     for j in range(7):
#         sum[j]+=M[i*7+j]
# print(sum/13)