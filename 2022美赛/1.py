import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.misc import derivative
import math



def sigmoid(t, a, b, k):
    return a / (1 + np.exp(b - k * t))


def CarbonStorage(t, CF, BEF, WD, R, a, b, k):
    return CF * BEF * WD * (1 + R) * sigmoid(t, a, b, k)


def DNOfProduct(CarbonStorage, alpha, beta, lifespan):
    return CarbonStorage * alpha * (1 - beta) * lifespan


'''
    参数：
    m采伐量    1/m采伐强度     n采伐间隔（每多少年采伐下一块森林）      limit生长周期限制
    Tmax时间变量        Ssum森林总面积
    CF含碳率       BEF生物量换算因子      WD木材密度      R地下与地上生物量之比
    a生长极限参数     b生长初始值有关参数      k生长速率参数
    alpha出材率        beta木材加工废弃率     lifespan产品生命周期
'''


def fun(m, n, limit, TMax, Ssum, CF=0.520, BEF=1.1509, WD=0.307, R=0.246,
        a=285.26, b=5.584, k=0.31, alpha=0.7, beta=0.2, lifespan=300.0):
    List = np.zeros(m, dtype=int)
    p = 0  # 标记采伐区域
    s = Ssum / m  # 每一块区域的面积
    out = []

    for i in range(TMax):
        List = [temp + 1 for temp in List]  # 每年树龄+1
        d = np.ones(m, dtype=int)  # 标记当前树是否被砍伐  =1表示未被砍伐，=0表示被砍伐
        if i % n == 0 and i > 0 and List[p % m] >= limit:  # 处于采伐期才可以采伐  采伐的树木必须是成熟的
            d[p % m] = 0  # 标记这块区域已经被砍伐

        sum = 0
        for j in range(m):
            DNm = 0
            for t in range(List[j]):
                t += 1
                DNm += (List[j] - t + 1) * (
                        CarbonStorage(t, CF, BEF, WD, R, a, b, k) - CarbonStorage(t - 1, CF, BEF, WD, R, a, b, k))
            sum += DNm * s * d[j] + (DNOfProduct(CarbonStorage(List[j], CF, BEF, WD, R, a, b, k),
                                                 alpha, beta, lifespan) + DNm) * s * (1 - d[j])
        out.append(sum / (i + 1))

        if i % n == 0 and i > 0 and List[p % m] >= limit:
            List[p % m] = 0
            p += 1
    # print(p)
    return out


def funNotCut(TMax, Ssum, lifeLimit, CF=0.520, BEF=1.1509, WD=0.307, R=0.246, a=285.26, b=5.584, k=0.31):
    out = []
    for i in range(TMax):
        age = i % lifeLimit
        sum = 0
        DNm = 0
        for t in range(age):
            if i // lifeLimit == 0:
                t += 1
                DNm += (age - t + 1) * (
                        CarbonStorage(t, CF, BEF, WD, R, a, b, k) - CarbonStorage(t - 1, CF, BEF, WD, R, a, b, k))
            elif i // lifeLimit == 1:  # 一个生命周期之后50%的树发病或者死去
                t += 1
                DNm += 0.5 * (age - t + 1) * (
                        CarbonStorage(t, CF, BEF, WD, R, a, b, k) - CarbonStorage(t - 1, CF, BEF, WD, R, a, b, k)) \
                       + 0.5 * (age + lifeLimit - t + 1) * (CarbonStorage(t + lifeLimit, CF, BEF, WD, R, a, b, k)
                                                            - CarbonStorage(t + lifeLimit - 1, CF, BEF, WD, R, a, b, k))
            else:
                t += 1
                DNm += 0.5 * (age - t + 1) * (
                            CarbonStorage(t, CF, BEF, WD, R, a, b, k) - CarbonStorage(t - 1, CF, BEF, WD, R, a, b, k)) \
                       + 0.5 * 0.5 * (age + lifeLimit - t + 1) * (
                                   CarbonStorage(t + lifeLimit, CF, BEF, WD, R, a, b, k) - CarbonStorage(
                               t + lifeLimit - 1, CF, BEF, WD, R, a, b, k)) \
                       + 0.5 *0.5 * (age + lifeLimit + lifeLimit - t + 1) * (
                                   CarbonStorage(t + lifeLimit + lifeLimit, CF, BEF, WD, R, a, b, k) - CarbonStorage(
                               t + lifeLimit + lifeLimit - 1, CF, BEF, WD, R, a, b, k))
        sum += DNm * Ssum
        out.append(sum / (i + 1))
    # print(p)
    return out


x = np.arange(0, 140)
out0 = np.array(funNotCut(140, 20, 40))
out0_smooth = gaussian_filter1d(out0, sigma=5)

