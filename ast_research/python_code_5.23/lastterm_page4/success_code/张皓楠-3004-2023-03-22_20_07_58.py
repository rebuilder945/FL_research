def su(x):
    ls = []
    i = x-1
    while i>1:
        if x%i == 0:
            ls.append(i)
            i-=1
    if len(ls)==0:
        return x
    elif x == 2:
        return x
a = eval(input())
for c in a:
    if not su(c):
        a.remove(c)
print(a)
