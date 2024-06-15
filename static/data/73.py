m, n, l = eval(input())
t = m + (n - 1) * l

import numpy as np

a = np.linspace(m, t, n)
c = a.tolist()  
#在 eval() 函数中传递了包含空字节的字符串。
#使用 a.tolist() 方法来将 numpy 数组 a 转换为列表 c，这样可以避免直接使用 eval() 函数来处理 numpy 数组。

print(c)