a=list(eval(input()))
for i in a:
    if a.count(i)!=1:
        a.remove(i)
        i=i-1
print(a)
