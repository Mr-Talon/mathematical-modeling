import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("needList.xlsx")
x = np.array(data).reshape(-1).tolist()

s = []
t = []
p = []
x_ans = []
s0 = x[0]
t0 = x[1] - x[0]
p0 = 0
alpha = 0.9
beta = 0.0
gamma = 0.1
T = 4

for i in range(len(x)):
    if i < T:
        if i == 0:
            s.append(alpha * (x[i] - p0) + (1 - alpha) * (s0 + t0))
            t.append(beta * (s[i] - s0) + (1 - beta) * t0)
            p.append(gamma * (x[i] - s[i]) + (1 - gamma) * p0)
        else:
            s.append(alpha * (x[i] - p0) + (1 - alpha) * (s[i - 1] + t[i - 1]))
            t.append(beta * (s[i] - s[i - 1]) + (1 - beta) * t[i - 1])
            p.append(gamma * (x[i] - s[i]) + (1 - gamma) * p0)
    else:
        s.append(alpha * (x[i] - p[i - T]) + (1 - alpha) * (s[i - 1] + t[i - 1]))
        t.append(beta * (s[i] - s[i - 1]) + (1 - beta) * t[i - 1])
        p.append(gamma * (x[i] - s[i]) + (1 - gamma) * p[i - T])
    if i < T:
        x_ans.append(s[i] + p0)
    else:
        x_ans.append(s[i] + p[i - T])

# x2=[]
# for h in range(112 - len(x)):
#     x_ans.append(s[103+h] + t[103+h] + p[103 - T + h])
#     x2.append(x_ans[104+h])
#
#     s.append(alpha * (x2[h] - p[103 + h - T]) + (1 - alpha) * (s[103 + h - 1] + t[103 + h - 1]))
#     t.append(beta * (s[103 + h] - s[103 + h - 1]) + (1 - beta) * t[103 + h - 1])
#     p.append(gamma * (x2[h] - s[103 + h]) + (1 - gamma) * p[103 + h - T])

t = np.arange(1, 105)
t2 = np.arange(1, 105 + 8)

x_ans1=[102,112,101,101,106,116,105,105,110]
x_down=[102.00,105.81,91.70,90.31,93.80,102.52,89.47,88.75,92.72]
x_up=[102.00,118.96,109.41,111.63,118.21,130.26,119.66,121.21,127.30]
print(len(x_ans))

plt.xlabel("weeks/w")
plt.ylabel('Needs')
plt.title('Demand forecast curve')
plt.grid(True)
plt.plot(t, x,label='label',linewidth=3)
plt.plot(t2[-9:], x_ans1,label="forecast",linewidth=3)
plt.plot(t2[-9:],x_up,'-.',color='gray')
plt.plot(t2[-9:],x_down,'-.',color='gray')
plt.legend()
plt.show()
