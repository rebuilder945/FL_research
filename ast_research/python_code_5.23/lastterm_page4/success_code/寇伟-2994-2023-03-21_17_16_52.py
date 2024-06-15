ls=input().split(',')
n,m=map(int,input().split(','))
if 0<=n<len(ls):
    for i in range(m):
        ls.append(ls[n-1])
    print(ls)
elif n>=len(ls):
    print('error')

