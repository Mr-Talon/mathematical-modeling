import pandas as pd
import numpy as np

gate = pd.read_excel("C:/Users/16046/Desktop/2018年F题/登机口数据.xlsx")
flight = pd.read_excel("C:/Users/16046/Desktop/2018年F题/航班数据.xlsx")

arrival_flight = np.array(flight["到达类型"])
departure_flight = np.array(flight["出发类型"])
type_flight = np.array(flight["航班种类"])
arrival_gate = np.array(gate["到达类型"])
departure_gate = np.array(gate["出发类型"])
type_gate = np.array(gate["机体类别"])

P = np.zeros((len(flight), len(gate)))

for i in range(len(flight)):
    for j in range(len(gate)):
        # 到达类型匹配
        if ((arrival_flight[i] == 1) & (arrival_gate[j] == 2)) | ((arrival_flight[i] == 2) & (arrival_gate[j] == 1)):
            continue

        # 出发类型匹配
        if ((departure_flight[i] == 1) & (departure_gate[j] == 2)) | ((departure_flight[i] == 2) & (departure_gate[j] == 1)):
            continue

        # 机体类型匹配
        if type_flight[i] != type_gate[j]:
            continue

        P[i][j]=1

P=pd.DataFrame(data=P)
P.to_excel("P.xlsx")