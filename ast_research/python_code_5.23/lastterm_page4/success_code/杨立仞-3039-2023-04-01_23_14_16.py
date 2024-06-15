a=eval(input())
d=max(a)
x=min(a)
for y in a:
    if y==max(a) or y==min(a):
        a.remove(y)
print(a)

