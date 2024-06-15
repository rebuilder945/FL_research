a=eval(input())
n,m=eval(input())
c=len(a)
if n in range(c)and m in range(c) :
    a1=a.copy()
    for i in range(n,m):
        d=a1[i]
        a.remove(d)
    print(a)
else:
    print('error')




