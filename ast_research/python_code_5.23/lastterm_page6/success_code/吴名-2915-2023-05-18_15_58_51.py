def s(n):
    n=list(str(n))
    a=0
    b=0
    c=len(n)
    d=len(n)
    for i in n:
        i=eval(i)
        d-=1
        a+=i**c
        b+=i*10**d
    if a==b and a>100:
        return True
n=eval(input())
flag=False
for i in range(n+1):
    if s(i):
        flag=True
        if i<=n:
            print(i)
if flag==False:
    print('none')
