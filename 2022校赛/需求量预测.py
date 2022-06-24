import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader,Dataset
from itertools import chain
from scipy.interpolate import make_interp_spline

def load_data():
    global MAX, MIN
    data = pd.read_excel('t4.xlsx')
    data = np.array(data).reshape(-1)
    MAX = np.max(data)
    MIN = np.min(data)
    data = (data - MIN) / (MAX - MIN)

    return data

def get_mape(x, y):
    """
    :param x:true
    :param y:pred
    :return:MAPE
    """
    return np.mean(np.abs((x - y) / x))

class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)


def nn_seq(B,tw):
    # batch-size 观察窗口大小tw
    print('处理数据:')
    data = load_data()
    load=data
    load = load.tolist()
    load = torch.FloatTensor(load).view(-1)
    data = data.tolist()
    seq = []   # 训练数据 标签对
    for i in range(len(data) - tw):
        train_seq = []
        train_label = []
        for j in range(i, i + tw):
            train_seq.append(load[j])
        train_label.append(load[i + tw])
        train_seq = torch.FloatTensor(train_seq).view(-1)
        train_label = torch.FloatTensor(train_label).view(-1)
        seq.append((train_seq, train_label))
    # print(seq[:5])

    Dtr = seq[0:int(len(seq) * 0.7)]    # 前70%作为训练数据
    Dte = seq[int(len(seq) * 0.7):len(seq)]

    train_len = int(len(Dtr) / B) * B
    test_len = int(len(Dte) / B) * B
    Dtr, Dte = Dtr[:train_len], Dte[:test_len]

    train = MyDataset(Dtr)
    test = MyDataset(Dte)

    Dtr = DataLoader(dataset=train, batch_size=B, shuffle=False, num_workers=0)
    Dte = DataLoader(dataset=test, batch_size=B, shuffle=False, num_workers=0)

    return Dtr, Dte


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size, batch_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.output_size = output_size
        self.num_directions = 1 # 单向LSTM
        self.batch_size = batch_size
        self.lstm = nn.LSTM(self.input_size, self.hidden_size, self.num_layers, batch_first=True)
        self.linear = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, input_seq):
        h_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(torch.device('cuda'))
        c_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(torch.device('cuda'))
        seq_len = input_seq.shape[1] # (5, 24)
        # input(batch_size, seq_len, input_size)
        input_seq = input_seq.view(self.batch_size, seq_len, 1)  # (5, 24, 1)
        # output(batch_size, seq_len, num_directions * hidden_size)
        output, _ = self.lstm(input_seq, (h_0, c_0)) # output(5, 24, 64)
        output = output.contiguous().view(self.batch_size * seq_len, self.hidden_size) # (5 * 24, 64)
        pred = self.linear(output) # pred(150, 1)
        pred = pred.view(self.batch_size, seq_len, -1) # (5, 24, 1)
        pred = pred[:, -1, :]  # (5, 1)
        return pred

def LSTM_train(b,tw):
    Dtr, Dte = nn_seq(B=b,tw=tw)
    input_size, hidden_size, num_layers, output_size = 1, 64, 5, 1
    model = LSTM(input_size, hidden_size, num_layers, output_size, batch_size=b).to(torch.device('cuda'))
    loss_function = nn.MSELoss().to(torch.device('cuda'))
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    # 训练
    epochs = 300
    cnt = 0
    for i in range(epochs):
        cnt = 0
        print('当前', i)
        for (seq, label) in Dtr:
            cnt += 1
            seq = seq.to(torch.device('cuda'))
            label = label.to(torch.device('cuda'))
            y_pred = model(seq)
            loss = loss_function(y_pred, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if cnt % 100 == 0:
                print('epoch', i, ':', cnt - 100, '~', cnt, loss.item())
    state = {'model': model.state_dict(), 'optimizer': optimizer.state_dict()}
    torch.save(state, 'model.pkl')

LSTM_train(4,12)

def test(b):
    global MAX, MIN
    Dtr, Dte = nn_seq(B=b,tw=12)
    pred = []
    y = []
    print('loading model...')
    input_size, hidden_size, num_layers, output_size = 1, 64, 5, 1
    model = LSTM(input_size, hidden_size, num_layers, output_size, batch_size=b).to(torch.device('cuda'))
    model.load_state_dict(torch.load('model.pkl')['model'])
    model.eval()
    print('predicting...')
    for (seq, target) in Dte:
        target = list(chain.from_iterable(target.data.tolist()))
        y.extend(target)
        seq = seq.to(torch.device('cuda'))
        seq_len = seq.shape[1]
        seq = seq.view(model.batch_size, seq_len, 1)  # (5, 24, 1)
        with torch.no_grad():
            y_pred = model(seq)
            y_pred = list(chain.from_iterable(y_pred.data.tolist()))
            pred.extend(y_pred)

    y, pred = np.array([y]), np.array([pred])
    y = (MAX - MIN) * y + MIN
    pred = (MAX - MIN) * pred + MIN
    print('accuracy:', get_mape(y, pred))
    # plot
    x = [i for i in range(1, 151)]
    x_smooth = np.linspace(np.min(x), np.max(x), 600)
    y_smooth = make_interp_spline(x, y.T[0:150])(x_smooth)
    plt.plot(x_smooth, y_smooth, c='green', marker='*', ms=1, alpha=0.75, label='true')

    y_smooth = make_interp_spline(x, pred.T[0:150])(x_smooth)
    plt.plot(x_smooth, y_smooth, c='red', marker='o', ms=1, alpha=0.75, label='pred')
    plt.grid(axis='y')
    plt.legend()
    plt.show()


test(4)