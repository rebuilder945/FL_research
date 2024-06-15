import copy
a=str(input())
n,m=eval(input())
b=copy.deepcopy(a)
b[n-1]=m-1
b[m-1]=n-1
print(b)
