ls=list(eval(input()))
n,m=eval(input())
if 0<=abs(n)<len(ls):
    a=ls[n]
    i=0
    while i<m:
        ls.append(a)
        i=i+1
    print(ls)
else:
    print('error')
