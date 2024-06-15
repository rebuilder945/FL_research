a=list(input().split(','))
n,m=eval(input())
c=len(a)
if n>=(c*1) or n<=(-1*c):
    print("error")
else:
    b=a.pop(n)
    for i in range(m):
        a.append(b)
    print(a)
