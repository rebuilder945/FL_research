a=list(eval(input()))
b=a.copy()
for i in b:
    if a.count(i)!=1:
        a.remove(i)
print(a)


