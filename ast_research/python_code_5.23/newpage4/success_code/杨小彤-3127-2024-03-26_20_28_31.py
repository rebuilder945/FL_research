from distutils.log import error
from re import A


n = eval(input())
a = [x for x in range(1,n+1)]
b = 1
for i in a:
     if i == n:
        a = [x for x in range(2,n+1)]
        c = a.append(b)
        print(a)
