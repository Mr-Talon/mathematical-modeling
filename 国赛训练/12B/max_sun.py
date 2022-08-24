import math
import numpy as np
import pandas as pd

data = pd.read_excel("C:/Users/16046/Desktop/data.xlsx")

latitude = 40 / 180 * math.pi  # 当地纬度
S0 = 1367  # 太阳常数
rho = 0.2  # 地面反射率

ts = np.array(data["实际时间"])  # 太阳时
n = np.array(data["日期差"])  # 日期差b
Hb = np.array(data["水平面直接辐射强度"])
Hd = np.array(data["水平面散射辐射强度"])
H = np.array(data["水平面总辐射强度"])


def fun(S):
    S = S / 180 * math.pi
    HT_south = 0

    for i in range(len(data)):
        delta_i = 23.45 * math.sin(2 * math.pi * (284 + n[i]) / 365) / 180 * math.pi
        ws_i = math.acos(-math.tan(latitude) * math.tan(delta_i))  # 此处的ws为弧度制 下面的ws应该换算成角度制
        wst_i_south = min(ws_i, math.acos(-math.tan(latitude - S) * math.tan(delta_i)))

        Rb_south_i = (math.cos(latitude - S) * math.cos(delta_i) * math.sin(wst_i_south) + wst_i_south * math.sin(
            latitude - S) * math.sin(delta_i)) \
                     / (ws_i * math.sin(latitude) * math.sin(delta_i) + math.cos(latitude) * math.cos(
            delta_i) * math.sin(ws_i))

        H0_i = 24 / math.pi * S0 * (1 + 0.033 * 360 / 365 * n[i]) * \
               (math.cos(latitude) * math.cos(delta_i) * math.sin(
                   ws_i) + math.pi / 180 * ws_i * 180 / math.pi * math.sin(latitude) * math.sin(delta_i))

        HT_south_i = Hb[i] * Rb_south_i + Hd[i] * (
                Hb[i] / H0_i * Rb_south_i + 0.5 * (1 - Hb[i] / H0_i) * (1 + math.cos(S))) \
                     + 0.5 * rho * H[i] * (1 - math.cos(S))

        HT_south=HT_south+HT_south_i

    return HT_south


HT_all = []
for i in range(290,400,1):
    degree=i/10
    print(degree)
    HT = fun(degree)
    HT_all.append(HT)
HT_all = np.array(HT_all)
HT_data = pd.DataFrame(data=HT_all)
HT_data.to_csv("寻找细.csv")
