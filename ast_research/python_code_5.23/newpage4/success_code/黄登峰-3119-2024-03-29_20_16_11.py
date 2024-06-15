a=eval(input())
for i in a:
    x=a.count(i)
    if x!=1:
        a.remove(i)
    else:
        continue
print(a)
