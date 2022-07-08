import pandas as pd
import numpy as np

data = pd.read_excel("C:/Users/16046/Desktop/task1.xlsx")

data1 = np.array(data['红组1总评分'])[0:270, ]
data2 = np.array(data['红组2总评分'])[0:270, ]
data3 = np.array(data['白组1总评分'])
data4 = np.array(data['白组2总评分'])

mean1 = []
mean2 = []
mean3 = []
mean4 = []
var1 = []
var2 = []
var3 = []
var4 = []

for i in range(0, len(data1), 10):
    mean1.append(data1[i:i + 10, ].mean())
    var1.append(data1[i:i + 10, ].var())

for i in range(0, len(data2), 10):
    mean2.append(data2[i:i + 10, ].mean())
    var2.append(data2[i:i + 10, ].var())

for i in range(0, len(data3), 10):
    mean3.append(data3[i:i + 10, ].mean())
    var3.append(data3[i:i + 10, ].var())

for i in range(0, len(data4), 10):
    mean4.append(data4[i:i + 10, ].mean())
    var4.append(data4[i:i + 10, ].var())

var1 = np.array(var1)
var2 = np.array(var2)
var3 = np.array(var3)
var4 = np.array(var4)

print("红组1：")
print(mean1)
print(var1)

print("红组2：")
print(mean2)
print(var2)

print("白组1：")
print(mean3)
print(var3)

print("白组2：")
print(mean4)
print(var4)

print("红组1：" + str(var1.mean()))
print("红组2：" + str(var2.mean()))
print("白组1：" + str(var3.mean()))
print("白组2：" + str(var4.mean()))
