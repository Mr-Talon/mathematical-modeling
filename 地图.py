import folium
import pandas as pd
from folium.plugins import HeatMap
import numpy as np

data = pd.read_excel('test.xlsx')
lst_data = data.values.tolist()

LNG = []  # 经度
LAT = []  # 纬度
t = 72.5
for i in range(22):
    LAT.append(t)
    t -= 1
t=-17.5
for i in range(29):
    LNG.append(t)
    t += 1
LOC = []
for i in range(22):
    for j in range(29):
        if lst_data[i][j]>100:
            continue
        else:
            LOC.append([LAT[i], LNG[j], lst_data[i][j]])
print(LOC)

Center = [np.mean(np.array(LAT, dtype='float32')), np.mean(np.array(LNG, dtype='float32'))]
m = folium.Map(location=Center, zoom_start=6)
HeatMap(LOC).add_to(m)
name = '1891.html'
m.save(name)
