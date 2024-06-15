ls1=eval(input())


ls=ls1[:]
n,m=map(int,input().split(','))

for i in range(n,m):
    if ls1[i]:
        del ls1[i]

if ls==ls1:
    print('error')
else:
    print(ls1)


