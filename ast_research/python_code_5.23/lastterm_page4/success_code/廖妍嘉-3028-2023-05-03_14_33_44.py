n,m,l=eval(input())
ls=[]
for i in range(n,n+m*l):
    ls.append(i)
    ls2=ls[0:len(ls):l]
print(ls2)
