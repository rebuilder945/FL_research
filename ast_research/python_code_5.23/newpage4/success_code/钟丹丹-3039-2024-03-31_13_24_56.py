n = eval(input())
a=max(n)
b=min(n)
for x in n:
    if n.count(a)>0:
        n.remove(a)
    elif n.count(b)>0:
        n.remove(b)
print(n)

