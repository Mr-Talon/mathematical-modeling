import folium
import pandas as pd
from folium.plugins import HeatMap
import numpy as np

data = pd.read_excel('test.xlsx')
colum=[column for column in data]
# print(len(colum))
lst_data = data.values.tolist()
# print(lst_data[0])
LOC = []
for i in range(len(colum)):
    LOC.append([colum[i], lst_data[0][i]])
print(LOC)

Center = [0,10]
m = folium.Map(location=Center, zoom_start=6)
HeatMap(LOC).add_to(m)
name = 't.html'
m.save(name)
