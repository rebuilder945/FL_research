ls=input().split(',')
for i in range(len(ls)):
    ls[i]=int(ls[i])
n,m=eval(input())
if n >len(ls):
    print('error')
else:
    a=ls[n]
    for i in range(m):
        ls.append(a)
    print(ls)

