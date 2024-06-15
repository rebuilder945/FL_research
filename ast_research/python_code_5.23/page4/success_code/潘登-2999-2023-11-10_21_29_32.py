import copy
a=str(input())
n,m=input().split()
b=copy.deepcopy(a)
b[n-1]=b[m-1]
b[m-1]=b[n-1]
print(b)
