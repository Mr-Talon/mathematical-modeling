import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 13


length_rode=70
length_car=4.9
length_d=1.1
n_max=int((length_rode+length_d)//(length_d+length_car))   # 上车点的最大个数   也是停车位的个数

def cal_T1(n):
    # 2n个车 两两并行 只需要计算一个车道的时间
    T=0
    T+=np.random.uniform(3,7,1)
    for i in range(n-1):
        T+=np.random.uniform(1.5,3.5,1)
    return T


def cal_T2(n):
    # 2n个乘客 上车时间服从指数分布 出租车开走的时间服从均匀分布 同T1    取所有旅客中最长的作为 T2
    T2=[]
    for i in range(2*n):
        time=0
        time+=np.random.exponential(32.8)  # 加上旅客上车时间
        time+=np.random.uniform(3,7,1)
        T2.append(time)
    T2=np.array(T2)
    return np.max(T2)


ans=[]
for n in range(1,n_max+1):
    print(n)
    average_n=[]
    for i in range(10000):    # 每种n模拟10000次
        average_n.append((cal_T1(n)+cal_T2(n))/(2*n))
    average_n=np.array(average_n)
    ans.append(np.mean(average_n))

ans=np.array(ans)
print(ans)

plt.figure("2")
plt.xlabel('每条车道的上车点数量n')
plt.ylabel('平均每辆车消耗的总时间/s')
plt.title('开放不同个数上车点对乘车效率的影响')
plt.axis([0, 13, 0, 35])
plt.grid(True)
x=np.arange(1,12)
plt.plot(x, ans, '-.')
plt.legend()
plt.show()


# T1=[]
# for i in range(10000):
#     T1.append(cal_T1(n_max))
# T1=np.array(T1)
# print(T1.mean())
#