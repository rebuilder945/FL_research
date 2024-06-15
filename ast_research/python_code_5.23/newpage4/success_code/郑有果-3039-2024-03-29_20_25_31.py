m=eval(input())
a=max(m)
b=min(m)
for x in m:
    if x==a:
       m.remove(x)
    elif x==b:
       m.remove(x)
    else:
        pass
print(m)
