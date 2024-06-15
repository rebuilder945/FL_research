ls=list(input().split(','))
n,m=eval(input())
if n>+len(ls) or n<len(ls)*(-1):
    print('error')
else:
    ls1=[ls[n]]*m
    print(ls+ls1)
