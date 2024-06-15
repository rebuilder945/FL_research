ls=input().split(',')
s=[]
n,m=map(int,input().split(','))
if 0<=n<len(ls):
    for i in range(m):
        ls.append(ls[n-1])
    for x in ls:
        x=int(x)
        s.append(x)
    print(s)
elif n>=len(ls):
    print('error')

