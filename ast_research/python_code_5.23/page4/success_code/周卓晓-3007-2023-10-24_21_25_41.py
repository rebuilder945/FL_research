a= eval(input())
b=input().split(",")
n=int(b[0])
m=int(b[1])
del a[n:m]
print(a)
