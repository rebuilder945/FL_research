n=eval(input())
a=max(n)
b=min(n)
for x in n:
    if x==a or x==b:
       n.remove(a)
       n.remove(b)


print(n)
