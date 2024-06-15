n=eval(input())
b=max(n)
c=min(n)
x=[i for i,t in enumerate(n)if t==b]
for m in x:
    n.pop(m)
p=[o for o,l in enumerate(n)if l==c]
for u in p:
    n.pop(u)
print(n)
