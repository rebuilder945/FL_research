n,m,l=map(int,input().split(","))
a=n+(m-1)*l+1
b=[]
for i in range(n,a,l):
    b.append(i)
print(b)
