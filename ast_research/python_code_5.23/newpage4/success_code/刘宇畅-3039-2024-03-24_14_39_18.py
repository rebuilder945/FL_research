a=eval(input())
b=max(a)
c=min(a)
while b in a:
    a.remove(max(a))
while c in a:
    a.remove(min(a))
print(a)
