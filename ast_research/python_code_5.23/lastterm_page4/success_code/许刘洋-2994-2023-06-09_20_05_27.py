a=list(input())
b=list(input().split(","))
n=b[0],m=b[1]
a.pop(n)
c=b[n]*m
a.append(c)
print(a)
