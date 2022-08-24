import math
import numpy as np
import pandas as pd

data = pd.read_excel("C:/Users/16046/Desktop/data.xlsx")

latitude = 40 / 180 * math.pi  # 当地纬度
# S_north = 59.7 / 180 * math.pi  # 北斜面角度
S_south = 35.9 / 180 * math.pi  # 南斜面角度
S0 = 1367  # 太阳常数
rho = 0.2  # 地面反射率

w = []  # 时角
ws = []  # 日落时角
delta = []  # 赤纬角
# Rb_north = []  # 倾斜面与水平面上直接辐射量之比 北斜面
Rb_south = []  # 倾斜面与水平面上直接辐射量之比 南斜面
H0 = []  # 大气层外水平面上太阳辐射量
ts = np.array(data["实际时间"])  # 太阳时
n = np.array(data["日期差"])  # 日期差n

# HT_north = []  # 倾斜面上太阳辐射量 北斜面
HT_south = []  # 倾斜面上太阳辐射量 南斜面
Hb = np.array(data["水平面直接辐射强度"])
Hd = np.array(data["水平面散射辐射强度"])
H = np.array(data["水平面总辐射强度"])

for i in range(len(data)):
    w_i = 15 * (ts[i] - 12) / 180 * math.pi
    delta_i = 23.45 * math.sin(2 * math.pi * (284 + n[i]) / 365) / 180 * math.pi
    ws_i = math.acos(-math.tan(latitude) * math.tan(delta_i))  # 此处的ws为弧度制 下面的ws应该换算成角度制
    wst_i_south= min(ws_i,math.acos(-math.tan(latitude-S_south)*math.tan(delta_i)))
    # wst_i_north = min(ws_i, math.acos(-math.tan(latitude - S_north) * math.tan(delta_i)))

    Rb_south_i = (math.cos(latitude - S_south) * math.cos(delta_i) * math.sin(wst_i_south) + wst_i_south * math.sin(latitude - S_south) * math.sin(delta_i)) \
                 / (ws_i * math.sin(latitude) * math.sin(delta_i) + math.cos(latitude) * math.cos(delta_i) * math.sin(ws_i))

    # Rb_north_i = (math.cos(latitude - S_north) * math.cos(delta_i) * math.sin(wst_i_north) + wst_i_north * math.sin(latitude - S_north) * math.sin(delta_i)) \
    #              / (ws_i * math.sin(latitude) * math.sin(delta_i) + math.cos(latitude) * math.cos(delta_i) * math.sin(ws_i))

    H0_i = 24 / math.pi * S0 * (1 + 0.033 * 360 / 365 * n[i]) * \
           (math.cos(latitude) * math.cos(delta_i) * math.sin(ws_i) + math.pi/ 180 * ws_i * 180 / math.pi * math.sin(latitude) * math.sin(delta_i))

    HT_south_i = Hb[i] * Rb_south_i + Hd[i] * (Hb[i] / H0_i * Rb_south_i + 0.5 * (1 - Hb[i] / H0_i) * (1 + math.cos(S_south))) \
                 + 0.5 * rho * H[i] * (1 - math.cos(S_south))

    # HT_north_i = Hb[i] * Rb_north_i + Hd[i] * (Hb[i] / H0_i * Rb_north_i + 0.5 * (1 - Hb[i] / H0_i) * (1 + math.cos(S_north))) \
    #              + 0.5 * rho * H[i] * (1 - math.cos(S_north))

    w.append(w_i)
    delta.append(delta_i)
    Rb_south.append(Rb_south_i)
    # Rb_north.append(Rb_north_i)
    ws.append(ws_i)
    H0.append(H0_i)

    HT_south.append(HT_south_i)
    # HT_north.append(HT_north_i)

w = np.array(w)
delta = np.array(delta)
Rb_south = np.array(Rb_south)
# Rb_north = np.array(Rb_north)
ws = np.array(ws)
H0 = np.array(H0)
# HT_north = np.array(HT_north)
HT_south = np.array(HT_south)

# data1 = pd.DataFrame(data=HT_north)
data2 = pd.DataFrame(data=HT_south)
# data1.to_csv('north1.csv')
data2.to_csv('south35.9.csv')
