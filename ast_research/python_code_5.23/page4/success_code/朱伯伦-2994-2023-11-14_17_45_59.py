ls=input().split(',')
n,m=eval(input())
if n >len(ls) or n<0:
    print('error')
else:
    a=ls.pop(n)
    for i in range(m):
        ls.append(a)
    print(ls)

