lst=eval(input())
for x in lst:
    k=lst.index(x)
    for s in range(2,x):
        if x//s!=0:
            pass
        else:
            lst.remove(x)
print(lst)