out1 = np.array(fun(36, 1, 24, 140, 20))
out1_smooth = gaussian_filter1d(out1, sigma=5)

out2 = np.array(fun(18, 2, 24, 140, 20))
out2_smooth = gaussian_filter1d(out2, sigma=5)

out3 = np.array(fun(12, 3, 24, 140, 20))
out3_smooth = gaussian_filter1d(out3, sigma=5)

out4 = np.array(fun(9, 4, 24, 140, 20))
out4_smooth = gaussian_filter1d(out4, sigma=5)

out5 = np.array(fun(6, 6, 24, 140, 20))
out5_smooth = gaussian_filter1d(out5, sigma=5)

out6 = np.array(fun(4, 9, 24, 140, 20))
out6_smooth = gaussian_filter1d(out6, sigma=5)

out7 = np.array(fun(3, 12, 24, 140, 20))
out7_smooth = gaussian_filter1d(out7, sigma=5)




out11 = np.array(fun(10, 2, 24, 140, 20))
out11_smooth = gaussian_filter1d(out11, sigma=5)

out12 = np.array(fun(12, 2, 24, 140, 20))
out12_smooth = gaussian_filter1d(out12, sigma=5)

out13 = np.array(fun(14, 2, 24, 140, 20))
out13_smooth = gaussian_filter1d(out13, sigma=5)

out14 = np.array(fun(16, 2, 24, 140, 20))
out14_smooth = gaussian_filter1d(out14, sigma=5)

out15 = np.array(fun(18, 2, 24, 140, 20))
out15_smooth = gaussian_filter1d(out15, sigma=5)



out21 = np.array(fun(18, 2, 24, 140, 20,lifespan=150*0.8))
out21_smooth = gaussian_filter1d(out21, sigma=5)

out22 = np.array(fun(18, 2, 24, 140, 20,lifespan=150*0.9))
out22_smooth = gaussian_filter1d(out22, sigma=5)

out23 = np.array(fun(18, 2, 24, 140, 20,lifespan=150))
out23_smooth = gaussian_filter1d(out23, sigma=5)

out24 = np.array(fun(18, 2, 24, 140, 20,lifespan=150*1.1))
out24_smooth = gaussian_filter1d(out24, sigma=5)

out25 = np.array(fun(18, 2, 24, 140, 20,lifespan=150*1.2))
out25_smooth = gaussian_filter1d(out25, sigma=5)

print(sum(out1))
print(sum(out2))
print(sum(out3))
print(sum(out4))
print(sum(out5))
print(sum(out6))
print(sum(out7))
print(sum(out0))
print("next")
print(sum(out11))
print(sum(out12))
print(sum(out13))
print(sum(out14))
print(sum(out15))
print('next')
print(sum(out21))
print(sum(out22))
print(sum(out23))
print(sum(out24))
print(sum(out25))
print('next max')
print(max(out21))
print(max(out22))
print(max(out23))
print(max(out24))
print(max(out25))


plt.figure("smooth")
plt.xlabel('Years/a')
plt.ylabel('Average Carbon Sequestration Of Each Years/t*a')
plt.title('The average Carbon Sequestration')
plt.axis([0, 140, -20, 700])
plt.grid(True)
plt.plot(x, out1_smooth, '-.', color = 'darkorange', label='Regrowth and production m=36 n=1')
plt.plot(x, out2_smooth, linewidth=3 ,color = 'dodgerblue', label='Regrowth and production m=18 n=2')
plt.plot(x, out3_smooth, '-.', color = 'wheat', label='Regrowth and production m=12 n=3')
plt.plot(x, out4_smooth, '-.', label='Regrowth and production m=9 n=4')
plt.plot(x, out5_smooth, '-.', label='Regrowth and production m=6 n=6')
plt.plot(x, out6_smooth, '-.', label='Regrowth and production m=4 n=9')
plt.plot(x, out7_smooth, '-.', label='Regrowth and production m=3 n=12')
plt.plot(x, out0_smooth, '-.', label='Grow naturally')
plt.legend()

plt.figure("2")
plt.xlabel('Years/a')
plt.ylabel('Average Carbon Sequestration Of Each Years/t*a')
plt.title('The average Carbon Sequestration')
plt.axis([0, 140, -20, 700])
plt.grid(True)
plt.plot(x, out11_smooth, '-.', color = 'darkorange', label='m=10 n=2')
plt.plot(x, out12_smooth, '-.', color = 'dodgerblue', label='m=12 n=2')
plt.plot(x, out13_smooth, '-.', color = 'wheat', label='m=14 n=2')
plt.plot(x, out14_smooth, '-.', label='m=16 n=2')
plt.plot(x, out15_smooth, linewidth=3 ,label='m=18 n=2')
plt.legend()

