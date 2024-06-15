def f(x):
    return x != 1 and all( x%1 != 0 for i in range(2,x) )

def g(x):
    return str(x) == str(x)[::-1]

def h(x):
    return f(x) and g(x)

n=input()

if n.find('.') !=-1 or int(n) <=0:
    print("illegal input")
else:
    n=int(n)
    print(*filter(h,range(1,n+1)))
