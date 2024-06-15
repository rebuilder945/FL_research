n = eval(input())
a=max(n)
b=min(n)
for x in n:
    if n.count(a)>0 or n.count(b)>0:
        n.remove(a)
        n.remove(b)
print(n)

