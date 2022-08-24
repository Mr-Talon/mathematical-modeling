import numpy as np
import pandas as pd
import datetime

data = pd.read_excel("C:/Users/16046/Desktop/2018年F题/航班数据raw.xlsx")

# flight=np.array(data["飞机型号"])
# wide=[332,333,"33E","33H","33L",773]
# narrow=[319,320,321,323,325,738,"73A","73E","73H","73L"]
#
# data_change=[]
# for i in flight:
#     if i in wide:
#         data_change.append('W')
#     elif i in narrow:
#         data_change.append("N")
#
# data_change=np.array(data_change)
# data_change=pd.DataFrame(data=data_change)
# data_change.to_csv("航班种类.csv")

arrival = np.array(data["到达日期时间"])
departure = np.array(data["出发日期时间"])
time=zip(arrival,departure)

arrival_time_list = []
departure_time_list = []
for arrival_time,departure_time in time:
    arrival_time=str(arrival_time)
    departure_time=str(departure_time)
    arrival_time_i = datetime.datetime.strptime(arrival_time, "%Y/%m/%d %H:%M")
    departure_time_i = datetime.datetime.strptime(departure_time, "%Y/%m/%d %H:%M")
    arrival_time_list.append(arrival_time_i)
    departure_time_list.append(departure_time_i)

time_flag=datetime.datetime(2018,1,19,0,0,0)

time_m_arrival=[]
time_m_departure=[]
for i in range(len(arrival_time_list)):
    delta1=arrival_time_list[i]-time_flag
    day1=delta1.days
    seconds1=delta1.seconds
    time_m_arrival.append(day1*24*60+seconds1/60)

    delta2 = departure_time_list[i] - time_flag
    day2 = delta2.days
    seconds2 = delta2.seconds
    time_m_departure.append(day2 * 24 * 60 + seconds2 / 60)

time_m_arrival=pd.DataFrame(data=time_m_arrival)
time_m_departure=pd.DataFrame(data=time_m_departure)
time_m_arrival.to_excel("到达分钟差.xlsx")
time_m_departure.to_excel("出发分钟差.xlsx")