a=list(eval(input()))
n,m=map(int,input().split(","))
e=[a.pop(n-1)]*m
print(a+e)

