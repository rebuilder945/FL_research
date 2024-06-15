a=eval(input())
b=min(a)
c=max(a)
while b in a:
    a.remove(b)
while c in a:
    a.remove(c)
print(a)
