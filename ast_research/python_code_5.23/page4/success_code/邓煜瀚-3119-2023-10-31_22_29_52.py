a=eval(input())
b=a.copy(a)
for i in a:
    if a.count(i)>=2:
        b.append(i)
print(b)

