ls=input().split(',')
ls=list(map(int,ls))
n,m=eval(input())
if n>=0 and n>=len(ls):
    print('error')
elif n<0 and (-n)>=len(ls):
    print('error')
else:
    a=ls[n]
    for i in range(m):
        ls+=a
    print(ls)
