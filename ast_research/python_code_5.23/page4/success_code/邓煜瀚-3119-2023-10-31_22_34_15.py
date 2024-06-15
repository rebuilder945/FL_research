a=eval(input())
c=a.copy()
for i in a:
    for i in range(a.count(i)):
        if a.count(i)>=2:
            a.append(i)
print(a)

