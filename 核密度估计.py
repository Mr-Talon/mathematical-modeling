def get_kde(x,data_array,bandwidth=0.1):
    def gauss(x):
        import math
        return (1/math.sqrt(2*math.pi))*math.exp(-0.5*(x**2))
    N=len(data_array)
    res=0
    if len(data_array)==0:
        return 0
    for i in range(len(data_array)):
        res += gauss((x-data_array[i])/bandwidth)
    res /= (N*bandwidth)
    return res

import numpy as np
# 需要顾及的序列
input_array=[14.6,11.8,14.8,20.4,7.7,7.5,10.9,7.5,5.3,11.1,10.0,9.1,8.8,12.6,15.4,11.9]
bandwidth=1.05*np.std(input_array)*(len(input_array)**(-1/5))
x_array=np.linspace(min(input_array),max(input_array),25)
y_array=[get_kde(x_array[i],input_array,bandwidth) for i in range(x_array.shape[0])]

import matplotlib.pyplot as plt
plt.figure(1)
plt.hist(input_array,bins=12,density=True)
plt.plot(x_array.tolist(),y_array,color='red',linestyle='-')
plt.title("The kernel density estimate of Time to get ID check")
plt.xlabel("Time to get ID check")
plt.ylabel("Probability Density")
plt.show()
