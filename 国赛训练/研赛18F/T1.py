import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import copy

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 30


def matrix(arrive, departure, type):
    G = np.zeros((len(arrive), len(arrive)), dtype='int')
    departure_end = departure + 45

    for i in range(len(arrive)):
        for j in range(i + 1, len(arrive)):
            # if type[i] != type[j]:  # 种类不同的飞机不会冲突
            #     continue
            # else:  # 种类相同
            if (arrive[j] >= arrive[i]) & (arrive[j] <= departure_end[i]):
                G[i][j] = 1
                G[j][i] = 1
    return G


def cal_degree(mg):
    degree_of_mg = np.sum(mg, axis=1)
    return degree_of_mg


def limit_color(p, x, mg):
    # 返回每个顶点的禁色数
    limit = 69 - np.sum(p, axis=1)  # 禁色数初始值

    for i in range(len(mg)):  # 遍历每个节点
        list = []  # 记录每一个邻接点的登机口（颜色）
        for j in range(len(mg)):
            if (mg[i][j] == 1) & (x[j] != 0):  # 对当前节点的所有邻接结点 如果已经分配了登机口
                if (p[i][x[j]] == 1) & (x[j] not in list):  # 并且该禁色不是在初始条件下形成的   而且之前没有禁掉这个颜色
                    limit[i] += 1
                    list.append(x[j])
    return limit


def cal_r(x, mg):
    used = [0]  # G中已经使用的颜色集合
    for x_i in x:
        if x_i not in used:
            used.append(x_i)
    used.remove(0)

    r = []
    for i in range(len(mg)):
        used_t = copy.deepcopy(used)  # 考查每一个结果的时候复制一份
        for j in range(len(mg)):
            if (mg[i][j] == 1) & (x[j] in used_t):
                used_t.remove(x[j])
        r.append(len(used_t))

    return r


def sort(degree, limit, r):
    L = []
    for j in range(len(limit)):
        L.append([j, degree[j], limit[j], r[j]])
    L.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    return L


def order_gate(x, p, mg, index, num_of_gate):
    for i in range(num_of_gate):
        if p[index][i] == 1:  # 遍历当前考查航班 index 能够匹配的登机口
            j = 0
            for j in range(len(mg)):
                if (mg[index][j] == 1) & (x[j] == i):  # 如果与该航班相邻接的航班j 分配的登机口也是i 就产生了冲突
                    break
            if j == len(mg) - 1:  # 上面的循环验证无误 就可以将第index个航班 安排在第i个登机口 并且结束函数
                x[index] = i
                return


def change(index, degree, mg, p, x):
    # 与刚才安排的航班相邻接的航班 节点度数-1
    for i in range(len(mg)):
        if mg[index][i] == 1:  # 当前邻接点为i
            degree[i] -= 1
    degree[index] = 0  # 将当前考查的航班的度数置0

    limit = limit_color(p, x, mg)  # 重新计算禁色数
    r = cal_r(x, mg)
    return degree, limit, r


def draw(x, arrive, departure):
    plt.figure("1")
    plt.xlabel('转场占据的时间段/分')
    plt.ylabel('登机口序号')
    plt.title('转场对应登机口序号图')
    plt.axis([0, 4000, 0, 70])

    x_ = []
    y_ = []
    for i in range(len(x)):
        x_.append([arrive[i], departure[i]])
        y_.append([x[i], x[i]])

    for j in range(len(x)):
        plt.plot(x_[j], y_[j])
    plt.show()


def main():
    data = pd.read_excel("C:/Users/16046/Desktop/2018年F题/航班数据.xlsx")
    p = pd.read_excel("P.xlsx")
    arrive = np.array(data["到达时间差"])
    departure = np.array(data["出发时间差"])
    # type = np.array(data["航班种类"])
    # p = np.array(p)  # 初始禁色数
    #
    # G_flight = matrix(arrive, departure, type)
    # num_of_gate = 69  # 颜色数——登机口最大个数
    # x = np.zeros(len(arrive), dtype='int')  # 解向量初始化
    #
    # degree = cal_degree(G_flight)  # 返回对顶点度的排序 和 相应排序的索引（对应的转场）
    # limit = limit_color(p, x, G_flight)
    # r = cal_r(x, G_flight)
    # for i in range(len(G_flight)):  # 求解解向量
    #     L = sort(degree, limit, r)
    #     index = L[0][0]  # 获取次轮安排的转场号
    #     order_gate(x, p, G_flight, index, num_of_gate)
    #     print(str(i) + ":正在分配第" + str(index) + "个航班")
    #     degree, limit, r = change(index, degree, G_flight, p, x)
    # print(x)
    x=[61, 36, 17, 0, 2, 55, 3, 23, 60, 22, 21, 37, 63, 68, 12, 19, 38, 29, 50, 6, 39, 54, 4, 34, 20, 5, 69, 43,
       47, 48, 49, 41, 13, 69, 7, 28, 15, 46, 14, 69, 35, 8, 69, 9, 44, 69, 69, 52, 11, 53, 42, 18, 51, 16, 30, 31,
       45, 69, 24, 10, 33, 32, 67, 39, 69, 22, 26, 1, 38, 59, 65, 0, 69, 27, 0, 69, 68, 27, 40, 3, 69, 60, 69, 0,
       58, 69, 15, 69, 69, 37, 13, 11, 44, 28, 20, 45, 23, 12, 69, 14, 22, 50, 10, 54, 49, 69, 33, 47, 8, 9, 48, 31,
       69, 35, 46, 69, 18, 69, 52, 69, 69, 53, 38, 0, 6, 69, 16, 69, 34, 37, 7, 69, 21, 20, 41, 15, 40, 39, 9, 47,
       8, 10, 22, 6, 32, 48, 11, 21, 19, 0, 45, 69, 7, 15, 38, 54, 46, 69, 69, 43, 52, 55, 29, 20, 40, 69, 27, 9,
       35, 53, 24, 34, 12, 6, 11, 19, 21, 31, 4, 8, 0, 69, 51, 69, 69, 50, 69, 42, 33, 69, 68, 7, 69, 22, 69, 2, 38,
       44, 5, 69, 26, 13, 27, 69, 52, 69, 69, 35, 54, 0, 55, 64, 19, 21, 23, 8, 7, 16, 49, 9, 6, 69, 44, 38, 51, 59,
       48, 20, 69, 32, 69, 13, 61, 0, 69, 60, 69, 69, 29, 1, 69, 69, 12, 36, 3, 37, 69, 46, 39, 30, 17, 43, 18, 40,
       47, 8, 31, 55, 21, 20, 6, 53, 22, 11, 19, 44, 69, 69, 42, 15, 14, 38, 33, 58, 16, 41, 54, 7, 29, 17, 46, 35,
       69, 69, 10, 48, 12, 45, 21, 69, 32, 36, 49, 13, 19, 55, 6, 11, 69, 37, 28, 15, 53]
    x=np.array(x)+1
    draw(x, arrive, departure)

    x = pd.DataFrame(data=x)
    x.to_excel("转场登机口分配表.xlsx")


main()
