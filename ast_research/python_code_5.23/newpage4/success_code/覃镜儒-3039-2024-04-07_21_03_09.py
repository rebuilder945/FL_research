l=eval(input())
a=max(l)
b=min(l)
n=l.copy()
for i in l:
    if i==a or i==b:
        n.remove(i)
print(n)
