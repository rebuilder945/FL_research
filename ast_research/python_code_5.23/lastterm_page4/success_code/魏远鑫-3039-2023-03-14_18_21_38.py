a=eval(input())
c=max(a)
while c in a:
    a.remove(c)
b=min(a)
while b in a:
    a.remove(b)
print(a)
