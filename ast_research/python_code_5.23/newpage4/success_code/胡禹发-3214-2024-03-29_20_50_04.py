a=list(eval(input()))
b=list(a.count(0))
a.remove(0)
for i in b:
    a.append(i)
print(a)

