a=eval(input())
c=max(a)
b=min(a)
while c in a:
    a.remove(c)
while b in a:
    a.remove(b)
print(a)
