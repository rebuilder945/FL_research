num=list(eval(input()))
n,m=eval(input())
if n<len(num):
    x=num[n]
    b=[x]
    c=num+b*m
    print(c)
else:
    print('error')
