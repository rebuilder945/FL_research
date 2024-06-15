a=eval(input())
d=max(a)
x=min(a)
b=[]
for y in a:
    if y!=d and y!=x:
        b.append(y)
print(b)

