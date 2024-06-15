a=eval(input())
b=a.copy()
for i in a:
    if a.count(i)>=2:
        b.append(i)
print(b)

