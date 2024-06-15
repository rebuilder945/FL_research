n,m,l=list(map(int,input().split(',')))
a=n+(m-1)*l
ls=[x for x in range(n,a+1,l)]
print(ls)
