import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import torch

matplotlib.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

'''数据划分部分'''
data = pd.read_csv()  # 已经清洗好的数据

# 数据归一化
quant_features = []  # 要归一化的列
scaled_features = {}  # 将每一个变量的均值和方差都存储到scaled_features变量中
for each in quant_features:
    mean, std = data[each].mean(), data[each].std()
    scaled_features[each] = [mean, std]
    data.loc[:, each] = (data[each] - mean) / std  # 求归一化结果并装载进data

# 数据划分
train_test_rate = 0.2  # 测试集在整个数据之间的占比  划分训练集测试集
train_data = data[:-len(data) * train_test_rate]
test_data = data[-len(data) * train_test_rate:]
print("训练数据：", len(train_data), "测试数据：", len(test_data))

label_column = []  # 数据的gt列   得到训练集和测试集的 特征 和 标签
features, labels = train_data.drop(label_column, axis=1), train_data[label_column]
test_features, test_targets = test_data.drop(label_column, axis=1), test_data[label_column]

X = features.values  # 取值
Y = labels.values  # 取值
Y = Y.astype(float)  # 转化格式
Y = np.reshape(Y, [len(Y), 1])  # 【16875，】转变为【16875，1】


'''模型训练部分'''
# 模型超参数
input_size = features.shape[1]
hidden_size = 10
output_size = 1
batch_size = 128
lr=0.01
epochs=1000

net = torch.nn.Sequential(
    torch.nn.Linear(input_size, hidden_size),
    torch.nn.ReLU(),
    torch.nn.Linear(hidden_size, output_size),
)
loss = torch.nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(), lr=lr)
losses = []

for i in range(epochs):
    # 使用小批量随机梯度下降
    batch_loss = []
    # start和end分别是提取一个batch数据的起始和终止下标
    for start in range(0, len(X), batch_size):
        end = start + batch_size if start + batch_size < len(X) else len(X)

        xx = torch.tensor(X[start:end], dtype=torch.float, requires_grad=True)   # xx为一个小批量的特征
        yy = torch.tensor(Y[start:end], dtype=torch.float, requires_grad=True)   # yy对应是一个小批量的标签
        predict = net(xx)
        loss = loss(predict, yy)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        batch_loss.append(loss.data.numpy())

    # 每100epoch输出一下损失值（loss）
    if i % 100 == 99:
        losses.append(np.mean(batch_loss))
        print(i, np.mean(batch_loss))


'''模型测试部分'''
targets = test_targets
targets = targets.values.reshape([len(targets), 1])  # 将数据转换成合适的tensor形式
targets = targets.astype(float)  # 保证数据为实数

x = torch.tensor(test_features.values, dtype=torch.float,requires_grad=True)
y = torch.tensor(targets, dtype=torch.float, requires_grad=True)
# 用神经网络进行预测
predict = net(x)
predict = predict.data.numpy()   # 进过训练好的网络输出的数据

#由于前面对数据进行了标准化处理，这里进行还原
mean, std = scaled_features['']  # 这里输入列名
print((predict * std + mean)[:10])


'''绘制图片'''
x_plot1=np.arange(0,len(data))
x_plot2=np.arange(0,len(targets))
plt.figure("smooth")
plt.xlabel('Years/a')
plt.ylabel('Average Carbon Sequestration Of Each Years/t*a')
plt.title('The average Carbon Sequestration')
plt.axis([0, 140, -20, 700])
plt.grid(True)
plt.plot(x_plot1, data[label_column], '-.', color = 'darkorange', label='数据')
plt.plot(x_plot2, predict, '-.', color = 'orange', label='预测值')
plt.legend()
plt.show()