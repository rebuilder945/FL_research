a=eval(input())
d=max(a)
x=min(a)

for y in a:
    if y==d or y==x:
        a.remove(y)
print(a)

