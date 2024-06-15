def issu(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
def ishui(n):
    n=str(n)
    m=n[::-1]
    if m == n:
        return 1
    else:
        return 0
n=eval(input())
if (n-int(n)) > 0 or n<1:
    print("illegal input")
else: 
    for i in range(2,n):
        if issu(i) and ishui(i):
            print(i,end=" ")
