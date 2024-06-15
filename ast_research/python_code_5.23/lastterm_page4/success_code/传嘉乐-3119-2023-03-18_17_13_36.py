l=eval(input())
for x in l:
    if l.count(x)>1:
        l.remove(x)
print(l)
