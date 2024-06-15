a=list(eval(input()))
b=a[:]
for i in a:
    if b.count(i)>1:
        b.remove(i)
print(b)
