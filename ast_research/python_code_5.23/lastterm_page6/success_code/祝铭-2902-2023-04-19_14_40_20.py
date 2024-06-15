def seq(n):
    a = 0
    for i in range(n):
        a += f(i+2)/f(i+1)
    print("%.4f"%(a))
def f(y):
    pv=1
    ppv=1
    for i in range(y):
        if i<1:
            value=1
        else:
            value=pv+ppv
            pv=ppv
            ppv=value
    return value

num = int(input())
seq(num)
