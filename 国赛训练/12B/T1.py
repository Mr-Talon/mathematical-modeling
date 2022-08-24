import math
import numpy as np
import pandas as pd

data1 = pd.read_excel("C:/Users/16046/Desktop/B/附件5.xlsx")  # 逆变器的数据
data2 = pd.read_excel("C:/Users/16046/Desktop/B/cumcm2012B_附件3_三种类型的光伏电池(A单晶硅B多晶硅C非晶硅薄膜)组件设计参数和市场价格.xls")  # 电池数据

# square = [2811900, 19970000, 18540000, 22720000, 60785133, 14031324]  # 房屋6个面的面积  北 东 南 西 南斜 北斜
# square = np.array(square)

square35 = [60785133]  # 南斜
square = np.array(square35)

square_battery = np.array(data2["面积"])  # 平方毫米

U_low = np.array(data1["允许输入电压下界（V）"])
U_up = np.array(data1["允许输入电压上界（V）"])
U_battery = np.array(data2["开路电压（Voc）"])

I_battery = np.array(data2["短路电流（Isc/A）"])
I = np.array(data1["输入额定电流（A）"])

P = np.array(data1["输出额定功率（KW）"])
P = P * 1000  # 换算成 w
P_battery = np.array(data2["组件功率（w)"])

answer = []

for surface in square:
    for i in range(18):  # 逆转器
        for j in range(24):  # 电池
            if I_battery[j] > I[i]:
                continue
            if U_battery[j] > U_up[i]:
                continue
            if P_battery[j] > P[i]:
                continue

            ymax = math.floor(I[i] / I_battery[j])  # y的最大值
            xmin = math.ceil(U_low[i] / U_battery[j])  # x的最小值
            xmax = math.floor(U_up[i] / U_battery[j])  # x的最大值

            for y in range(1, ymax + 1):
                for x in range(xmin, xmax + 1):
                    if (x * y * square_battery[j]*math.cos(10.62/180*math.pi)/math.cos(35.9/180*math.pi) <= surface) & (x * y * P_battery[j] <= P[i]):
                        answer.append((i + 1, j + 1, x, y, np.where(square == surface)))

answer = np.array(answer)
print(answer.shape)
print(answer[:5])
print(answer[-5:])

answer = pd.DataFrame(data=answer)
answer.to_csv("answer35.9.csv")
