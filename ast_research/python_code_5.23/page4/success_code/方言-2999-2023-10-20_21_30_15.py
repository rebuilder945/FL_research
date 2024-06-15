p=input().split()
o=input().split()
m=o[0]
n=o[1]
cd=p[int(n)]
p[int(n)]=p[int(m)]
p[int(m)]=cd
print(p)
