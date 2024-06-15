a=eval(input())
for i in a:
    if i==0:
        a.append(i)
        a.pop(a.index(i))
print(a)
