a = list(map(int,input().split(',')))
N,M=eval(input())
nb = []
if N<len(a)-1:
    for x in range(M):
        nb.append(a[N])
    a = a+nb
    print(a)
else:
    print('error')


