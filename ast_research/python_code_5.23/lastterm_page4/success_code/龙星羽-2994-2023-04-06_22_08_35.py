ls=input().split(',')
n,m=eval(input())
if n>=len(ls) or n<=-len(ls):
    print('error')
else:
    a=ls[n]
    lm=[a]
    ls1=list(map(int,ls+lm*m))
    print(ls1)
