ls=list(input().split(','))
n,m=eval(input())
a=[]
if n<len(ls):
    a.append(ls[n])
    a=a*m
    del ls[n]
    print(ls+a)
else:
    print("error")

