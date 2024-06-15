#n,m,l=list(map(int,input().split(',')))
n,m,l=eval(input())
ls=[n+i*l for i in range(m)]
print(ls)
