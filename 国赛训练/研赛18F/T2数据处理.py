import numpy as np
import pandas as pd

flight = pd.read_excel("C:/Users/16046/Desktop/2018年F题/航班数据raw.xlsx")
traveler = pd.read_excel("C:/Users/16046/Desktop/2018年F题/旅客数据.xlsx")

traveler_arrive = np.array(traveler["到达航班"])
traveler_arrive_date = np.array(traveler["到达日期"])
traveler_departure = np.array(traveler["出发航班"])
traveler_departure_date = np.array(traveler["出发日期"])

flight_arrive_id = np.array(flight["到达航班"])
flight_arrive_date = np.array(flight["到达日期"])
flight_arrive_time = np.array(flight["到达分钟差"])
flight_arrive_type = np.array(flight["到达类型"])

flight_departure_id = np.array(flight["出发航班"])
flight_departure_date = np.array(flight["出发日期"])
flight_departure_time = np.array(flight["出发分钟差"])
flight_departure_type = np.array(flight["出发类型"])

flight_type = np.array(flight["航班种类"])

arrive_info = []
for i in range(len(traveler_arrive)):
    id = traveler_arrive[i]
    date = traveler_arrive_date[i]
    for j in range(len(flight_arrive_id)):
        if (id == flight_arrive_id[j]) & (date == flight_arrive_date[j]):
            arrive_info.append([flight_arrive_time[j], flight_arrive_type[j], flight_type[j]])
            break
        if j == len(flight_arrive_id) - 1:
            print(str(i)+"未找到（到达）")
            arrive_info.append([0, 0, 0])

departure_info = []
for i in range(len(traveler_departure)):
    id = traveler_departure[i]
    date = traveler_departure_date[i]
    for j in range(len(flight_departure_id)):
        if (id == flight_departure_id[j]) & (date == flight_departure_date[j]):
            departure_info.append([flight_departure_time[j], flight_departure_type[j]])
            break
        if j == len(flight_arrive_id) - 1:
            print(str(i) + "未找到（出发）")
            departure_info.append([0,0])

arrive_info = np.array(arrive_info)
departure_info = np.array(departure_info)

data=pd.DataFrame({
    "到达时间":arrive_info[:,0],
    "到达类型":arrive_info[:,1],
    "飞机种类":arrive_info[:,2],
    "出发时间":departure_info[:,0],
    "出发类型":departure_info[:,1],
})
data.to_excel("traveler.xlsx")
