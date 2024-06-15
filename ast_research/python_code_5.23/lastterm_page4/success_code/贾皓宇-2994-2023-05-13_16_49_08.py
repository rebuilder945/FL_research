a=list(eval(input()))
n,m=eval(input())
if n in range(-len(a),-1) or n in range(0,len(a)+1):
    for x in range(m):
        a.append(a[n])
    print(a)
else:
    print(error)
