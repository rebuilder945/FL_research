a = eval(input()) 
for i in a:
    if max(a) == i:
        del a[i]
    elif min(a) == i:
        del a[i]
print(a)
