import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 10

# 青年组
Y1 = [2.916679545454545,
      2.4788151515151515,
      2.666570967741935,
      2.6336576923076924,
      2.533745,
      1.7309999999999999]

Y2 = [2.474831707317073,
      2.3237956521739127,
      2.5690567567567566,
      2.395528,
      2.198112,
      1.9821571428571427]

Y3 = [2.6420177777777782,
      2.845153333333333,
      2.6073225806451608,
      2.1627454545454543,
      2.336327777777778,
      2.605575]

Y4 = [2.598381818181818,
      2.990241666666667,
      3.1972451612903225,
      2.8715961538461547,
      3.123616666666667,
      2.8472375000000003]

MY1 = [2.9666733766233766,
       2.8462470588235296,
       2.7692247787610618,
       2.506467469879518,
       2.533297872340426,
       2.238847619047619]

MY2 = [2.971614619883041,
       2.9429701612903227,
       2.827347244094488,
       2.4961626373626373,
       2.5882799999999997,
       2.416776]

MY3 = [2.9629012738853504,
       3.1198268907563027,
       2.9800937007874015,
       2.926438372093023,
       2.886444444444445,
       3.0212347826086954]

MY4 = [2.894968292682927,
       3.092374336283186,
       3.2230177966101685,
       2.8104122222222223,
       2.8199340659340657,
       2.7188576923076915]

M1 = [2.9318669811320754,
      2.750164179104478,
      2.7830679487179486,
      2.5498464285714286,
      2.6495875,
      2.31573]

M2 = [2.9305884210526325,
      2.9504745762711866,
      2.8682095238095235,
      2.6074804347826084,
      2.836310204081633,
      2.5028111111111113]

M3 = [2.867,
      3.046481944444445,
      2.9544060240963854,
      2.9078967213114755,
      2.688448275862069,
      2.691578571428572]

M4 = [2.851439000000001,
      3.216671830985916,
      3.2422460526315793,
      3.193201724137931,
      3.0012648148148147,
      3.3125785714285714]

O1 = [3.0718967741935486,
      3.0675600000000003,
      3.0058500000000006,
      2.899535294117647,
      2.623976470588236,
      2.6517]

O2 = [3.4658970588235296,
      3.271479166666667,
      3.2454444444444444,
      2.871019047619047,
      3.2291600000000003,
      3.09575]

O3 = [3.0734793103448275,
      3.2649684210526315,
      3.2431130434782607,
      2.781142857142857,
      2.7535823529411765,
      3.7136]

O4 = [2.969922857142857,
      3.4219107142857146,
      3.1781035714285717,
      3.3293190476190477,
      3.0868692307692305,
      3.06057]

T = [1, 8, 16, 24, 32, 40]
plt.figure("1")
plt.xlabel('测量时间/（周）')
plt.ylabel('Log(CD4 count+1) ')
plt.title('青年组4种疗法对比图')
plt.axis([0, 45, 0, 3.8])
plt.grid(True)
plt.plot(T, Y1, '-.', color='dodgerblue', label="疗法1")
plt.plot(T, Y2, '-.', color='darkorange', label="疗法2")
plt.plot(T, Y3, '-.', color='r', label="疗法3")
plt.plot(T, Y4, '-.', color='g', label="疗法4")
plt.legend()

plt.figure("2")
plt.xlabel('测量时间/（周）')
plt.ylabel('Log(CD4 count+1) ')
plt.title('中青年组4种疗法对比图')
plt.axis([0, 45, 0, 3.8])
plt.grid(True)
plt.plot(T, MY1, '-.', color='dodgerblue', label="疗法1")
plt.plot(T, MY2, '-.', color='darkorange', label="疗法2")
plt.plot(T, MY3, '-.', color='r', label="疗法3")
plt.plot(T, MY4, '-.', color='g', label="疗法4")
plt.legend()

plt.figure("3")
plt.xlabel('测量时间/（周）')
plt.ylabel('Log(CD4 count+1) ')
plt.title('中年组4种疗法对比图')
plt.axis([0, 45, 0, 3.8])
plt.grid(True)
plt.plot(T, M1, '-.', color='dodgerblue', label="疗法1")
plt.plot(T, M2, '-.', color='darkorange', label="疗法2")
plt.plot(T, M3, '-.', color='r', label="疗法3")
plt.plot(T, M4, '-.', color='g', label="疗法4")
plt.legend()

plt.figure("4")
plt.xlabel('测量时间/（周）')
plt.ylabel('Log(CD4 count+1) ')
plt.title('老年组4种疗法对比图')
plt.axis([0, 45, 0, 3.8])
plt.grid(True)
plt.plot(T, O1, '-.', color='dodgerblue', label="疗法1")
plt.plot(T, O2, '-.', color='darkorange', label="疗法2")
plt.plot(T, O3, '-.', color='r', label="疗法3")
plt.plot(T, O4, '-.', color='g', label="疗法4")
plt.legend()
plt.show()
