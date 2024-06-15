l=eval(input())
for i in l:
    for x in l:
        if x==i in l:
            del l[i]
        else:
            pass
print(l)
