a = eval(input())
b = []
for i in a:
    b.append(i)
    if b.count(i)>1:
            b.remove(i)
print(b)
