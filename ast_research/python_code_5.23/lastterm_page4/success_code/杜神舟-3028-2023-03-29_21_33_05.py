nml=input().split(",")
n,m,l=map(int,nml)
lst=[]
for i in range(m):
    lst.append(n+i*l)
print(*lst, sep=",")

