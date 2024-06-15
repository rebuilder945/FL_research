l=eval(input())
a=max(l)
b=min(l)
while a in l:
    l.remove(a)
while b in l:
    l.remove(b)
print(l)
