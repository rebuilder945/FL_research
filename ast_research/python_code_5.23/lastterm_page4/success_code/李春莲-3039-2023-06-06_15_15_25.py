l=eval(input())
a=max(l)
b=min(l)
for i in l:
    if i==a or i==b:
        l.remove(i)
    else:
        pass
print(l)
