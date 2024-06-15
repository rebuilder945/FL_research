m=input().split()
c=list(input())
a,b=c[0],c[2]
m[int(a)],m[int(b)]=m[int(b)],m[int(a)]
print(m)
