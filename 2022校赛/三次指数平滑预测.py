from statsmodels.tsa.api import Holt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.arima_model import ARIMA

data=pd.read_excel("needList.xlsx")
data=np.array(data).reshape(-1)
numOfDate=len(data)

x=np.linspace(0,104,104)
train_data=data[:-8]     # 训练数据
val_data=data[-8:]          # 测试数据

fit = Holt(np.asarray(train_data)).fit(smoothing_level=0.3, smoothing_slope=0.1)
y_hat= fit.forecast(len(val_data))   # 预测 测试数据长度的数据

fit1 = ExponentialSmoothing(np.asarray(train_data),seasonal_periods=7, trend='add', seasonal='add').fit(smoothing_level=0.3, smoothing_slope=0.1)
y_hat1= fit1.forecast(len(val_data))   # 预测 测试数据长度的数据

ts_arima=train_data.astype(float)
fit2=ARIMA(ts_arima, order=(0, 0, 0)).fit()
y_hat2= fit2.forecast(len(val_data))   # 预测 测试数据长度的数据

plt.plot(x[:-8],train_data)
plt.plot(x[-8:],val_data)
plt.plot(x[-8:],y_hat)
plt.plot(x[-8:],y_hat1)
plt.plot(x[-8:],y_hat2)

var1=(val_data-y_hat)**2
print(sum(var1))
var2=(val_data-y_hat1)**2
print(sum(var2))
var3=(val_data-y_hat2)**2
print(sum(var3))

plt.show()
