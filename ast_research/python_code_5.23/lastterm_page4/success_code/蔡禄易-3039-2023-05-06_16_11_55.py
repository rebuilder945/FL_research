a = eval(input()) 
for i in a:
    if max(a) == i:
        a.remove(i)
for i in a:
    if min(a) == i:
        a.remove(i)
print(a)
