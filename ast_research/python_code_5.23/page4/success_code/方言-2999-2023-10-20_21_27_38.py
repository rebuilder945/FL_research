p=input().split()
o=input().split()
m=o[0]
n=o[1]
cd=p[n]
p[n]=p[m]
p[m]=cd
print(p)
