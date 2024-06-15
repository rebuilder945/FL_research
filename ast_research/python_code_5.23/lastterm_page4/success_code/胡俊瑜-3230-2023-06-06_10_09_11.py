import random
a=eval(input())
b=sorted(a)
c=b[-1::-1]
c=[str(i) for i in c]
sep=""
d=int(sep.join(c))
print(d)

