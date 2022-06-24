import numpy
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import folium
from folium.plugins import HeatMap

data = pd.read_excel('1891-2022海温.xlsx')
# print(data)    493
# data.dropna(axis=1, inplace=True)  # 删除陆地的数据
data = np.array(data).T  # 让矩阵的每一行是一个小区域所有年份的数据

# 记录不同年份9月的预测数据
LOC_2021 = []
LOC_2031 = []
LOC_2041 = []
LOC_2051 = []
LOC_2061 = []
LOC_2071 = []
LNG_start = -17.5  # 经度
LAT_start = 67.5  # 纬度
totaldata = []  # 记录所有预测数据
namelist=[]
# 记录3个栅格2011-2071 九月的温度
LOC_1 = []
LOC_2 = []
LOC_3 = []
'''
用前12个月的数据观察后一个月的数据，这13个数据一起写入一个列表里面
'''


def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L - tw):
        train_seq = input_data[i:i + tw]
        train_label = input_data[i + tw:i + tw + 1]
        inout_seq.append((train_seq, train_label))
    return inout_seq


class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1, 1, self.hidden_layer_size),
                            torch.zeros(1, 1,
                                        self.hidden_layer_size))  # (num_layers * num_directions, batch_size, hidden_size)

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq), 1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]


for t in range(17):
    LAT = LAT_start - t
    for j in range(29):
        LNG = LNG_start + j
        t=9
        j=17
        print(t * 29 + j)
        zoom_data = data[t * 29 + j]  # 读取数据
        if zoom_data[0] > 100:
            continue
        else:
            testDataSize = 0  # 设置测试集大小
            train_data = zoom_data
            test_data = zoom_data[-testDataSize:]

            # 归一化数据
            scaler = MinMaxScaler(feature_range=(-1, 1))
            train_data_normalized = scaler.fit_transform(train_data.reshape(-1, 1))
            train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)
            # print(train_data_normalized)

            train_window = 24  # 设置用多少个月的数据预测下一个月的数据
            train_inout_seq = create_inout_sequences(train_data_normalized, train_window)  # 生成feature label对
            # print(train_inout_seq[-5:])

            model = LSTM().to(torch.device('cuda'))
            loss = nn.MSELoss()  # 交叉熵损失
            optimizer = torch.optim.Adam(model.parameters(), lr=0.005)

            epochs = 700

            for i in range(epochs):
                for seq, labels in train_inout_seq:
                    seq = seq.to(torch.device('cuda'))
                    labels = labels.to(torch.device('cuda'))
                    optimizer.zero_grad()
                    model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size).to(torch.device('cuda')),
                                         torch.zeros(1, 1, model.hidden_layer_size).to(torch.device('cuda')))
                    y_pred = model(seq)
                    single_loss = loss(y_pred, labels)
                    single_loss.backward()
                    optimizer.step()

                if i % 5 == 1:
                    print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

            print(f'epoch: {i:3} loss: {single_loss.item():10.10f}')

            fut_pred = 600
            test_inputs = train_data_normalized[-train_window:].tolist()  # 选出训练集最后12个月的数据来预测之后的值，也就是测试集第一个数据

            # 预测
            model.eval()
            for i in range(fut_pred):
                seq = torch.FloatTensor(test_inputs[-train_window:])
                seq = seq.to(torch.device('cuda'))
                with torch.no_grad():
                    model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                                    torch.zeros(1, 1, model.hidden_layer_size))
                    test_inputs.append(model(seq).item())

            # print(test_inputs[-fut_pred:])
            # 由于一开始对数据进行了标准化 所以这边用反运算得到真正的预测值
            actual_predictions = scaler.inverse_transform(np.array(test_inputs[train_window:]).reshape(-1, 1))
            temp=[]
            for m in range(600):
                temp.append(actual_predictions[m][0])
            totaldata.append(temp)
            namelist.append(str(LAT)+str(LNG))

            predict71 = actual_predictions[-4][0]  # 2071年9月的数据
            # print([LAT, LNG, predict71])
            LOC_2071.append([LAT, LNG, predict71])
            LOC_2071.append([0, 0, 18])  # 添加一个基准点

            predict61 = actual_predictions[-124][0]  # 2061年9月的数据
            # print([LAT, LNG, predict61])
            LOC_2061.append([LAT, LNG, predict61])
            LOC_2061.append([0, 0, 18])  # 添加一个基准点

            predict51 = actual_predictions[-244][0]  # 2051年9月的数据
            # print([LAT, LNG, predict51])
            LOC_2051.append([LAT, LNG, predict51])
            LOC_2051.append([0, 0, 18])  # 添加一个基准点

            predict41 = actual_predictions[-364][0]  # 2041年9月的数据
            # print([LAT, LNG, predict41])
            LOC_2041.append([LAT, LNG, predict41])
            LOC_2041.append([0, 0, 18])  # 添加一个基准点

            predict31 = actual_predictions[-484][0]  # 2031年9月的数据
            # print([LAT, LNG, predict31])
            LOC_2031.append([LAT, LNG, predict31])
            LOC_2031.append([0, 0, 18])  # 添加一个基准点

            data21 = train_data[-4]  # 2021年9月的数据
            # print([LAT, LNG, data21])
            LOC_2021.append([LAT, LNG, data21])
            LOC_2021.append([0, 0, 18])  # 添加一个基准点

            # 绘制三个栅格每年9月份的数据
            if t == 9 and j == 17:
                data2011 = train_data[-120:]
                month=8
                while month<120:
                    LOC_1.append(data2011[month])
                    month+=12
                month = 8
                while month < 600:
                    LOC_1.append(actual_predictions[month][0])
                    month += 12
                break

            if t == 4 and j == 13:
                data2011 = train_data[-120:]
                month = 8
                while month < 120:
                    LOC_2.append(data2011[month])
                    month += 12
                month = 8
                while month < 600:
                    LOC_2.append(actual_predictions[month][0])
                    month += 12

            if t == 7 and j == 9:
                data2011 = train_data[-120:]
                month = 8
                while month < 120:
                    LOC_3.append(data2011[month])
                    month += 12
                month = 8
                while month < 600:
                    LOC_3.append(actual_predictions[month][0])
                    month += 12
    break

x = numpy.arange(2011, 2071, 1)
plt.title('temp predict of 3 zooms in Sep')
plt.ylabel('temp')
plt.grid(True)
plt.autoscale(axis='x', tight=True)
plt.plot(x, LOC_1)
# plt.plot(x, LOC_2)
# plt.plot(x, LOC_3)
plt.show()

# 绘制热力图
m71 = folium.Map(zoom_start=6)
HeatMap(LOC_2071).add_to(m71)
name = '2071.html'
m71.save(name)

m61 = folium.Map(zoom_start=6)
HeatMap(LOC_2071).add_to(m61)
name = '2061.html'
m61.save(name)

m51 = folium.Map(zoom_start=6)
HeatMap(LOC_2071).add_to(m51)
name = '2051.html'
m51.save(name)

m41 = folium.Map(zoom_start=6)
HeatMap(LOC_2071).add_to(m41)
name = '2041.html'
m41.save(name)

m31 = folium.Map(zoom_start=6)
HeatMap(LOC_2071).add_to(m31)
name = '2031.html'
m31.save(name)

m21 = folium.Map(zoom_start=6)
HeatMap(LOC_2071).add_to(m21)
name = '2021.html'
m21.save(name)

all_data=pd.DataFrame(columns=namelist,data=np.array(totaldata).T)
all_data.to_csv('data.csv')