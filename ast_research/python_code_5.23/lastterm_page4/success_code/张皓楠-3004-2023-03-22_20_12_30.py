def su(x):
    if x>2:
        ls = []
        for i in range(2,x):
            if x%i == 0:
                ls.append(i)
        if len(ls)==0:
            return x
    elif x == 2:
        return x
a = eval(input())
for c in a:
    if not su(c):
        a.remove(c)
print(a)
