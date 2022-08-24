import numpy as np
import pandas as pd


def matrix(arrive, departure, type):
    G = np.zeros((len(arrive), len(arrive)),dtype='int')
    departure_end = departure + 45

    for i in range(len(arrive)):
        for j in range(i + 1, len(arrive)):
            if type[i] != type[j]:  # 种类不同的飞机不会冲突
                continue
            else:  # 种类相同
                if (arrive[j] >= arrive[i]) & (arrive[j] <= departure_end[j]):
                    G[i][j] = 1
                    G[j][i] = 1

    return G


def NextValue(k, m, x, mg, p):
    while (1):
        x[k] = (x[k] + 1) % (m + 1)  # 尝试所有颜色 0表示没有颜色  这里就是登机口
        if x[k] == 0:
            return

        gate=x[k]-1
        if (p[k][gate]) == 0:  # 登机口不匹配  退出循环
            continue

        j = 0
        for j in range(k):
            if (mg[k][j] != 0) & (x[k] == x[j]):  # 和其他飞机冲突 退出循环
                break

        if j == k-1:  # 判断结束
            return


def mColoring(k, m, x, mg, p):
    # k为当前考查的解向量下标
    while (1):
        print(k)
        NextValue(k, m, x, mg, p)
        if x[k] == 0:
            break

        if k == len(x) - 1:
            for x_i in x:
                print(str(x_i) + " ")
            print("\n")
        else:
            mColoring(k + 1, m, x, mg, p)


def mColoring_in(m, x, mg, p):  # 非递归函数
    mColoring(0, m, x, mg, p)


def main():
    data = pd.read_excel("C:/Users/16046/Desktop/2018年F题/航班数据.xlsx")
    p = pd.read_excel("P.xlsx")

    arrive = np.array(data["到达时间差"])
    departure = np.array(data["出发时间差"])
    type = np.array(data["航班种类"])
    p = np.array(p)

    G_flight = matrix(arrive, departure, type)
    num_of_gate = 69  # 颜色数——登机口最大个数
    x = np.zeros(len(arrive),dtype='int')  # 解向量初始化
    mColoring_in(num_of_gate, x, G_flight, p)


main()
