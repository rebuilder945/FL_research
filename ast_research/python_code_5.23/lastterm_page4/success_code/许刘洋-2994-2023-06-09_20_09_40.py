a=list(input())
b=list(input().split(","))
n=int(b[0])
m=int(b[1])
a.pop(n)
c=b[n]*m
a.append(c)
print(a)
