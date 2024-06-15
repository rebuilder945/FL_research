ls=input().split(',')
s=[]
n,m=map(int,input().split(','))
if 0<=n<len(ls) or (-len(ls)<n<=-1):
    for i in range(m):
        ls.append(ls[n])
    for x in ls:
        x=int(x)
        s.append(x)
    print(s)
else:
    print('error')

