import numpy as np

average = 9894.106

def func(t):  # 污水排放回归方程
    return 12.864 * t + 149


put2 = (20 - (-5.493799 - 0.000993 * average)) / 0.137599  # 二类干流应该的排污量
put3 = (0 - (-10.361764 - 0.000334 * average)) / 0.074253  # 三类干流应该的排污量

x=np.arange(11,21)
print(func(x)-min(put2,put3))