a=eval(input())
b=max(a)
while b in a:
    a.remove(b)
if a==[]:
    print(a)
else:
    c=min(a)
    while c in a:
        a.remove(c)
    print(a)
