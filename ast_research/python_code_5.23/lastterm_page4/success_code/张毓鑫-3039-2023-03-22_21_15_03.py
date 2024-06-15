a=eval(input())
b=max(a)
c=min(a)
while b in a:
    a=a.remove(b)
while c in a:
    a=a.remove(b)
print(a)
