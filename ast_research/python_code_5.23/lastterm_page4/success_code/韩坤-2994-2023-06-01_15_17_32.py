a=list(map(int,input().split(",")))
n,m=map(int,input().split(","))
if n>len(a)-1 or n<(-1)*len(a):
    print("error")
else:
    b=[a[n]]*m
    a.append(b)
    print(a)
