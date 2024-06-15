import numpy as np
import matplotlib.pyplot as plt
x=int(input())
y=int(input())
a=int(input())
b=int(input())
plt.plot(x,y)
plt.show()
d=[(x-a)*(x-a)+(y-b)*(y-b)]^1/2
print("{:.2f}".format(d))
