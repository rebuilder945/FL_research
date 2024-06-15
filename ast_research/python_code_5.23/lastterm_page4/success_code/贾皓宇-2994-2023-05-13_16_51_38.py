a=list(eval(input()))
n,m=eval(input())
if n in range(-len(a),-1) or n in range(0,len(a)+1):
    b=a[n]
    for x in range(m):
        a.append(b)
    print(a)
else:
    print('error')
