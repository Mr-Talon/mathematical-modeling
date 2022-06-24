import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data=pd.read_excel("needList.xlsx")
data=np.array(data).reshape(-1)
numOfDate=len(data)

def fun(x,a,b,e,c,w,f,d):
    return a*np.exp(b*x+e)+c*np.sin(w*x+f)+d

def fun1(x,a1,b1,c1,d1):
    return a1*np.exp(b1*x+c1)+d1

x=np.linspace(0,numOfDate,numOfDate)
x_test=np.linspace(0,numOfDate-8,numOfDate-8)
plt.plot(x,data)   #绘制原始数据

popt1, pcov1=curve_fit(fun,x_test,data[:-8])
popt2, pcov2=curve_fit(fun1,x_test,data[:-8],maxfev=10000)

plt.plot(x,fun(x,*popt1), 'g--',label='fit: a=%5.3f, b=%5.3f,e=%5.3f, c=%5.3f,w=%5.3f, f=%5.3f, d=%5.3f' % tuple(popt1))
plt.plot(x,fun1(x,*popt2), 'r--', label='fit: a=%5.3f, b=%5.3f,c=%5.3f, d=%5.3f' % tuple(popt2))

plt.axis([0, 120, 0, 200])

var1=(data-fun(x,*popt1))**2
print(sum(var1))

var2=(data-fun1(x,*popt2))**2
print(sum(var2))


#预测
x_pred=np.linspace(0,112,112)
plt.plot(x_pred,fun1(x_pred,*popt2))
plt.show()
print(fun1(x_pred[-8:],*popt2))