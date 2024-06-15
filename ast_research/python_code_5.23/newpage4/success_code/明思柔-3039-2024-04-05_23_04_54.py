a=eval(input())
b=max(a)
c=min(a)
while (b or c) in a:
    a.remove(b)
    a.remove(c)
print(a)
