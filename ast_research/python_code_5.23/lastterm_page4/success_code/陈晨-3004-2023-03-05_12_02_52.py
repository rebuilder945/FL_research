lst=eval(input())
lst.remove(1)
for x in lst:
    k=lst.index(x)
    for s in range(2,x):
        if x%s!=0:
            pass
        else:
            del lst[x]
print(lst)
