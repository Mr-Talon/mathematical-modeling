from sklearn.neighbors import KernelDensity
import numpy as np
import matplotlib.pyplot as plt

input_array=[48,45,28,25,22,24,17,33,8,10,26,32,21,37,68,40,18,26,8,21,23,28,50,28,48,28,36,27,5]
plt.hist(input_array,bins=10,density=True)
bandwidth=1.05*np.std(input_array)*(len(input_array)**(-1/5))   # 计算带宽
kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(np.array(input_array).reshape(1,-1))   # 核密度拟合
plt.plot(np.array(input_array).tolist(),kde,color='red',linestyle='-')
plt.title("The kernel density estimate of Time to get scanned property")
plt.xlabel("Time to get scanned property")
plt.ylabel("Probability Density")
plt.show()