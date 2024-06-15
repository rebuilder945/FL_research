a = eval(input()) 
for i in a:
    if max(a) == i:
        a.remove(i)
    elif min(a) == i:
        a.remove(i)
print(a)
