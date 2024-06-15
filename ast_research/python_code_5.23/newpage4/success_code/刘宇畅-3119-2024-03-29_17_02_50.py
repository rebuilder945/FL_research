a=eval(input())
for i in a:
    if a.count(i)>=2:
        a.remove(i)
print(a)
