def color(a,b):
    c = ['red','blue','yellow']
    ls1 = ['purple','orange','green']
    if a == b or a not in c or b not in c:
        return 'error'
    else:
        e = c.index(a)
        f = c.index(b)
        n = e + f
        return ls1[n - 1]





a = input()
b = input()
print(color(a,b))
