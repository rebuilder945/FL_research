a=list(input())
b=input().split(",")
n=b[0],m=b[1]
a.pop(n)
c=b[n]*m
a.append(c)
print(a)
