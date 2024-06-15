a=eval(input())
b=max(a)
c=min(a)
while (b or c) in a:
    a.remove(b or c)
print(a)
