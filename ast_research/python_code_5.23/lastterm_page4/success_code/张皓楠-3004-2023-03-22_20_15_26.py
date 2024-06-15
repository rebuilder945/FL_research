def su(x):
    if x>2:
        ls = []
        for i in range(x-1,1,-1):
            if x%i == 0:
                ls.append(i)
        if len(ls)==0 and x!=1:
            return x
    elif x == 2:
        return x
a = eval(input())
for c in a:
    if not su(c):
        a.remove(c)
print(a)
