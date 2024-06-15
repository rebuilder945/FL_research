lst=eval(input())
for i in lst:
    if i>2:
        for x in range(2,i):
            if i%x==0:
                lst.remove(i)
    else:
        if i<2:
            lst.remove(i)
        elif i==2:
            pass
print(lst)
