a=eval(input())
b=max(a)
s=min(a)
while b in a:
    a.remove(b)
while s in a:
    a.remove(s)
print(a)
