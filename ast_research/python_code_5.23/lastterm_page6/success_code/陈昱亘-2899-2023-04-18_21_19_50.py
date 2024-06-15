n,m=tuple(input().split(' '))
n=int(n)
m=int(m)
lst=[]
if n<=(m-3):
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    lst.append(a*100+b*10+c)
    result=' '.join(list(map(str,lst)))
    print(result)
else: print('illegal input')
