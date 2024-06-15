n=eval(input())
b=max(n)
c=min(n)
if b in n:
    n.remove(b)
if c in n:
    n.remove(c)
print(n)
