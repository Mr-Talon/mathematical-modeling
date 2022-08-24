import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.preprocessing import MinMaxScaler

import torch.nn as nn
import torch
from torch.utils.data import Dataset, DataLoader

matplotlib.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

'''数据读取与数据处理'''
# 读取数据 划分训练集测试集
data = pd.read_excel("C:/Users/16046/Desktop/data.xlsx").astype('float32')
data = np.array(data).reshape(-1)
test_data_rate = 0.2
train_data = data[:-int(len(data) * test_data_rate)]
test_data = data[-int(len(data) * test_data_rate):]

# 数据标准化
scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data.reshape(-1, 1))
train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)

# 形成 特征标签对
class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)


train_window = 12  # 超参数（序列长度）
batch_size = 128  # 批量大小
device = torch.device('cuda:0')


def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L - tw):
        train_seq = input_data[i:i + tw]
        train_label = input_data[i + tw:i + tw + 1]
        inout_seq.append((train_seq, train_label))

    inout_seq = MyDataset(inout_seq)
    inout_seq = DataLoader(dataset=inout_seq, batch_size=batch_size, shuffle=True, num_workers=0, drop_last=True)
    return inout_seq


train_inout_seq = create_inout_sequences(train_data_normalized, train_window)

'''模型定义'''
# rnn架构
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size, batch_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.output_size = output_size
        self.num_directions = 1  # 单向LSTM
        self.batch_size = batch_size
        self.lstm = nn.LSTM(self.input_size, self.hidden_size, self.num_layers, batch_first=True)
        self.linear = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, input_seq):
        batch_size, seq_len = input_seq[0], input_seq[1]
        h_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(device)
        c_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(device)
        # output(batch_size, seq_len, num_directions * hidden_size)
        output, _ = self.lstm(input_seq, (h_0, c_0))
        pred = self.linear(output)
        pred = pred[:, -1, :]
        return pred


# 模型超参数
input_size = 1  # 时间序列就是1  多变量时间序列就是变量个数   文本就是词嵌入向量长度
hidden_size = 128
num_layers = 1  # rnn深度
output_size = 1
weight_decay = 0.9
model = LSTM(input_size, hidden_size, num_layers, output_size, batch_size).to(device)
loss_function = nn.MSELoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=weight_decay)
epochs = 300

print("training...")
for i in range(epochs):
    for seq, labels in train_inout_seq:
        seq = seq.to(device)
        label = labels.to(device)
        optimizer.zero_grad()
        y_pred = model(seq)
        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

        if i % 25 == 0:
            print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')



# fut_pred = 10
#
# test_inputs = train_data_normalized[-train_window:].tolist()
#
# model.eval()
#
# for i in range(fut_pred):
#     seq = torch.FloatTensor(test_inputs[-train_window:])
#     with torch.no_grad():
#         model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
#                         torch.zeros(1, 1, model.hidden_layer_size))
#         test_inputs.append(model(seq).item())
#
# actual_predictions = scaler.inverse_transform(np.array(test_inputs[train_window:]).reshape(-1, 1))
# print(actual_predictions)
#
# print(sum(actual_predictions - data[-10:0]) ** 2)
#
# x = np.arange(96, 104, 1)
# print(x)
# plt.title('Month vs Passenger')
# plt.ylabel('Total Passengers')
# plt.grid(True)
# plt.autoscale(axis='x', tight=True)
# plt.plot(data)
# plt.plot(x, actual_predictions)
# plt.show()