plt.figure("3")
plt.xlabel('Years/a')
plt.ylabel('Average Carbon Sequestration Of Each Years/t*a')
plt.title('The average Carbon Sequestration')
plt.axis([0, 140, -20, 700])
plt.grid(True)
plt.plot(x, out21_smooth, '-.', color = 'darkorange', label='-20%')
plt.plot(x, out22_smooth, '-.', color = 'dodgerblue', label='-10%')
plt.plot(x, out23_smooth, '-.', color = 'wheat', label='lifespan=50')
plt.plot(x, out24_smooth, '-.', label='+10%')
plt.plot(x, out25_smooth, '-.', color='springgreen',label='+20%')
plt.legend()


out31 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,alpha=0.7*1.05))
out31_smooth = gaussian_filter1d(out31, sigma=5)

out32 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,alpha=0.7*1.1))
out32_smooth = gaussian_filter1d(out32, sigma=5)

out33 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,alpha=0.7))
out33_smooth = gaussian_filter1d(out33, sigma=5)

out34 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,alpha=0.7*0.95))
out34_smooth = gaussian_filter1d(out34, sigma=5)

out35 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,alpha=0.7*0.9))
out35_smooth = gaussian_filter1d(out35, sigma=5)

print('next')
print(max(out32))
print(max(out31))
print(max(out33))
print(max(out34))
print(max(out35))


plt.figure("4")
plt.xlabel('Years/a')
plt.ylabel('Average Carbon Sequestration Of Each Years/t*a')
plt.title('The average Carbon Sequestration')
plt.axis([0, 140, 0, 650])
plt.grid(True)
plt.plot(x, out32_smooth, '-.', color = 'dodgerblue', label='+10%')
plt.plot(x, out31_smooth, '-.', color = 'darkorange', label='+5%')
plt.plot(x, out33_smooth, '-.', color = 'r', label='alpha=0.7')
plt.plot(x, out34_smooth, '-.', label='-5%')
plt.plot(x, out35_smooth, '-.', color='y',label='-10%')
plt.legend()


out41 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,beta=0.2*1.05))
out41_smooth = gaussian_filter1d(out41, sigma=5)

out42 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,beta=0.2*1.1))
out42_smooth = gaussian_filter1d(out42, sigma=5)

out43 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,beta=0.2))
out43_smooth = gaussian_filter1d(out43, sigma=5)

out44 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,beta=0.2*0.95))
out44_smooth = gaussian_filter1d(out44, sigma=5)

out45 = np.array(fun(18, 2, 24, 140, 20,lifespan=300,beta=0.2*0.9))
out45_smooth = gaussian_filter1d(out45, sigma=5)

print('next')
print(max(out42))
print(max(out41))
print(max(out43))
print(max(out44))
print(max(out45))


plt.figure("5")
plt.xlabel('Years/a')
plt.ylabel('Average Carbon Sequestration Of Each Years/t*a')
plt.title('The average Carbon Sequestration')
plt.axis([0, 140, 100, 650])
plt.grid(True)
plt.plot(x, out42_smooth, '-.', color = 'dodgerblue', label='+10%')
plt.plot(x, out41_smooth, '-.', color = 'darkorange', label='+5%')
plt.plot(x, out43_smooth, '-.', color = 'r', label='beta=0.2')
plt.plot(x, out44_smooth, '-.', label='-5%')
plt.plot(x, out45_smooth, '-.', color='y',label='-10%')
plt.legend()


outs1=[]
outs2=[]
outs3=[]
def sigmoid1(x):
    return 258.43 / (1 + math.exp(4.01 - 0.758 * x))
for x in range(1,40):
    outs1.append(sigmoid1(x))
    outs2.append(derivative(sigmoid1, x, dx=1e-6))
    outs3.append(sigmoid1(x)/x)
x = np.arange(1, 40)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ln1=ax1.plot(x, outs1,'r',label='Accumulation')
ax1.set_ylabel('Accumulation(m^3/ha)')
ax1.set_title("Simulation of eucalyptus growth curve")
ax1.set_xlabel('Years(a)')
ax1.grid()
ax2 = ax1.twinx() # this is the important function
ln2=ax2.plot(x, outs2, '-.', color = 'dodgerblue',label='year-on-year growth')
ln3=ax2.plot(x, outs3, '.', color = 'darkorange', label='average annual growth')
ax2.set_ylabel('Average annual growth & year-on-year growth(m^3/ha)')

ln=ln1+ln2+ln3
labs=[i.get_label() for i in ln]
ax1.legend(ln, labs,loc='center right')
plt.show()
