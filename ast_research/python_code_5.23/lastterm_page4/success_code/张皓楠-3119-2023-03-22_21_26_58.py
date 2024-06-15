a = eval(input())
b = []
for i in a:
    b.append(i)
for i in a:
    if a.count(i)>1:
        for x in range(a.count(i)-1):
            b.remove(i)
print(b)
