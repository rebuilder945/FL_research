ls=map(int,input().split(','))
n,m=eval(input())
if n>=len(ls) or n<=-len(ls):
    print('error')
else:
    a=ls[n]
    lm=[a]
    ls1=ls+lm*m
    print(ls1)
