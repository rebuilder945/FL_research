ls=list(map(int,input().split(',')))
n,m=eval(input())
if n>len(ls)-1:
    print('error')
else:
    n=ls[n]
print(ls+[n]*m)

