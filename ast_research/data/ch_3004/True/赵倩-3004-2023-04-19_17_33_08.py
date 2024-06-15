def f(x):
    d = 0
    for x1 in range(2,x):
        if x%x1==0:
            d+=1
    if x==1 or x==0:
        return 1
    elif d==0:
        return 0
    elif d!=0:
        return 1
a = eval(input())
b = []
for x in a:
    c = f(x)
    if c==0:
        b.append(x)
print(b)

