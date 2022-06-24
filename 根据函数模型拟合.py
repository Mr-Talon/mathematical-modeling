import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [8.8,11.3,12.4,3.5,7.5,8.2,13.0,11.0,9.0,7.8,10.6,15.2,11.0,16.9,13.4,7.7,6.7,11.7,19.4,8.6,37.4,11.4,12.4,12.0,13.2,11.1,7.3,8.1,14.4,7.0,11.0,9.6,27.5,8.5,9.7,11.0,9.7,8.6,11.9,7.1]
n = len(x)
nbins = 10
freq, bins = np.histogram(x, bins=nbins)
freq_rate = freq / n
bin_w = bins[1] - bins[0]
bin_h = freq_rate / bin_w

# ==================1. 通过distplot
ax= sns.distplot(x, bins=nbins,
                 hist=True, # Whether to plot a (normed) histogram.
                 kde=False,
                 norm_hist=True, # norm_hist = norm_hist or kde or (fit is not None); 如果为False且kde=False, 则高度为频数
#                 kde_kws={"label": "density_est_by_sns",
#                          "bw": bin_w}
                 )
ax.grid(True)
ax.set_yticks(np.arange(0.16, step=0.01))


def func(x, a,b):     #一个指数函数
    return (1/(np.sqrt(2*np.pi)*a)) * np.exp(-((x-b)**2)/(2*a**2))
xdata = np.linspace(min(x),max(x), 10)

popt,pcov = curve_fit(func, xdata, bin_h)
y=[func(i,popt[0],popt[1])for i in xdata]
plt.plot(xdata,y,'r--')
print(popt[0],popt[1])

plt.title("Pre-check arrival time")
plt.xlabel("Interval of arrival time ")
plt.ylabel("Probability Density")
plt.axis([0,40,0,0.15])
plt.show()
