import numpy as np
import pandas as pd

print("读取数据……")
data1 = pd.read_excel("answer35.9.xlsx")  # 阵列组合数据
data2 = pd.read_excel("C:/Users/16046/Desktop/data.xlsx")   # 日照数据
data3 = pd.read_excel("C:/Users/16046/Desktop/B/cumcm2012B_附件3_三种类型的光伏电池(A单晶硅B多晶硅C非晶硅薄膜)组件设计参数和市场价格.xls")  # 电池数据
data4=pd.read_excel("C:/Users/16046/Desktop/B/附件5.xlsx")   # 逆变器数据

answer_data=np.array(data1)
north = np.array(data1.loc[data1['墙面序号'] == 1, ['逆转器', '电池', '串联数', '并联数', '墙面序号']])
east = np.array(data1.loc[data1['墙面序号'] == 2, ['逆转器', '电池', '串联数', '并联数', '墙面序号']])
south = np.array(data1.loc[data1['墙面序号'] == 3, ['逆转器', '电池', '串联数', '并联数', '墙面序号']])
west = np.array(data1.loc[data1['墙面序号'] == 4, ['逆转器', '电池', '串联数', '并联数', '墙面序号']])
south_up = np.array(data1.loc[data1['墙面序号'] == 5, ['逆转器', '电池', '串联数', '并联数', '墙面序号']])
north_up = np.array(data1.loc[data1['墙面序号'] == 6, ['逆转器', '电池', '串联数', '并联数', '墙面序号']])

north_energy=np.array(data2["北向总辐射强度"])
east_energy=np.array(data2["东向总辐射强度"])
south_energy=np.array(data2["南向总辐射强度"])
west_energy=np.array(data2["西向总辐射强度"])
# south_up_energy=np.array(data2["南"])
north_up_energy=np.array(data2["北"])
south_up_energy_35=np.array(data2["南35.9"])

walls=[north,east,south,west,south_up,north_up]

# energys=[north_energy,east_energy,south_energy,west_energy,south_up_energy,north_up_energy]
energys=[north_energy,east_energy,south_energy,west_energy,south_up_energy_35,north_up_energy]

square=np.array(data3["面积"])/1000000   # 电池面积 单位平方米
eta=np.array(data3["转换效率η（%）"])  # 电池转换效率
P=np.array(data3["组件功率（w)"])  # 电池组件功率
price=np.array(data3["价格（元/Wp）"])   # 电池价格

priceInv=np.array(data4["参考价格（元/台）"])  # 逆变器价格

Q=[]

'''计算每个墙面 不同电池的E'''
print("计算E……")
E=np.zeros((6,24))
for i,energy in enumerate(energys):
    for j in range(24):
        E_i=0
        if (j+1 >=1) & (j+1<=6):
            for x in range(len(energy)):
                if energy[x] >= 200:
                    E_i += energy[x]

        elif (j+1 >=7) & (j+1<=13):
            for x in range(len(energy)):
                if energy[x] >= 80:
                    E_i += energy[x]

        elif (j+1 >=14) & (j+1<=24):
            for x in range(len(energy)):
                if energy[x] >= 30:
                    E_i += energy[x]

        E[i][j]=E_i
E_data=pd.DataFrame(data=E)
E_data.to_csv("E35.9.csv")

# E=pd.read_excel("E.xlsx")
# E=np.array(E)

'''计算所有可行组合的Q'''
print("计算……")
for i,wall in enumerate(walls):
    for sample in wall:
        n_i=sample[2]*sample[3]   # 该阵列电池的个数
        S_i=square[sample[1]-1]   # 该电池的面积
        eta_i=eta[sample[1]-1]    # 该电池的效率
        E_i=E[i][sample[1]-1]

        Q_i=n_i*S_i*E_i*eta_i/1000
        Q.append(Q_i)

Q=np.array(Q)
Q_data=pd.DataFrame(data=Q)
Q_data.to_csv("Qnew.csv")

'''计算35年的Q'''
Q35=Q*10*1+Q*15*0.9+Q*10*0.8
Q35=np.array(Q35)
Q35_data=pd.DataFrame(data=Q35)
Q35_data.to_csv("Q35new.csv")

'''计算经济效益'''
economy=[]
for i,sample in enumerate(south_up):
    economy_i = Q35[i] * 0.5 - (sample[2] * sample[3]*price[sample[1] - 1]*P[sample[1] - 1]+priceInv[sample[0] - 1])
    economy.append(economy_i)

economy=np.array(economy)
economy_data=pd.DataFrame(data=economy)
economy_data.to_csv("economynew.csv")