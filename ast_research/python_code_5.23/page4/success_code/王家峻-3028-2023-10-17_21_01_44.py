m,n,l=eval(input())
t=m+(n-1)*l
import numpy as np
a= np.linspace(m,t,n)
c=list(map(int,a))
print(c)

