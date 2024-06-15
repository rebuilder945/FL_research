n = eval(input())
s = 0
if n <= 2:
    if n == 1:
        s = 2
    else:
        s = 2+3/2
else:
    f = 1
    a = 2
    b = 3
    i = 3
    while i<=n:
        d = f+a 
        e = a+b
        s = 2+3/2+e/d
        i +=1
print("%.4f"%(s))




